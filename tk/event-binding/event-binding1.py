import tkinter as tk

master = tk.Tk()

def callback(event):
	print("clicked at", event.x, event.y)

frame = tk.Frame(master, width=100, height=100)
frame.bind("<Button-1>", callback);
frame.pack()

master.mainloop()