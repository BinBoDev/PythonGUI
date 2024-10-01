from tkinter import *

from RadioButton import click

window= Tk()
window.title("Drop Menu")
window.geometry("400x400")
def selectitem():
    labelitem = Label(window,text=clicked.get())


clicked = StringVar()
clicked.set("Tan")
drop = OptionMenu(window,clicked,"Tan","Dung","Bong","Bin",command=selectitem)
drop.pack()
labelitem = Label(window)
labelitem.pack()

window.mainloop()