import tkinter as tk

root = tk.Tk()

canvas= tk.Canvas(root, width= 400, height=400, bg='black')
canvas.pack()

entry = tk.Entry(root)
canvas.create_window(75, 350, window=entry)

entry2 = tk.Entry(root)
canvas.create_window(210, 350, window=entry2)
#canvas.update()

def circle():
    polomer = int(entry.get())
    x, y = entry2.get().split()
    canvas.create_oval(int(x)-(polomer/2),int(y)-(polomer/2),int(x)+(polomer/2),int(y)+(polomer/2), fill = 'white')


button = tk.Button(text="Create", command=circle)
canvas.create_window(300, 350, window=button)


tk.mainloop()