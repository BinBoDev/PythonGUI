from tkinter import *
from tkinter import filedialog
wd = Tk()
wd.filename = filedialog.askopenfile(initialdir="D:\OneDrive\OneDrive - Cong ty TNHH But chi Mitsubishi Viet nam\Desktop\Img_temp",title="Chon file",filetypes=(("PNG file","*.png"),("All file","*.*")))
wd.mainloop()