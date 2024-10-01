from tkinter import *
wd = Tk()
wd.title("Add Frame")
wd.geometry("420x420")

frame = LabelFrame(wd,text="My Frame",padx=20,pady=20)
frame.pack(padx=100,pady=100)
button = Button(frame,text="Click me")
#button.pack()
button.grid(row=0,column=0)

wd.mainloop()
