import Tkinter as tk

HEIGHT = 450
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='blue')
frame.place(relx=0.4, rely = 0.3, relwidth=0.8, relheight=0.8)

button = tk.Button(root, text='test button')
button.pack()

root.mainloop()