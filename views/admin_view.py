from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import datetime
import sys


def admin_view(my_users_service):
    def on_closing():
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            sys.exit(0)
            window.destroy()

    # methods for add new user, delete selected user
    def repopulate_user_table(all_users):
        user_table.delete(*user_table.get_children())
        for user in all_users:
            user_table.insert(
                "",
                "end",
                values=(
                    user["username"],
                    user["password"],
                    user["first_name"],
                    user["last_name"],
                    user["email"],
                ),
            )

    def delete_selected_user():
        selected_item = user_table.selection()
        if selected_item:
            username = user_table.item(selected_item)["values"][0]
            my_users_service.delete_user(username)
            user_table.delete(selected_item)
            all_users = my_users_service.find_all_users()
            repopulate_user_table(all_users)

    def add_new_user():
        def submit_new_user(username, password, first_name, last_name, email):
            my_users_service.add_user(username, password, first_name, last_name, email)
            all_users = my_users_service.find_all_users()
            repopulate_user_table(all_users)
            add_user_window.destroy()

        # Create a new window
        add_user_window = tk.Toplevel(window)
        add_user_window.title("Add User")
        add_user_window.geometry("400x300")

        # Create a form for adding a new user
        username_label = tk.Label(add_user_window, text="Username:")
        username_label.pack()
        username_entry = tk.Entry(add_user_window)
        username_entry.pack()

        password_label = tk.Label(add_user_window, text="Password:")
        password_label.pack()
        password_entry = tk.Entry(add_user_window)
        password_entry.pack()

        first_name_label = tk.Label(add_user_window, text="First Name:")
        first_name_label.pack()
        first_name_entry = tk.Entry(add_user_window)
        first_name_entry.pack()

        last_name_label = tk.Label(add_user_window, text="Last Name:")
        last_name_label.pack()
        last_name_entry = tk.Entry(add_user_window)
        last_name_entry.pack()

        email_label = tk.Label(add_user_window, text="Email:")
        email_label.pack()
        email_entry = tk.Entry(add_user_window)
        email_entry.pack()

        # Add a button to submit the form
        submit_button = tk.Button(
            add_user_window,
            text="Submit",
            command=lambda: submit_new_user(
                username_entry.get(),
                password_entry.get(),
                first_name_entry.get(),
                last_name_entry.get(),
                email_entry.get(),
            ),
        )
        submit_button.pack()

    def update_time():
        now = datetime.datetime.now()
        date_time_label.config(text=now.strftime("%d.%m.%Y %H:%M:%S").format())
        window.after(1000, update_time)

    window = tk.Tk()
    window.title("Admin View")
    window.attributes("-fullscreen", True)
    # background
    img = Image.open("plant_img/admin_view_bg2.png")
    # bg_img = ImageTk.PhotoImage(img)
    bg_img = ImageTk.PhotoImage(img.resize((1920, 1000)))
    bg_label = tk.Label(window, image=bg_img)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    all_users = my_users_service.find_all_users()
    window.geometry("1920x1000")
    FONT = ("Roboto Mono", 12)
    # get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # calculate the x and y coordinates to center the window
    x = (screen_width // 2) - (1920 // 2)
    y = (screen_height // 2) - (1080 // 2)
    window.geometry(f"+{x}+{y}")

    # Create a header frame with a title label and a button to return to the dashboard
    header_frame = tk.Frame(window, bg="blue", padx=20, pady=10)
    header_frame.pack(side="top", fill="x")
    title_label = tk.Label(
        header_frame, text="USER MANAGMENT", font=FONT, fg="white", bg="blue"
    )
    title_label.place(relx=0.5, rely=0.5, anchor="center")

    dashboard_button = tk.Button(
        header_frame,
        text="Close Admin View",
        command=on_closing,
        bg="#e3dfe0",
        fg="#0000cd",
        font=FONT,
        relief="raised",
    )
    dashboard_button.pack(side="right", padx=10)

    date_time_label = tk.Label(header_frame, font=FONT)
    date_time_label.pack(side="left", padx=10)

    # Create a second header frame with a red background color
    add_delete_frame = tk.Frame(window, padx=20, pady=10, bg="#e3dfe0")
    add_delete_frame.pack(side="top", fill="x")

    add_delete_label = tk.Label(
        add_delete_frame,
        text="Add/Delete User",
        font=FONT,
        fg="#0000cd",
        bg="#e3dfe0",
    )
    add_delete_label.place(relx=0.5, rely=0.5, anchor="center")

    # delete user button
    delete_user = tk.Button(
        add_delete_frame,
        text="Delete selected user",
        command=delete_selected_user,
        font=FONT,
        bg="#e3dfe0",
        fg="#0000cd",
        relief="raised",
    )
    delete_user.pack(side="right", padx=10)

    # add user button
    add_user = tk.Button(
        add_delete_frame,
        text="Add new user",
        command=add_new_user,
        font=FONT,
        bg="#e3dfe0",
        fg="#0000cd",
        relief="raised",
    )
    add_user.pack(side="left", padx=10)

    # user table frame and table
    user_table_frame = tk.Frame(window)
    user_table_frame.pack(side="bottom", fill="y", expand=True)

    user_table = ttk.Treeview(
        user_table_frame,
        columns=("username", "password", "first_name", "last_name", "email"),
        show="headings",
    )
    user_table.heading("username", text="Username")
    user_table.column("username", anchor="w")
    user_table.heading("password", text="Password")
    user_table.column("password", anchor="w")
    user_table.heading("first_name", text="First name")
    user_table.column("first_name", anchor="w")
    user_table.heading("last_name", text="Last name")
    user_table.column("last_name", anchor="w")
    user_table.heading("email", text="Email")
    user_table.column("email", anchor="w")
    user_table.pack(side="top", fill="both", expand=True)

    for user in all_users:
        user_table.insert(
            "",
            "end",
            values=(
                user["username"],
                user["password"],
                user["first_name"],
                user["last_name"],
                user["email"],
            ),
        )
    update_time()
    window.mainloop()
