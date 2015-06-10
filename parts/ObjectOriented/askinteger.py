#! /usr/bin/python
#-*- coding:utf-8 -*-
#整数を読み込んでフィボナッチ数列を計算する
from Tkinter import *
import math,tkSimpleDialog

#=================================================
# difinition class
#=================================================
class main_window(Frame):

	def __init__(self, master):
		Frame.__init__(self,master)
		master.title("Fibonacci number")
		master.minsize(200,50)
		self.label = Label(master,text="Fibonacci")
		self.label.pack()
		self.buttons = Button(master, text="Integer", fg="red",command=self.askint)
		self.buttons.pack()
		
	def fibonacci(self, n):
		if n==0:
			return 0
		if n==1:
			return 1
		return (self.fibonacci(n-2)+self.fibonacci(n-1))
	
	def set(self, st):
		self.label.config(text=st)

	def askint(self):
		n  = tkSimpleDialog.askinteger("Input integer", "Fibonacci n",)
		fn = self.fibonacci(n) 
		self.set(fn)

#=================================================
# main function
#=================================================
if __name__  == '__main__':
	root = Tk()
	mw = main_window(root)
	root.mainloop()