from tkinter import *
from  tkinter import  messagebox

from Addframe import button

wd = Tk()
def popme():
    messagebox.showinfo("Buzz","Hi,Bian",icon="info")
button1 =Button(wd,text="click me",command=popme).pack()
wd.mainloop()