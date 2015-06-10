#coding: utf-8
from Tkinter import *

class Application(Frame):

	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.master.title('PackThree Lables')

		# First Label
		self.la = Label(self, text="Hello everybody",bg='yellow',relief=RIDGE, bd=2)
		self.la.pack()

		# Second Label
		self.lb = Label(self, text="Oh My God!", bg='red', relief=RIDGE, bd=2)
		self.lb.pack()

		#Third Label
		self.lc = Label(self, text="See you tomorrow.", bg='LightSkyBlue', relief=RIDGE, bd=2)
		self.lc.pack()

if __name__ == '__main__':
	app = Application()
	app.pack()
	app.mainloop()