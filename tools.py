# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame
###########################################################################

class MyFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"zxz-tools", pos=wx.DefaultPosition,
                          size=wx.Size(600, 500), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook1 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel1 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        m_comboBox1Choices = [u"2", u"8", u"10", u"16"]
        self.m_comboBox1 = wx.ComboBox(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       m_comboBox1Choices, 0)
        self.m_comboBox1.SetSelection(0)
        bSizer3.Add(self.m_comboBox1, 0, wx.ALL, 5)

        m_comboBox2Choices = [u"2", u"8", u"10", u"16"]
        self.m_comboBox2 = wx.ComboBox(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       m_comboBox2Choices, 0)
        self.m_comboBox2.SetSelection(0)
        bSizer3.Add(self.m_comboBox2, 0, wx.ALL, 5)

        self.m_button1 = wx.Button(self.m_panel1, wx.ID_ANY, u"转换", wx.Point(-1, -1), wx.DefaultSize, 0)
        bSizer3.Add(self.m_button1, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self.m_panel1, wx.ID_ANY, u"清除", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_button2, 0, wx.ALL, 5)

        bSizer2.Add(bSizer3, 0, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"输入：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        bSizer4.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_MULTILINE)
        bSizer4.Add(self.m_textCtrl1, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticText2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"结果：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        bSizer4.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_textCtrl2 = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_MULTILINE)
        bSizer4.Add(self.m_textCtrl2, 1, wx.ALL | wx.EXPAND, 5)

        bSizer2.Add(bSizer4, 1, wx.EXPAND, 5)

        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        self.m_notebook1.AddPage(self.m_panel1, u"进制转换", False)
        self.m_panel2 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"输入：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        bSizer6.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_MULTILINE)
        bSizer6.Add(self.m_textCtrl3, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticText4 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"翻译：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        bSizer6.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_textCtrl4 = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_MULTILINE)
        bSizer6.Add(self.m_textCtrl4, 1, wx.ALL | wx.EXPAND, 5)

        bSizer5.Add(bSizer6, 1, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button3 = wx.Button(self.m_panel2, wx.ID_ANY, u"翻译", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_button3, 0, 0, 5)

        self.m_button4 = wx.Button(self.m_panel2, wx.ID_ANY, u"清除", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_button4, 0, 0, 5)

        m_comboBox3Choices = [u"汉译英", u"英译汉"]
        self.m_comboBox3 = wx.ComboBox(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       m_comboBox3Choices, 0)
        self.m_comboBox3.SetSelection(0)
        bSizer7.Add(self.m_comboBox3, 0, 0, 5)

        bSizer5.Add(bSizer7, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel2.SetSizer(bSizer5)
        self.m_panel2.Layout()
        bSizer5.Fit(self.m_panel2)
        self.m_notebook1.AddPage(self.m_panel2, u"中英互译", False)
        self.m_panel3 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"输入：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        bSizer9.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_MULTILINE)
        bSizer9.Add(self.m_textCtrl5, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticText6 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"输出：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        bSizer9.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.m_textCtrl6 = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_MULTILINE)
        bSizer9.Add(self.m_textCtrl6, 1, wx.ALL | wx.EXPAND, 5)

        bSizer8.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button5 = wx.Button(self.m_panel3, wx.ID_ANY, u"解密", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.m_button5, 0, 0, 5)

        self.m_button6 = wx.Button(self.m_panel3, wx.ID_ANY, u"清除", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.m_button6, 0, 0, 5)

        bSizer8.Add(bSizer10, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel3.SetSizer(bSizer8)
        self.m_panel3.Layout()
        bSizer8.Fit(self.m_panel3)
        self.m_notebook1.AddPage(self.m_panel3, u"维吉利亚解密", False)
        self.m_panel4 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText7 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"！！！可用于base64,32,16,85，utf-8编码的加解密",
                                           wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.m_staticText7.Wrap(-1)

        self.m_staticText7.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.m_staticText7.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer12.Add(self.m_staticText7, 0, wx.EXPAND, 5)

        bSizer11.Add(bSizer12, 0, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        m_comboBox4Choices = [u"base16", u"base32", u"base64", u"base85", wx.EmptyString]
        self.m_comboBox4 = wx.ComboBox(self.m_panel4, wx.ID_ANY, u"base16", wx.DefaultPosition, wx.DefaultSize,
                                       m_comboBox4Choices, 0)
        self.m_comboBox4.SetSelection(0)
        bSizer13.Add(self.m_comboBox4, 0, wx.ALL, 5)

        self.m_button7 = wx.Button(self.m_panel4, wx.ID_ANY, u"加密", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.m_button7, 0, wx.ALL, 5)

        self.m_button8 = wx.Button(self.m_panel4, wx.ID_ANY, u"解密", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.m_button8, 0, wx.ALL, 5)

        self.m_button9 = wx.Button(self.m_panel4, wx.ID_ANY, u"清除", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.m_button9, 0, wx.ALL, 5)

        bSizer11.Add(bSizer13, 0, wx.EXPAND, 5)

        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText8 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"输入：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)

        bSizer14.Add(self.m_staticText8, 0, wx.ALL, 5)

        self.m_textCtrl7 = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_MULTILINE)
        bSizer14.Add(self.m_textCtrl7, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticText9 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"输出：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)

        bSizer14.Add(self.m_staticText9, 0, wx.ALL, 5)

        self.m_textCtrl8 = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_MULTILINE)
        bSizer14.Add(self.m_textCtrl8, 1, wx.ALL | wx.EXPAND, 5)

        bSizer11.Add(bSizer14, 1, wx.EXPAND, 5)

        self.m_panel4.SetSizer(bSizer11)
        self.m_panel4.Layout()
        bSizer11.Fit(self.m_panel4)
        self.m_notebook1.AddPage(self.m_panel4, u"base加解密", True)

        bSizer1.Add(self.m_notebook1, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button1.Bind(wx.EVT_BUTTON, self.transf)
        self.m_button2.Bind(wx.EVT_BUTTON, self.clear_fun1)
        self.m_button3.Bind(wx.EVT_BUTTON, self.translate)
        self.m_button4.Bind(wx.EVT_BUTTON, self.clear_fun2)
        self.m_button5.Bind(wx.EVT_BUTTON, self.vigenere_decrypt)
        self.m_button6.Bind(wx.EVT_BUTTON, self.clear_fun3)
        self.m_button7.Bind(wx.EVT_BUTTON, self.base_encrypt)
        self.m_button8.Bind(wx.EVT_BUTTON, self.base_decrypt)
        self.m_button9.Bind(wx.EVT_BUTTON, self.clear_fun4)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def transf(self, event):
        event.Skip()

    def clear_fun1(self, event):
        event.Skip()

    def translate(self, event):
        event.Skip()

    def clear_fun2(self, event):
        event.Skip()

    def vigenere_decrypt(self, event):
        event.Skip()

    def clear_fun3(self, event):
        event.Skip()

    def base_encrypt(self, event):
        event.Skip()

    def base_decrypt(self, event):
        event.Skip()

    def clear_fun4(self, event):
        event.Skip()
