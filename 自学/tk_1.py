from tkinter import *

root = Tk()
root.title("WARNING")
textlable = Label(root,text="WARNING!*_*",justify=CENTER,padx=100)
textlable.pack(side=TOP)

ph = PhotoImage(file="下载.gif")
img=Label(root,image=ph)
img.pack()

mainloop()
