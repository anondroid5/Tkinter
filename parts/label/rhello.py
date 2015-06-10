#coding: utf-8
from Tkinter import *
from random import *

class Application(Label):
	def __init__(self,master=None):
		Label.__init__(self, master, text='Hello world!', font=('Helvetica', '24', 'bold'))
		self.bind_all('<1>',self.bg_change)


	def bg_change(self, event):
		r = randint(0, 255)
		g = randint(0, 255)
		b = randint(0, 255)
		self.configure(bg='#%02X%02X%02X' % (r, g, b))


if __name__ == '__main__':
	l = Application()
	l.pack()
	l.mainloop()
