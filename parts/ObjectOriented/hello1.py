#! /usr/bin/python
#-*- coding:utf-8 -*-
#HelloWorldを表示させるプログラム
from Tkinter import *

#===========================
#main function
#===========================
if __name__  == '__main__':
	root = Tk()
	w = Label(root,text="Hello,world!")
	w.pack()
	root.mainloop()