import tkinter as tk

master = tk.Tk()

var = tk.IntVar()

c = tk.Checkbutton(master, text="Expand", variable=var)
c.pack()

master.mainloop()