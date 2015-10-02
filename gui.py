# -*- coding: utf-8 -*- 

###########################################################################
# Python code generated with wxFormBuilder (version Jun 17 2015)
# http://www.wxformbuilder.org/
#
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.html


###########################################################################
# Class MainFrame
###########################################################################

class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"KoHighlights",
                          pos=wx.DefaultPosition, size=wx.Size(640, 480),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.Size(140, 240), wx.DefaultSize)
        self.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        sizer_main = wx.BoxSizer(wx.VERTICAL)

        self.text_field = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        sizer_main.Add(self.text_field, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(sizer_main)
        self.Layout()
        self.menu_bar = wx.MenuBar(0)
        self.menu_file = wx.Menu()
        self.m_open = wx.MenuItem(self.menu_file, wx.ID_ANY, u"&Open file\tCtrl-O",
                                  wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_file.AppendItem(self.m_open)

        self.m_save = wx.MenuItem(self.menu_file, wx.ID_ANY, u"&Save file\tCtrl-S",
                                  wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_file.AppendItem(self.m_save)

        self.m_open_dir = wx.MenuItem(self.menu_file, wx.ID_ANY,
                                      u"Process &Directory\tCtrl-D", wx.EmptyString,
                                      wx.ITEM_NORMAL)
        self.menu_file.AppendItem(self.m_open_dir)

        self.menu_file.AppendSeparator()

        self.m_exit = wx.MenuItem(self.menu_file, wx.ID_ANY, u"Exit\tCtrl-Q",
                                  wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_file.AppendItem(self.m_exit)

        self.menu_bar.Append(self.menu_file, u"&File")

        self.menu_help = wx.Menu()
        self.m_about = wx.MenuItem(self.menu_help, wx.ID_ANY, u"&About", wx.EmptyString,
                                   wx.ITEM_NORMAL)
        self.menu_help.AppendItem(self.m_about)

        self.menu_bar.Append(self.menu_help, u"&Help")

        self.SetMenuBar(self.menu_bar)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.on_open_file, id=self.m_open.GetId())
        self.Bind(wx.EVT_MENU, self.on_save_file, id=self.m_save.GetId())
        self.Bind(wx.EVT_MENU, self.on_dir, id=self.m_open_dir.GetId())
        self.Bind(wx.EVT_MENU, self.exit_app, id=self.m_exit.GetId())
        self.Bind(wx.EVT_MENU, self.on_about, id=self.m_about.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_open_file(self, event):
        event.Skip()

    def on_save_file(self, event):
        event.Skip()

    def on_dir(self, event):
        event.Skip()

    def exit_app(self, event):
        event.Skip()

    def on_about(self, event):
        event.Skip()


###########################################################################
# Class BatchDialog
###########################################################################

class BatchDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Batch Convertion",
                           pos=wx.DefaultPosition, size=wx.DefaultSize,
                           style=wx.DEFAULT_DIALOG_STYLE | wx.STAY_ON_TOP)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        sizer_4batch = wx.BoxSizer(wx.VERTICAL)

        sizer_4batch_text = wx.BoxSizer(wx.HORIZONTAL)

        self.batch_icon = wx.StaticBitmap(self, wx.ID_ANY,
                                          wx.ArtProvider.GetBitmap(wx.ART_QUESTION, ),
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        sizer_4batch_text.Add(self.batch_icon, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.batch_text = wx.StaticText(self, wx.ID_ANY,
                                        u"Would you like to convert the droped files?",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        self.batch_text.Wrap(-1)
        sizer_4batch_text.Add(self.batch_text, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        sizer_4batch.Add(sizer_4batch_text, 1, wx.EXPAND, 5)

        sizer_4batch_btn = wx.BoxSizer(wx.HORIZONTAL)

        sizer_4batch_btn.AddSpacer((0, 0), 1, 0, 5)

        self.batch_cancel = wx.Button(self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        sizer_4batch_btn.Add(self.batch_cancel, 0, wx.ALL, 5)

        sizer_4batch_btn.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        self.batch_ok = wx.Button(self, wx.ID_OK, u"OK", wx.DefaultPosition,
                                  wx.DefaultSize, 0)
        self.batch_ok.SetDefault()
        sizer_4batch_btn.Add(self.batch_ok, 0, wx.ALL, 5)

        sizer_4batch_btn.AddSpacer((0, 0), 1, 0, 5)

        sizer_4batch.Add(sizer_4batch_btn, 1, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        self.SetSizer(sizer_4batch)
        self.Layout()
        sizer_4batch.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.batch_ok.Bind(wx.EVT_BUTTON, self.on_batch)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_batch(self, event):
        event.Skip()


###########################################################################
# Class BatchResults
###########################################################################

class BatchResults(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Batch Results",
                           pos=wx.DefaultPosition, size=wx.DefaultSize,
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        sizer_4results = wx.BoxSizer(wx.VERTICAL)

        sizer_4result_text = wx.BoxSizer(wx.HORIZONTAL)

        self.results_icon = wx.StaticBitmap(self, wx.ID_ANY, wx.ArtProvider.GetBitmap(
            wx.ART_INFORMATION, ), wx.DefaultPosition, wx.DefaultSize, 0)
        sizer_4result_text.Add(self.results_icon, 0,
                               wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, 5)

        self.results_text = wx.StaticText(self, wx.ID_ANY,
                                          u"Dropped        Koreader files\nNo "
                                          u"highlights in        files\nConverted       "
                                          u" files", wx.DefaultPosition, wx.DefaultSize,
                                          0)
        self.results_text.Wrap(-1)
        sizer_4result_text.Add(self.results_text, 1,
                               wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, 5)

        sizer_4results.Add(sizer_4result_text, 1, wx.EXPAND, 5)

        sizer_4results_btn = wx.BoxSizer(wx.HORIZONTAL)

        sizer_4results_btn.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        self.results_ok = wx.Button(self, wx.ID_CANCEL, u"OK", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        sizer_4results_btn.Add(self.results_ok, 0, wx.ALL, 5)

        sizer_4results_btn.AddSpacer((0, 0), 1, 0, 5)

        sizer_4results.Add(sizer_4results_btn, 1, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        self.SetSizer(sizer_4results)
        self.Layout()
        sizer_4results.Fit(self)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


###########################################################################
# Class About
###########################################################################

class About(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"About KoHighlights",
                           pos=wx.DefaultPosition, size=wx.Size(440, 360),
                           style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        sizer_4about = wx.BoxSizer(wx.VERTICAL)

        self.about_notebook = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.info_panel = wx.Panel(self.about_notebook, wx.ID_ANY, wx.DefaultPosition,
                                   wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizer_4info = wx.BoxSizer(wx.VERTICAL)

        self.about_text = wx.html.HtmlWindow(self.info_panel, wx.ID_ANY,
                                             wx.DefaultPosition, wx.DefaultSize,
                                             wx.html.HW_NO_SELECTION | 
                                             wx.html.HW_SCROLLBAR_AUTO)
        self.about_text.Hide()

        sizer_4info.Add(self.about_text, 1, wx.ALL | wx.EXPAND, 5)

        self.info_panel.SetSizer(sizer_4info)
        self.info_panel.Layout()
        sizer_4info.Fit(self.info_panel)
        self.about_notebook.AddPage(self.info_panel, u"About", True)
        self.usage_panel = wx.Panel(self.about_notebook, wx.ID_ANY, wx.DefaultPosition,
                                    wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizer_4usage = wx.BoxSizer(wx.VERTICAL)

        self.usage_text = wx.html.HtmlWindow(self.usage_panel, wx.ID_ANY,
                                             wx.DefaultPosition, wx.DefaultSize,
                                             wx.html.HW_NO_SELECTION |
                                             wx.html.HW_SCROLLBAR_AUTO)
        sizer_4usage.Add(self.usage_text, 1, wx.ALL | wx.EXPAND, 5)

        self.usage_panel.SetSizer(sizer_4usage)
        self.usage_panel.Layout()
        sizer_4usage.Fit(self.usage_panel)
        self.about_notebook.AddPage(self.usage_panel, u"Usage", False)

        sizer_4about.Add(self.about_notebook, 1, wx.EXPAND | wx.ALL, 5)

        sizer_4about_btn = wx.BoxSizer(wx.HORIZONTAL)

        sizer_4about_btn.AddSpacer((0, 0), 1, 0, 5)

        self.about_ok = wx.Button(self, wx.ID_OK, u"OK", wx.DefaultPosition,
                                  wx.DefaultSize, 0)
        sizer_4about_btn.Add(self.about_ok, 0, wx.ALL, 5)

        sizer_4about_btn.AddSpacer((0, 0), 1, 0, 5)

        sizer_4about.Add(sizer_4about_btn, 0, wx.EXPAND, 5)

        self.SetSizer(sizer_4about)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
