#! /usr/bin/python
#-*- coding:utf-8 -*-
#ボタンを一つ表示し，それを押すと終了するプログラム(継承元)
from Tkinter import *

#=================================================
# definition of class
#=================================================
class one_button(Frame):
	#クラス初期設定
	def __init__(self, master=None):
		Frame.__init__(self, master)
		#クラスウィジェット作成
		f=Frame(master,bg='red', bd=10)
		f.pack()
		b=Button(f, text=u'終了', command=self.goout)
		b.pack()

	def goout(self):
		print('終了')
		exit()

#=======================================
# メインプログラム
#=======================================
if __name__  == '__main__':
	g=one_button()
	g.mainloop()