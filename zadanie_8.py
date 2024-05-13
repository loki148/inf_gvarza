import tkinter as tk

root = tk.Tk()

canvas= tk.Canvas(root, width= 320, height=320, bg='black')
canvas.pack()

for i in range(8):
    for j in range(8):
        if i % 2 == 1:
            if j %2 ==1:
                canvas.create_rectangle(0+40*i,0+40*j,40+40*i,40+40*j, fill = 'white')
            else:
                canvas.create_rectangle(0+40*i,0+40*j,40+40*i,40+40*j, fill = 'black')
        else:
            if j %2 ==1:
                canvas.create_rectangle(0+40*i,0+40*j,40+40*i,40+40*j, fill = 'black')
            else:
                canvas.create_rectangle(0+40*i,0+40*j,40+40*i,40+40*j, fill = 'white')


tk.mainloop()
