from PIL import Image, ImageTk
import tkinter as tk


def main():

    window = tk.Tk()

    window.title("Plant View")

    window.geometry("1920x1080")

    # get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate the x and y coordinates to center the window
    x = (screen_width // 2) - (1920 // 2)
    y = (screen_height // 2) - (1080 // 2)
    window.geometry(f"+{x}+{y}")

    window.mainloop()


if __name__ == "__main__":
    main()
