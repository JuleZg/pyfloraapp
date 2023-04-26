from tkinter import *
from turtle import window_height, window_width

window = Tk()
window.geometry("800x600")
frame = Frame(window, width=500, height=400, bg="red")
frame.pack(side="top")
label = Label(frame, text="Hello, world!", width=300, height=200, bg="red")
label.grid(row=0, column=0, sticky="nesw")
window.mainloop()
