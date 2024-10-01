from tkinter import *
def Creat_newwindow():
    #new_widow = Toplevel()
    new_widow = Tk()
    wd.destroy()

wd = Tk()


Button(wd,text="New Window",command = Creat_newwindow).pack()
wd.mainloop()
