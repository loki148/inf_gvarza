import tkinter as tk
import math
h,m  = input().split()

canvas= tk.Canvas(width= 400, height=400, )
canvas.pack()
a = [4,5,6,7,8,9,10,11,12,1,2,3,]
for i in range(1,13):
    canvas.create_text(math.cos(i/2)*150+200,math.sin(i/2)*150+200, text =str(a[(i)-1]), font='arial 30 bold')

canvas.create_text(200,200, text = '           ———', font='arial 25 bold', angle = 6*int(m)+90)
canvas.create_text(200,200, text = '       ————', font='arial 25 bold', angle = 30*int(h)+90)

tk.mainloop()