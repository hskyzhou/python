import tkinter as tk

master = tk.Tk()

var = tk.StringVar()
e = tk.Entry(master, textvariable=var)
e.pack()

e.focus_set()

def callback():
	print(var.get())

b = tk.Button(master, text="get", width=10, command=callback)
b.pack()

e = tk.Entry(master, width=50)
e.pack

text = e.get()

def makeentry(parent, caption, width=None, **options):
	tk.Label(parent, text=caption).pack(side=tk.LEFT)
	entry = tk.Entry(parent, **options)
	if width:
		entry.config(width=width)
	entry.pack()
	return entry

user = makeentry(master, "User name:", 10)
password = makeentry(master, "Password:", 10, show="*")

content = tk.StringVar()
entry = tk.Entry(master, text="caption", textvariable=content)

text = content.get()
content.set(text)

master.mainloop()