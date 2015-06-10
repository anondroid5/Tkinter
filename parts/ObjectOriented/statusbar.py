#! /usr/bin/python
#-*- coding:utf-8 -*-
#ステータスバーがついたウィンドウをつくるプログラム
from Tkinter import *
import time

#=================================================
# definition of class
#=================================================
class StatusBar(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.main = Label(self, bd=1, relief="sunken", anchor="n",\
                                 height=10, width=20, text="status bar test")
        self.main.pack(fill="both")
        self.label = Label(self, bd=1, relief="sunken", anchor="w")
        self.label.pack(fill="x")

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()

#=================================================
# main function
#=================================================
if __name__  == '__main__':
    root = Tk()
    status = StatusBar(root)
    status.pack(side="bottom", fill="x")
    for var in range(0, 101):
        status.set("status\t%d percent",var)
        time.sleep(1)
    root.mainloop()