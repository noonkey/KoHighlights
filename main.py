# coding=utf-8
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals
import codecs
import os
import re
import wx, wx.html
import gui

__author__ = 'noonkey'
__version__ = '0.1'


class DragAndDrop(wx.FileDropTarget):
    def __init__(self, text_field):
        wx.FileDropTarget.__init__(self)
        self.text_field = text_field
        self.dropped_files_list = []

    # noinspection PyMethodOverriding
    def OnDropFiles(self, x, y, filenames):
        if len(filenames) == 1:
            if os.path.isfile(filenames[0]):
                frame.get_highlights(filenames[0])
        else:
            self.dropped_files_list = []
            for filename in filenames:
                if os.path.splitext(filename)[1] == '.lua':
                    self.dropped_files_list.append(filename)
            frame.dropped_files = len(self.dropped_files_list)
            frame.batch_dialog.ShowModal()


class KoHighlightsMainFrame(gui.MainFrame):
    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)
        path = os.path.abspath("./stuff/icon.png")
        self.SetIcon(wx.Icon(path, wx.BITMAP_TYPE_PNG))
        self.dropped_files = 0
        self.converted_files = 0
        self.highlights = []
        self.current_text_name = ''

        self.drop = DragAndDrop(self.text_field)
        self.text_field.SetDropTarget(self.drop)
        self.batch_dialog = BatchDialog(self)
        self.batch_results = BatchResults(self)
        self.about = About(self)

    def get_highlights(self, filename, display_results=True):
        """ Gets the highlights from the KoReader History File.
        :type filename: str|unicode
        :param filename: path to file
        """
        self.text_field.Clear()
        file_name_full = os.path.split(filename)[1]
        try:
            file_name = file_name_full.split('#] ')[1]
            file_name_no_ext = os.path.splitext(file_name)[0]
            self.SetTitle('KoHighlights: ' + file_name_no_ext)
            location = file_name_full.split('#] ')[0][1:].replace('#', '/') + '/'
            self.current_text_name = os.path.splitext(file_name_no_ext)[0]
            if display_results:
                self.text_field.WriteText(location + '\n' + file_name_no_ext + '\n\n')
        except IndexError:
            self.SetTitle('KoHighlights: ' + os.path.splitext(file_name_full)[0])
            self.current_text_name = os.path.splitext(file_name_full)[0]
            if display_results:
                self.text_field.WriteText(os.path.splitext(file_name_full)[0] + '\n\n')
        with codecs.open(filename, 'r', encoding='utf-8') as lua_file:
            lua_text = lua_file.read().replace('\\', '')
            highlight_text = re.compile(r'\["text"\] = "(.+?)"', re.DOTALL)
            phrases = re.findall(highlight_text, lua_text)
            bookmark_text = re.compile(r'\["text"\] = "(Page \d+? .+? @ \d+?-\d+?-\d+? '
                                       r'\d+?:\d+?:\d+?)"', re.DOTALL)
            bookmarks = re.findall(bookmark_text, lua_text)
            self.highlights = []
            for phrase in phrases:
                if phrase not in bookmarks:
                    self.highlights.append(phrase)
            if display_results:
                if self.highlights:
                    for phrase in self.highlights:
                        self.text_field.WriteText(phrase + '\n\n')
                    self.text_field.SetInsertionPoint(0)
                else:
                    self.text_field.WriteText('No Highlights Found...')

    def on_open_file(self, event):
        """ Open a KoReader History File via a 'file selector' dialog.
        """
        wildcard = 'KoReader History Files|*.lua|All files (*.*)|*.*'
        dialog = wx.FileDialog(self, "Open KoReader History File", wildcard=wildcard,
                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dialog.ShowModal() == wx.ID_OK:
            filename = dialog.GetPaths()[0]
            self.get_highlights(filename)
        dialog.Destroy()

    def on_save_file(self, event):
        """ Saves the current text as text file.
        """
        wildcard = 'text files (*.txt)|*.txt|All files (*.*)|*.*'
        dialog = wx.FileDialog(self, "Select filename for the text file",
                               wildcard=wildcard,
                               style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        dialog.SetFilename(self.current_text_name)
        # dialog.SetFilename(os.path.splitext(self.current_text_name)[0])
        if dialog.ShowModal() == wx.ID_OK:
            filename = dialog.GetPaths()[0]
            if self.highlights:
                with codecs.open(filename, 'w+', encoding='utf-8') as text_file:
                    for highlight in self.highlights:
                        text_file.write(highlight + '\n\n')
            else:
                wx.MessageBox("Nothing to save!", style=wx.ICON_QUESTION | wx.OK)
            dialog.Destroy()

    # noinspection PyUnboundLocalVariable
    def on_dir(self, event):
        """ Chose directory to batch process.
        """
        source_dialog = wx.DirDialog(self, "Choose a directory with some Koreader "
                                           "History files", style=wx.DD_DEFAULT_STYLE)
        if source_dialog.ShowModal() == wx.ID_OK:
            source_path = source_dialog.GetPath()
        else:
            return
        source_dialog.Destroy()
        dest_dialog = wx.DirDialog(self, "Choose a directory for the converted files",
                                   style=wx.DD_DEFAULT_STYLE)
        if dest_dialog.ShowModal() == wx.ID_OK:
            dest_path = dest_dialog.GetPath()
        else:
            return
        dest_dialog.Destroy()
        current_path, _, files = os.walk(source_path).next()
        frame.dropped_files = len(files)
        for name in files:
            filename = os.path.join(current_path, name)
            frame.drop.dropped_files_list.append(filename)
        self.batch_dialog.on_batch(None, dest_path)

    def on_about(self, event):
        self.about.ShowModal()

    def exit_app(self, event):
        """ When the 'Exit' button is pressed.
        """
        self.Close()


class BatchDialog(gui.BatchDialog):
    """ The Batch Dialog window.
    """
    def __init__(self, parent):
        gui.BatchDialog.__init__(self, parent)
        path = os.path.abspath("./stuff/icon.png")
        icon = wx.Icon(path, wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)

    def on_batch(self, event, dest=None):
        """ Process many dropped files.
        """
        frame.converted_files = 0
        for filename in frame.drop.dropped_files_list:
            file_dir, file_name_full = os.path.split(filename)
            try:
                file_name = file_name_full.split('#] ')[1]
                file_name_no_ext = os.path.splitext(file_name)[0]
            except IndexError:
                file_name_no_ext = os.path.splitext(file_name_full)[0]
            frame.get_highlights(filename, False)
            if frame.highlights:
                if dest:
                    file_name = os.path.join(dest, file_name_no_ext) + '.txt'
                else:
                    file_name = os.path.join(file_dir, file_name_no_ext) + '.txt'
                with codecs.open(file_name, 'w+', encoding='utf-8') as text_file:
                    for highlight in frame.highlights:
                        text_file.write(highlight + '\n\n')
                    frame.converted_files += 1
        self.Close()
        if dest:
            text = 'Processed {} Koreader files\nNo highlights in {} files\n' \
                   'Converted {} files'.format(frame.dropped_files, (frame.dropped_files -
                                               frame.converted_files),
                                               frame.converted_files)
        else:
            text = 'Dropped {} Koreader files\nNo highlights in {} files\n' \
                   'Converted {} files'.format(frame.dropped_files, (frame.dropped_files -
                                               frame.converted_files),
                                               frame.converted_files)
        frame.batch_results.results_text.SetLabelText(text)
        frame.batch_results.Show()


class BatchResults(gui.BatchResults):
    """ The Batch Results info window.
    """
    def __init__(self, parent):
        gui.BatchResults.__init__(self, parent)
        path = os.path.abspath("./stuff/icon.png")
        icon = wx.Icon(path, wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)


class About(gui.About):
    """ The About window.
    """
    def __init__(self, parent):
        gui.About.__init__(self, parent)
        path = os.path.abspath("./stuff/icon.png")
        icon = wx.Icon(path, wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)

        about = """<html>
        <span class="style1"></span>
        <center>
          <table width="100%" height="100%" border="0">
            <tr>
              <td height="10%">&nbsp;</td>
            </tr>
            <tr>
              <td height="128"><table width="100%" height="100" border="0">
                <tr>
                  <td width="10%">&nbsp;</td>
                  <td width="128" height="128"><img src="stuff/logo.png" width="128" height="128"></td>
                  <td><p align="center"><b>KoHighlights</b> is a  utility for converting the Koreader's history files to simple text. </p>
                  <p align="center">Version <b>{}</b></p></td>
                  <td width="10%">&nbsp;</td>
                </tr>
              </table></td>
            </tr>
            <tr>
              <td height="10%">&nbsp;</td>
            </tr>
          </table>
        </center>
        </body>
        </html>
        """.format(__version__)
        self.about_text.SetPage(about)


if __name__ == '__main__':
    app = wx.App(False)
    frame = KoHighlightsMainFrame(None)
    frame.Show(True)
    app.MainLoop()
