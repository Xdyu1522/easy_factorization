# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import traceback
from sympy import factor,symbols
import ctypes


###########################################################################
## Class MainFrame
###########################################################################

ctypes.windll.shcore.SetProcessDpiAwareness(2)
 
class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"easy_factorization", pos = wx.DefaultPosition, size = wx.Size( 300,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.icon = wx.Icon(name="./icon.ico", type=wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.unknown_text = wx.StaticText( self, wx.ID_ANY, u"请输入未知数(以半角空格分隔)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.unknown_text.Wrap( -1 )

        bSizer2.Add( self.unknown_text, 0, wx.ALL, 5 )

        self.unknowns = wx.TextCtrl( self, wx.ID_ANY, u"x y", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.unknowns, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.equation_text = wx.StaticText( self, wx.ID_ANY, u"请输入算式,乘方请使用\"^\",不要省略乘号\"*\"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.equation_text.Wrap( -1 )

        bSizer3.Add( self.equation_text, 0, wx.ALL, 5 )

        self.equation = wx.TextCtrl( self, wx.ID_ANY, u"x ^ 2 + 2 * x * y + y ^ 2", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.equation, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.calc_btn = wx.Button( self, wx.ID_ANY, u"分解！", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.calc_btn, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.result = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,200 ), style=wx.TE_MULTILINE)
        bSizer5.Add( self.result, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.calc_btn.Bind( wx.EVT_BUTTON, self.calc )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def calc( self, event ):
        try: 
            equation = self.equation.Value.replace("^", "**")

            tmp = ", ".join(self.unknowns.Value.split(" "))
            exec(f"{tmp} = symbols(\"{self.unknowns.Value}\")")


            result = str(factor(equation))
            result = result.replace("**", "^")
            self.result.SetValue(result)
        except Exception as e: 
            self.result.SetValue(traceback.format_exc())


if __name__ == "__main__": 
    app = wx.App()
    frame = MainFrame(None)
    frame.Show(True)
    app.MainLoop()