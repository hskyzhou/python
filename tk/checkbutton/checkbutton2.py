import tkinter as tk

master = tk.Tk()

var = tk.StringVar()

c = tk.Checkbutton(master, text="Color Image", variable=var, onvalue="RGB", offvalue="L")
c.pack()

master.mainloop()