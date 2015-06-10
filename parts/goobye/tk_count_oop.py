#coding: utf-8
from Tkinter import *
class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.grid()
		self.create_widgets()
		self.count_value = 0

	def create_widgets(self):
		self.count_label = Label(self, text="Count: 0")
		self.count_label.grid(row=0, column=1)
		self.incr_button = Button(self, text="Increment",command=self.increment_count)
		self.incr_button.grid(row=0, column=0)
		self.quit_button = Button(self, text="Quit",command = self.master.destroy)
		self.quit_button.grid(row=1, column=0)

	def increment_count(self):
		self.count_value += 1
		self.count_label.configure(text='count:' + str(self.count_value))

app = Application()
app.mainloop()