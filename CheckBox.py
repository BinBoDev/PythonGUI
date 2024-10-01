from msilib.schema import CheckBox
from tkinter import *

from RadioButton import mylabel

wd=Tk()
wd.geometry("400x400")
def checked():
    mylabel1 = Label(wd,text=var.get())
    mylabel1.pack()
var = StringVar()
checkBox = Checkbutton(wd,text="check",variable=var,onvalue="On",offvalue="Off",command=checked)
checkBox.pack()




wd.mainloop()
