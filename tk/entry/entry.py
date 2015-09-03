import tkinter as tk

master = tk.Tk()

var = tk.StringVar()

e = tk.Entry(master, textvariable=var)
e.pack()

var.set("a test file name")
s = var.get()

print(s)

master.mainloop()