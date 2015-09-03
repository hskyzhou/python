import tkinter as tk

master = tk.Tk()

def callback():
	print("click")

b = tk.Button(master, text="OK", comman=callback)
b.pack()

master.mainloop()