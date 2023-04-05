from turtle import mainloop
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
from matplotlib.pyplot import show
from os import name
from views.main_view import main_view
from service_prema_db.users_service import UsersService


def login_gui():
    def login_calback():
        connection_uri = "mongodb://localhost:27017/"
        database_name = "pyflora"
        collection_name_users = "users"
        my_users_service = UsersService(
            connection_uri, database_name, collection_name_users
        )
        username = username_entry.get()
        password = password_entry.get()
        user = my_users_service.find_user(username)
        if user is None:
            messagebox.showerror("Error", "Invalid username")
        elif len(password) == 0:
            messagebox.showerror("Error", "Password cant be empty")
        elif password != user["password"]:
            messagebox.showerror("Error", "Incorrect password")
        else:
            messagebox.showinfo("Success", "Login successful")
            window.destroy()
            main_view()

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
    img = Image.open("plant_img/login.png")
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
    welcome_label.place(relx=0.5, y=40, anchor=tk.CENTER)
    # label for the username
    username_label = tk.Label(
        window, text="Username:", padx=10, pady=10, bg="#f5f6f8", font=font
    )
    username_label.place(relx=0.5, y=90, anchor=tk.CENTER)
    # entry field for the username
    username_entry = tk.Entry(window, font=font, fg="black")
    username_entry.place(relx=0.5, y=130, anchor=tk.CENTER)
    # label for the password
    password_label = tk.Label(
        window, text="Password:", padx=10, pady=10, bg="#f5f6f8", font=font
    )
    password_label.place(relx=0.5, y=170, anchor=tk.CENTER)
    # entry field for the password
    password_entry = tk.Entry(window, show="*", font=font)
    password_entry.place(relx=0.5, y=210, anchor=tk.CENTER)
    # login button
    login_button = tk.Button(
        window,
        text="Login",
        padx=20,
        pady=5,
        bg="#f5f6f8",
        font=font,
        width=10,
        command=login_calback,
    )
    login_button.place(relx=0.5, y=260, anchor=tk.CENTER)

    # Start the main loop of the window
    window.mainloop()
