from statistics import geometric_mean
from  tkinter import *
wd = Tk()

frame = Frame(wd)
frame.pack()
Button(frame,text="W",font=("Times new Roman",25),width=3).pack(side=TOP)
Button(frame,text="A",font=("Times new Roman",25),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Times new Roman",25),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Times new Roman",25),width=3).pack(side=LEFT)
wd.mainloop()