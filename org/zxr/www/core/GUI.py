#!/usr/bin/python
#  -*- coding: UTF-8 -*-

from Tkinter import *
import tkMessageBox


# first GUI process
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgetsHello()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def createWidgetsHello(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text="hello", command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or "world!"
        tkMessageBox.showinfo('message', 'Hello, %s' % name)

app = Application()
app.master.title = "hello world!"
app.mainloop()