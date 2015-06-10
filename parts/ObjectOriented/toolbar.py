#! /usr/bin/python
#-*- coding:utf-8 -*-
#ツールバーがついたウィンドウをつくるプログラム
from Tkinter import *

def callback():
	print("called the callback!")

#===========================
#main function
#===========================
if __name__  == '__main__':
	root = Tk()
	#create a toolbar
	toolbar = Frame(root)
	
	b = Button(toolbar,text="new",width=6,command=callback)
	b.pack(side="left",padx=2,pady=2)
	
	b = Button(toolbar,text="open",width=6,command=callback)
	b.pack(side="left",padx=2,pady=2)
	
	toolbar.pack(side="top",fill=X)
	root.mainloop()