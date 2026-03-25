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
## Class MyFrame1
###########################################################################


class MyFrame1(wx.Frame):
    fr = open("courses.txt", mode="r", encoding="UTF-8")

    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=wx.EmptyString,
            pos=wx.DefaultPosition,
            size=wx.Size(500, 398),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        b_sizer1 = wx.BoxSizer(wx.VERTICAL)

        self.load_button = wx.Button(
            self, wx.ID_ANY, "LoadButton", wx.DefaultPosition, wx.DefaultSize, 0
        )
        b_sizer1.Add(self.load_button, 0, wx.ALL, 5)

        self.m_staticText1 = wx.StaticText(
            self, wx.ID_ANY, "Course", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText1.Wrap(-1)

        b_sizer1.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.title = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0
        )
        b_sizer1.Add(self.title, 0, wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(
            self, wx.ID_ANY, "Duration", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText2.Wrap(-1)

        b_sizer1.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.duration = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0
        )
        b_sizer1.Add(self.duration, 0, wx.ALL, 5)

        self.m_staticText3 = wx.StaticText(
            self, wx.ID_ANY, "Location", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText3.Wrap(-1)

        b_sizer1.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.location = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0
        )
        b_sizer1.Add(self.location, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(
            self, wx.ID_ANY, "Price", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText4.Wrap(-1)

        b_sizer1.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.price = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0
        )
        b_sizer1.Add(self.price, 0, wx.ALL, 5)

        self.SetSizer(b_sizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.load_button.Bind(wx.EVT_BUTTON, self.LoadCourse)

    def __del__(self):
        pass

        # Virtual event handlers, overide them in your derived class

    def LoadCourse(self, event):
        # reading a text file
        coursename = MyFrame1.fr.readline()
        courseduration = MyFrame1.fr.readline()
        courselocation = MyFrame1.fr.readline()
        courseprice = MyFrame1.fr.readline()

        self.title.SetValue(coursename)
        self.duration.SetValue(courseduration)
        self.location.SetValue(courselocation)
        self.price.SetValue(courseprice)


app = wx.App()
frame = MyFrame1(None).Show()
app.MainLoop()
