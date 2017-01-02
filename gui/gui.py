#!/usr/local/bin/python
#import wx
#app=wx.App()
#win=wx.Frame(None,title='Editor',size=(420,345))
#loadbtn=wx.Button(win,label='Open',pos=(225,5),size=(80,25))
#savebtn=wx.Button(win,label='Save',pos=(315,5),size=(80,25))
#filename=wx.TextCtrl(win,pos=(5,5),size=(210,25))
#contents=wx.TextCtrl(win,pos=(5,35),size=(390,260),
#         style=wx.TE_MULTILINE|wx.HSCROLL)
#win.Show()
#app.MainLoop()
import wx

def load(event):
  file=open(filename.GetValue())
  contents.SetValue(file.read())
  file.close()

def save(event):
  file=open(filename.GetValue(),'w')
  file.write(contents.GetValue())
  file.close()

app=wx.App()
win=wx.Frame(None,title='Editor',size=(410,335))
bkg=wx.Panel(win)

loadbtn=wx.Button(bkg,label='Open')
loadbtn.Bind(wx.EVT_BUTTON,load)

savebtn=wx.Button(bkg,label='Save')
savebtn.Bind(wx.EVT_BUTTON,save)

filename=wx.TextCtrl(bkg)
contents=wx.TextCtrl(bkg,style=wx.TE_MULTILINE|wx.HSCROLL)

hbox=wx.BoxSizer()
hbox.Add(filename,proportion=0,flag=wx.EXPAND)
hbox.Add(loadbtn,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(savebtn,proportion=0,flag=wx.LEFT,border=5)

vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
vbox.Add(contents,proportion=1,
         flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)

bkg.SetSizer(vbox)
win.Show()

app.MainLoop()

