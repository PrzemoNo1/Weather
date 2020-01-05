import Tkinter as tk

HEIGHT = 450
WIDTH = 800

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='blue', bd=5)
frame.place(relx=0.5, rely = 0.2, relwidth=0.7, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relx=0, rely=0, relwidth=0.6, relheight=1)

button = tk.Button(frame, text='test button', font = 40)
button.place(relx=0.65, relwidth=0.35, relheight=1)

lower_frame = tk.Frame(root, bg='blue', bd=5)
lower_frame.place(relx=0.5, rely = 0.35, relwidth=0.7, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg='yellow', text='This is label')
label.place(relwidth=1, relheight=1)

root.mainloop()