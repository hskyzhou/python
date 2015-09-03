import tkinter as tk

master = tk.Tk()

def callback():
	print("click")

b = tk.Button(master, text="OK", comman=callback)
b.pack()

h = tk.Button(master, text="Help", state=tk.DISABLED)
h.pack()

master.mainloop()