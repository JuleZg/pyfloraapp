import tkinter as tk

# create the main window
root = tk.Tk()
root.geometry("400x200")

# create two frames
frame1 = tk.Frame(root, bg="red", width=200, height=200)
frame2 = tk.Frame(root, bg="blue", width=200, height=200)

# pack the frames side by side
frame1.pack(side="left", fill="both", expand=True)
frame2.pack(side="right", fill="both", expand=True)

# start the main loop
root.mainloop()
