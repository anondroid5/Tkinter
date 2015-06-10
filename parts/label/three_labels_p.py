#coding: utf-8
from Tkinter import *
class Application(Frame):

	def __init__(self,master=None):
		Frame.__init__(self,master,height=100, width=250)
		self.master.title('Pack Three Labels')

		#First Label
		la = Label(self,text='Hello everybody. How are you?', bg='yellow',relief=RIDGE,bd=2)
		la.place(relx=0.02, rely=0.1, relheight=0.3, relwidth=0.95)


		# Second Label
		lb = Label(self, text='Oh My God!', bg='red', relief=RIDGE, bd=2)
		lb.place(relx=0.15, rely=0.45)

		# Third Label
		lc = Label(self, text='See you tomorrow.', bg='LightSkyBlue', relief=RIDGE, bd=2)
		lc.place(relx=0.5, rely=0.75)

if __name__ == '__main__':
	app = Application()
	app.pack()
	app.mainloop()
