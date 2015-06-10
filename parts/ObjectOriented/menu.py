#! /usr/bin/python
#-*- coding:utf-8 -*-
#メニューがついた画面をつくるプログラム
from Tkinter import *

def new():
	print("called the New!")

def open():
	print("called the Open!")

def exit():
	print("called the Exit!")

def about():
	print("called the About!")

#===========================
#main function
#===========================
if __name__  == '__main__':
	root = Tk()
	#create a menu
	menu = Menu(root)
	root.config(menu=menu)
	
	filemenu = Menu(menu)
	menu.add_cascade(label="File",menu=filemenu)
	filemenu.add_command(label="NEW",command=new)
	filemenu.add_command(label="Open...", command=open)
	filemenu.add_separator()
	filemenu.add_command(label="Exit", command=exit)
	
	helpmenu = Menu(menu)
	menu.add_cascade(label="Help", menu=helpmenu)
	helpmenu.add_command(label="About...", command=about)
	
	root.mainloop()