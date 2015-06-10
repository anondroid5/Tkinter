#coding: utf-8
from Tkinter import *

class Application(Frame):

	def __init__(self,master=None):
		Frame.__init__(self,master,height=200,width=200)
		self.master.title('Nested Frames')

		#First Frame
		f1 = Frame(self, relief=RIDGE, bd=2)
		for text, color in [('A', 'magenta'), ('B', 'yellow'), ('C', 'SeaGreen'), ('D', 'LightSkyBlue')]:
			l=Label(f1, text=text, bg=color, font=('Helvetica', '16'))
			l.pack(side=LEFT)
		f1.place(relx=0.2, rely=0.2)

		# Second Frame
		f2 = Frame(self, relief=RIDGE, bd=2)
		for i, (text, color) \
                        in enumerate([('A', 'magenta'), ('B', 'yellow'), ('C', 'SeaGreen'), ('D', 'LightSkyBlue')]):
			l=Label(f2, text=text, bg=color, font=('Helvetica', '16'))
			l.grid(row=i/2, column=i%2)
		f2.place(relx=0.6, rely=0.6)

if __name__ == '__main__':
	app = Application()
	app.pack()
	app.mainloop()