import tkinter as tk

class VanCB:
	def __init__(self, master):
		self.var = tk.IntVar()
		c = tk.Checkbutton(master, text="Enable Tab", variable=self.var, command=self.cb)
		c.pack()
	def cb(self):
		print("variable is ", self.var.get())

master = tk.Tk()
cb = VanCB(master)
master.mainloop()