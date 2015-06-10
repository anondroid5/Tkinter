#! /usr/bin/python
#-*- coding:utf-8 -*-
#sampleA.pyを継承するプログラム
import sampleA as B
#=================================================
# definition of class
#=================================================
class BE(B.one_button):
	#メソッドの再設定
	def goout(self):
		print(u'expanded 終了')
		exit()

#=======================================
# メインプログラム
#=======================================
if __name__  == '__main__':
	g=BE()
	g.mainloop()