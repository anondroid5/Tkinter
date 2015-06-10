#! /usr/bin/python
#-*- coding:utf-8 -*-
#ボタン付き Hello プログラム
from Tkinter import *
class App:
	def __init__(self,master):
		frame = Frame(master)
		frame.pack()
		
		self.button = Button(frame,text="QUIT",fg="red",command=frame.quit)
		self.button.pack(side="left")
		
		self.hi_there = Button(frame,text="Hello",command=self.say_hi)
		self.hi_there.pack(side="left")
		
	def say_hi(self):
		print("hi there, everyone!")

#===========================
#main function
#===========================
if __name__  == '__main__':
	root = Tk()
	app = App(root)
	root.mainloop()