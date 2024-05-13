import tkinter as tk
from random import randint

text = input('text:')
angle = int(input('uhol:'))

canvas = tk.Canvas(width= 400, height=400)
canvas.pack()

canvas.create_text(randint(50,250),randint(50,250), text = text, angle= angle)


def delete(_):
    canvas.delete('all')


canvas.bind('<Button-1>',delete)
tk.mainloop()