import tkinter as tk
import random

canvas= tk.Canvas(width= 200, height=200, bg='black')
canvas.pack()

canvas.create_oval(75, 75, 125,125, fill=('white'))
def circle():
    x = random.randint(85,115)
    y = random.randint(85,115)
    
    canvas.create_oval(x-5,y-5,x+5,y+5, fill=('red'))
    canvas.update()
    canvas.after(20)
    
    circle()

circle()
tk.mainloop()
    
