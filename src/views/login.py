from PIL import Image, ImageTk
import tkinter as tk


def main():

    # Create a new tkinter window
    window = tk.Tk()

    # Set the window title
    window.title("PyFlora Login")

    # Set the window size
    window.geometry("400x250")

    # get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate the x and y coordinates to center the window
    x = (screen_width // 2) - (300 // 2)
    y = (screen_height // 2) - (150 // 2)
    window.geometry(f"+{x}+{y}")
    # Load the image file
    img = Image.open("src/scripts/plant_img/login.png")

    # Convert the image to a PhotoImage object
    bg_img = ImageTk.PhotoImage(img.resize((400, 250)))

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
    welcome_label.place(x=150, y=10)

    # label for the username
    password_label = tk.Label(
        window,
        text="Username:",
        padx=10,
        pady=10,
        bg="#f5f6f8",
        font=font,
    )
    password_label.place(x=60, y=50)

    # entry field for the username

    username_entry = tk.Entry(window, font=font, fg="grey")
    username_entry.place(x=160, y=60)

    # label for the password
    password_label = tk.Label(
        window,
        text="Password:",
        padx=10,
        pady=10,
        bg="#f5f6f8",
        font=font,
    )
    password_label.place(x=60, y=90)

    # entry field for the password
    password_entry = tk.Entry(
        window,
        show="*",
        font=font,
    )
    password_entry.place(x=160, y=100)

    # login button
    login_button = tk.Button(
        window,
        text="Login",
        padx=5,
        pady=5,
        bg="#f5f6f8",
        font=font,
    )
    login_button.place(x=180, y=140)

    # Start the main loop of the window
    window.mainloop()


if __name__ == "__main__":
    main()
