from tkinter import  *
root = Tk()

lbred = Label(root,text="Red",fg="Red",relief=GROOVE)
lbred.pack()
lbgreen = Label(root,text="绿色",fg="green",relief=GROOVE)
lbgreen.pack()
lbblue = Label(root,text="蓝",fg="blue",relief=GROOVE)
lbblue.pack()
root.mainloop()