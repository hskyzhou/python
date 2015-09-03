import tkinter as tk

master = tk.Tk()

var = tk.IntVar()

c = tk.Checkbutton(master, text="Don't show this again", variable=var)
c.var = var
c.pack()

master.mainloop()