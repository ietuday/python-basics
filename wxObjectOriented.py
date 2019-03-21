import wx


class MyClass(wx.Frame):
    def __init__(self, msg):
        wx.Frame.__init__(self, msg)

        self.panel = wx.Panel(self)
        self.button = wx.Button(self.panel, label='click', pos=(150, 300))
        self.textfield = wx.TextCtrl(self.panel, pos=(10, 100))
        self.var = wx.StaticText(self.panel, label="You Entered:")
        self.mytext = wx.StaticText(self.panel, label='k', pos=(100, 0))
        self.button.Bind(wx.EVT_BUTTON, self.showData)
    
    def showData(self, event):
        self.mytext.SetLabel(self.textfield.GetValue())

if __name__=='__main__':
    app = wx.App()
    frame = MyClass(None)
    frame.Show()
    app.MainLoop()

