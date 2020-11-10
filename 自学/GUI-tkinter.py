import tkinter as tk
import os
root = tk.Tk()
root.title(os.path.realpath("GUI-tkinter.py"))
#app.title("hello")
theLabel = tk.Label(root,text="我的第一个窗口程序")
theLabel.pack()

win = tk.Tk()
win.title("GUI.py")
theLabel2=tk.Label(win,text="My second Application")
theLabel2.pack()

class APP():
    def __init__(self,main):
        frame=tk.Frame(main)
        frame.pack()
    
        self.hi=tk.Button(frame,text="hello",fg="blue")
        self.hi.pack()

class APP2():
    def __init__(self,main):
        frame=tk.Frame(main)
        frame.pack()
        self.click=tk.Button(frame,text="click",fg="blue")
        self.click.pack()
app=APP(root)
app2=APP2(root)
#root.mainloop()
win.mainloop()


