import tkinter as tk

def create_new_window():
    new_window = tk.Toplevel(window)
    # configure new_window as desired
    new_window.title("New Window")
    new_window.geometry("400x400")
    new_window.configure(bg="white")
    # add widgets to new_window
    label = tk.Label(new_window, text="This is a new window")
    label.pack()

# add button to main window to create new window
new_window_button = tk.Button(window, text="New Window", command=create_new_window)
new_window_button.pack()

# create the main window
root = tk.Tk()

# add a button to create a new window
button = tk.Button(root, text="Create New Window", command=create_new_window)
button.pack()



# start the main event loop
root.mainloop()