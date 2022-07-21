import tkinter as tk

x = 0

# 创建窗口
window = tk.Tk()
window.title('Mywindow')  # 窗口的标题
window.geometry('200x100')  # 窗口的大小
# 定义一个label
var = tk.StringVar()  # 定义一个字符串变量
l = tk.Label(window,
             textvariable=var,  # 标签的文字
             bg='green',  # 标签背景颜色
             font=('Arial', 12),  # 字体和字体大小
             width=15,
             height=2  # 标签长宽
             )
l.pack()  # 固定窗口位置
# 定义一个全局变量，来表明字符显示与不显示
on_hit = False

kk = False
# 按钮的函数
def hit_me(x):
    global on_hit  # 声明全局变量
    if on_hit == False:
        on_hit = True
        global kk
        kk = True
        var.set(x)
    else:
        on_hit = False
        var.set(x)


# 按钮
b = tk.Button(window,
              text='点我',
              width=15,
              height=2,
              ommand=hit_me(x)
              )  # 点击按钮执行一个名为“hit_me”的函数
b.pack()

window.mainloop()
