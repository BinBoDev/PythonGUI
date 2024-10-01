from  tkinter import *
wd = Tk()
User = Label(wd,text="User").grid(row = 0,column= 0)
EntryText = Entry(wd).grid(row = 0,column= 1)

Pasword = Label(wd,text="Password").grid(row = 1,column= 0)
EntryTextPa = Entry(wd).grid(row = 1,column= 1)



wd.mainloop()
