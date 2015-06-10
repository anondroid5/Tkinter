#coding: utf-8
from Tkinter import *
main_window = Tk()
label = Label(main_window,text="Hello",background='white',foreground='red',font='Times 20',relief='groove',borderwidth=3)
label.grid(row=0,column=0)
mainloop()