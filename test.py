import tkinter as tk

window = tk.Tk()
window.geometry("1920x1000")

# get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
print(screen_width)
print(screen_height)
# calculate the x and y coordinates to center the window
x = (screen_width // 2) - (1920 // 2)
y = (screen_height // 2) - (1080 // 2)

print((screen_width // 2) - (1920 // 2))
print((screen_height // 2) - (1080 // 2))
window.geometry(f"+{x}+{y}")
