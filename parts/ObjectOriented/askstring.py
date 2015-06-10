#! /usr/bin/python
#-*- coding:utf-8 -*-
#文字列の入力を促すダイアログを表示するプログラム
from Tkinter import *
import tkSimpleDialog

class main_window(Frame):
	def __init__(self,master):
		Frame.__init__(self,master)
		self.label = Label(master,text="There is no data.")
		self.label.pack()
		
		self.button = Button(master,text ="Input String",fg="red",command=self.askstr)
		self.button.pack(side="left")
		
	def set(self,str):
		self.label.config(text=str)
			
	def askstr(self):
		data=tkSimpleDialog.askstring("test askstring", "input", initialvalue="hoge")
		self.set(data)


#===========================
#main function
#===========================
if __name__  == '__main__':
	root = Tk()
	mw = main_window(root)
	root.mainloop()