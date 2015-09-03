import tkinter as tk

master = tk.Tk()

def key(event):
	print("pressed:",repr(event.char))

def callback(event):
	frame.focus_set()
	print("clicked at", event.x, event.y)

frame = tk.Frame(master, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

master.mainloop()