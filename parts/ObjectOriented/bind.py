#! /usr/bin/python
#-*- coding:utf-8 -*-
#クリックした座標を読み取るプログラム
from Tkinter import *

def callback(event):
	print("clicked at",event.x,event.y)

#===========================
#main function
#===========================
if __name__  == '__main__':
	root = Tk()
	frame = Frame(root,width=100,height=100)
	frame.bind("<Button-1>", callback)
	frame.pack()
	root.mainloop()