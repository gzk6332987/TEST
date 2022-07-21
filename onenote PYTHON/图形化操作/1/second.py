from  tkinter import *
root = Tk()

x = '煞笔'
color = '#ff00ff'

lb = Label(root,text=x,
        bg='#d3fbfb',
        fg='red',
        font=('微软雅黑',32),
        width=20,
        height=2,
        relief=SUNKEN)
lb.pack()
root.mainloop()