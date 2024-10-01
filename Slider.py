from cProfile import label
from tkinter import *

wd=Tk()
vertical = Scale(wd,from_=0,to=100)
vertical.pack()
horizontal = Scale(wd,from_=0,to=100,orient=HORIZONTAL)
horizontal.pack()



label = Label(wd,text=horizontal.get())
label.pack()

wd.mainloop()
