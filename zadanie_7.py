import tkinter as tk

root = tk.Tk()

canvas= tk.Canvas(root, width= 400, height=400, bg='black')
canvas.pack()

entry = tk.Entry(root)
canvas.create_window(75, 350, window=entry)

def draw(sur):
    x,y = sur.x, sur.y
    a = int(entry.get())
    canvas.create_oval(x-a/2,y-a/2,x+a/2,y+a/2, fill = 'red')


canvas.bind("<Button-1>", draw)

tk.mainloop()