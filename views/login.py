from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
from views.admin_view import admin_view
from views.user_view import user_view


def login_gui(my_users_service, my_plant_service):
    def login_calback():
        username = username_entry.get()
        password = password_entry.get()
        user = my_users_service.find_user(username, password)
        if len(username) == 0:
            messagebox.showerror("Error", "Username can't be empty")
        elif len(password) == 0:
            messagebox.showerror("Error", "Password can't be empty")
        elif user is None:
            messagebox.showerror("Error", "User not found")
        elif user["username"] == "admin":
            messagebox.showinfo("Success", "Login successful")
            window.destroy()
            admin_view(my_users_service)
        else:
            user != "admin"
            my_name = user["first_name"]
            my_user_id = str(user["_id"])
            messagebox.showinfo("Welcome", "Hello " + my_name)
            window.destroy()
            user_view(my_plant_service, my_name, my_user_id)

    window = tk.Tk()
    window.title("PyFlora Login")
    window.geometry("350x400")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (350 // 2)
    y = (screen_height // 2) - (400 // 2)
    window.geometry(f"+{x}+{y}")
    img = Image.open("plant_img/login.png")
    bg_img = ImageTk.PhotoImage(img.resize((350, 400)))
    bg_label = tk.Label(window, image=bg_img)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
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

    username_label = tk.Label(
        window, text="Username:", padx=10, pady=10, bg="#f5f6f8", font=font
    )
    username_label.place(relx=0.5, y=90, anchor=tk.CENTER)
    username_entry = tk.Entry(window, font=font, fg="black")
    username_entry.place(relx=0.5, y=130, anchor=tk.CENTER)
    password_label = tk.Label(
        window, text="Password:", padx=10, pady=10, bg="#f5f6f8", font=font
    )
    password_label.place(relx=0.5, y=170, anchor=tk.CENTER)
    password_entry = tk.Entry(window, show="*", font=font)
    password_entry.place(relx=0.5, y=210, anchor=tk.CENTER)
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

    window.mainloop()
