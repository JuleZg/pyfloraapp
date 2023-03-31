from PIL import Image, ImageTk
import tkinter as tk

from numpy import size


def main():

    # Create a new tkinter window
    window = tk.Tk()

    # Set the window title
    window.title("PyFlora Login")

    # Set the window size
    window.geometry("350x400")

    # get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate the x and y coordinates to center the window
    x = (screen_width // 2) - (350 // 2)
    y = (screen_height // 2) - (400 // 2)
    window.geometry(f"+{x}+{y}")
    # Load the image file
    img = Image.open("src/scripts/plant_img/login.png")

    # Convert the image to a PhotoImage object
    bg_img = ImageTk.PhotoImage(img.resize((350, 400)))

    # Create a label with the image as the background
    bg_label = tk.Label(window, image=bg_img)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # welcome label
    font = ("Roboto Mono", 12)
    welcome_label = tk.Label(
        window,
        text="Login to Your Account",
        padx=10,
        pady=10,
        bg="#f5f6f8",
        font=font,
    )
    welcome_label.place(
        relx=0.5,
        y=40,
        anchor=tk.CENTER,
    )

    # label for the username
    username_label = tk.Label(
        window,
        text="Username:",
        padx=10,
        pady=10,
        bg="#f5f6f8",
        font=font,
    )
    username_label.place(
        relx=0.5,
        y=90,
        anchor=tk.CENTER,
    )

    # entry field for the username

    username_entry = tk.Entry(
        window,
        font=font,
        fg="black",
    )
    username_entry.place(
        relx=0.5,
        y=130,
        anchor=tk.CENTER,
    )

    # label for the password
    password_label = tk.Label(
        window,
        text="Password:",
        padx=10,
        pady=10,
        bg="#f5f6f8",
        font=font,
    )
    password_label.place(
        relx=0.5,
        y=170,
        anchor=tk.CENTER,
    )

    # entry field for the password
    password_entry = tk.Entry(
        window,
        show="*",
        font=font,
    )
    password_entry.place(
        relx=0.5,
        y=210,
        anchor=tk.CENTER,
    )

    # login button
    login_button = tk.Button(
        window,
        text="Login",
        padx=20,
        pady=5,
        bg="#f5f6f8",
        font=font,
        width=10,
    )
    login_button.place(
        relx=0.5,
        y=260,
        anchor=tk.CENTER,
    )

    # Start the main loop of the window
    window.mainloop()


if __name__ == "__main__":
    main()
