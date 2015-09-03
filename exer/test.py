import tkinter as tk #引入模块
#resize函数是用来改变文字大小的，当进度条改变时调用
def resize(ev=None):
	tk.Label.config(font='Helvetica -%d bold' % tk.Scale.get())
	#config函数就是通过设置组件的参数来改变组件的，这里改变的是font字体大小
top=tk.Tk()   #主窗口
top.geometry('600x400')  #设置了主窗口的初始大小600x400
label= tk.Label(top,text='Hello world!',font='Helvetica -12 bold')  #设置标签字体的初始大小
label.pack(fill=tk.Y,expand=1)
#scale创建进度条，设置
scale=tk.Scale(top,from_=10,to=40,orient=tk.HORIZONTAL,command=resize)
scale.set(12)  #设置起始位置
scale.pack(fill=tk.X,expand=1)
quit = tk.Button(top,text='QUIT',command=top.quit,activeforeground='white',
activebackground='red')
quit.pack()
top.mainloop()