#! /usr/bin/python
#-*- coding:utf-8 -*-
#メッセージボックスを表示するプログラム
from Tkinter import *
import tkMessageBox

#===========================
#main function
#===========================
if __name__  == '__main__':
	filename = "hoge"
	try:
		fp = open(filename)
	except:
		tkMessageBox.showwarning(
			"Open file",
			"Cannot open this file\n(%s)" % filename
		)