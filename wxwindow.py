import wx     
def sayHello(event):
    print('Button Pressed')
app = wx.App()
win = wx.Frame(None, title="MyAPP", size=(400, 400))
panel = wx.Panel(win)
loadButton = wx.Button(panel, label="Click Me", pos=(30, 70))
loadButton.Bind(wx.EVT_BUTTON, sayHello)
win.Show()
app.MainLoop()  