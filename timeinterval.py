import tkinter as tk
import time
import winsound
import threading

# master = tk.Tk()

# # laebl
# implylabel = tk.Label(master, text="时间(s)")
# implylabel.pack(side=tk.LEFT)
# # entry
# secondsVar = tk.IntVar()
# secondsEntry = tk.Entry(master, textvariable=secondsVar)
# secondsEntry.pack(side=tk.LEFT)
# # daojishi function
# def daojishi():
# 	seconds = int(secondsVar.get())
# 	if seconds == 0:
# 		return
# 	for sec in range(seconds):
# 		print(sec)
# 		time.sleep(1)
# 	winsound.Beep(300,500)
# # button
# daojishiButton = tk.Button(master, text="开始倒计时", command=daojishi)
# daojishiButton.pack()


# master.mainloop()



master = tk.Tk()
# VanTimer class 定时器类
class VanTimer(threading.Thread):
	pass

var = tk.IntVar()
# VanLayout class  整体布局类
class VanLayout:
	def __init__(self, master):
		# wrap层
		print(dir(self))
		self.van_create_label(master, "倒计时1", {"side": tk.LEFT})
		self.van_create_entry(master)
		self.van_create_button(master, "开始倒计时", {"side": tk.LEFT})
		
	# create button
	def van_create_button(self, master, buttonName="button", args=''):
		b = tk.Button(master, text=buttonName);
		b.pack(args)

	# create label
	def van_create_label(self, master, textName="label", args=''):
		l = tk.Label(master, text=textName)
		l.pack(args)

	# create entry
	def van_create_entry(self, master, args=''):
		e = tk.Entry(master, textvariable=var)
		e.pack(args)

	def callback(self, master):
		print(var.get())


VanLayout(master)
master.mainloop()