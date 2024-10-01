from tkinter import *
wd = Tk()
wd.title("Radio Button")
x = IntVar()
def click():
    mylabel = Label(wd,text=x.get())
    mylabel.pack()
Radiobutton(wd,text="Option 1",variable=x,value=1,command=click).pack()
Radiobutton(wd,text="Option 2",variable=x,value=2,command=click).pack()

mylabel = Label(wd,text=str(x.get())).pack()

wd.mainloop()