#coding: utf-8
from Tkinter import *
main_window = Tk()
count_label = Label(main_window, text="count 0")
count_label.grid(row=0, column=1)
count_value = 0

def increment_count():
	global count_value, count_label
	count_value = count_value + 1
	count_label.configure(text ='Count:' + str(count_value))

incr_button = Button(main_window, text="Increment" ,command= increment_count)
incr_button.grid(row=0,column=0)
quit_button = Button(main_window, text="Quit", command = main_window.destroy)
quit_button.grid(row=1, column=0)
mainloop()