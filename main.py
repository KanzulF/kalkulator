import wx
import Gui

class subClass(Gui.MyFrame8):
    def __init__(self,parent):
        Gui.MyFrame8.__init__(self,parent)

    #override



app = wx.App()
frame = subClass(parent=None)
frame.Show()

app.MainLoop()
