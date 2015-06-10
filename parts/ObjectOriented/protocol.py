#! /usr/bin/python
#-*- coding:utf-8 -*-
#終了メッセージボックスを表示するプログラム
from Tkinter import *
import tkMessageBox

def callback():
	if tkMessageBox.askokcancel("Quit","Do you really wish to quit?"):
		root.destroy()

#===========================
#main function
#===========================
if __name__  == '__main__':
	root = Tk()
	root.protocol("WM_DELETE_WINDOW",callback)
	root.mainloop()