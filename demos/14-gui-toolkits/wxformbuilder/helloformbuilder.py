# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wx_form_builder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################


class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=wx.EmptyString,
            pos=wx.DefaultPosition,
            size=wx.Size(500, 300),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        b_sizer1 = wx.BoxSizer(wx.VERTICAL)

        self.HelloText = wx.StaticText(
            self,
            wx.ID_ANY,
            "Hello",
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.ALIGN_CENTER_HORIZONTAL,
        )
        self.HelloText.Wrap(-1)

        self.HelloText.SetFont(
            wx.Font(
                20,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                wx.EmptyString,
            )
        )

        b_sizer1.Add(
            self.HelloText, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5
        )

        choice_choices = ["World", "Afrika", "America", "Asia", "Europ", "Amerika"]
        self.choice = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_choices, 0
        )
        self.choice.SetSelection(0)
        self.choice.SetFont(
            wx.Font(
                20,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                wx.EmptyString,
            )
        )

        b_sizer1.Add(self.choice, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.button = wx.Button(
            self, wx.ID_ANY, "Print", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.button.SetFont(
            wx.Font(
                20,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                wx.EmptyString,
            )
        )

        b_sizer1.Add(self.button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.SetSizer(b_sizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.button.Bind(wx.EVT_BUTTON, self.print_func)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def print_func(self, event):
        hw = self.choice.GetStringSelection()
        self.HelloText.SetLabel("Hello... " + hw)
        self.Layout()


app = wx.App()
frame = MainFrame(None).Show()
app.MainLoop()
