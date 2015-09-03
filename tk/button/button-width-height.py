import tkinter as tk

master = tk.Tk()

f = tk.Frame(master, height=34, width=34)
f.pack_propagate(0)
f.pack()

b = tk.Button(f, text="Sure!")
b.pack(fill=tk.BOTH, expand=1)
b.config(relief=tk.SUNKEN)

master.mainloop()