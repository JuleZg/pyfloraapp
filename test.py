import tkinter as tk

def update_label_text():
    new_label1=label.config(text="New label text")

root = tk.Tk()

label = tk.Label(root, text="Original label text")
label.pack()

button = tk.Button(root, text="Update label text", command=update_label_text)
button.pack()

root.mainloop()
