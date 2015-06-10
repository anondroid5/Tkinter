#coding: utf-8
from Tkinter import *
class Application(Frame):

	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.master.title('Pack Three Labels')

		# First Label
		self.la = Label(self, text="Hello everybody.",bg='yellow',relief=RIDGE, bd=2)
		self.la.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

		# Second Label
		self.lb = Label(self, text='Oh My God!', bg='red', relief=RIDGE, bd=2)
		self.lb.grid(row=1, column=0, padx=5, pady=5)

		# Third Label
		self.lc = Label(self, text='See you tomorrow.', bg='LightSkyBlue', relief=RIDGE, bd=2)
		self.lc.grid(row=1, column=1, padx=5, pady=5)


if __name__ == '__main__':
	app = Application()
	app.pack()
	app.mainloop()
