import tkinter as tk
import random

a,b = input().split()
a, b = int(a), int(b)
height_of_win = a//2*b + 600
canvas= tk.Canvas(width= a*b+200, height=height_of_win, bg='black')
canvas.pack()

def pyramid(base_num, size, j=0):
    colors = ['blue','red','magenta', 'green', 'white', 'yellow']
    while base_num > 0:
        for i in range(base_num):
            canvas.create_rectangle(100-size/2+i*size+j*size,600-size/2-j*size, 100+size/2+i*size+j*size,600+size/2-j*size, fill = random.choice(colors))
        
        base_num -=2
        j +=1



pyramid(a,b)

tk.mainloop()