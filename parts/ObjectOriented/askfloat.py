#! /usr/bin/python
#-*- coding:utf-8 -*-
#実数を読み込んで三角関数を計算する
from Tkinter import *
import math,tkSimpleDialog

#=================================================
# difinition class
#=================================================
class main_window(Frame):
	def __init__(self, master):
		Frame.__init__(self,master)
		self.label = Label(master,text="Trigonometric function.")
		self.label.pack()
		self.buttons = Button(master, text="sin(x)", fg="red",command=lambda:self.askstr("sin"))
		self.buttons.pack(side="left")
		self.buttonc = Button(master, text="cos(x)", fg="red", command=lambda:self.askstr("cos"))
		self.buttonc.pack(side="left")
	def set(self, st):
		self.label.config(text=st)

	def askstr(self, f):
		theta=tkSimpleDialog.askfloat("test askinteger", "deg",)
		if f=="sin":
			data=str(math.sin(math.radians(theta)))
		if f=="cos":
			data=str(math.cos(math.radians(theta)))
		self.set(data)

#=================================================
# main function
#=================================================
if __name__  == '__main__':
	root = Tk()
	mw = main_window(root)
	root.mainloop();