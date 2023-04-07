from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk


def admin_view(my_users_service):
    window = tk.Tk()
    window.title("Admin View")
    all_users = my_users_service.find_all_users()
    window.geometry("1920x1000")

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
        header_frame, text="USER MANAGMENT", font=("Arial", 20), fg="white", bg="blue"
    )
    title_label.place(relx=0.5, rely=0.5, anchor="center")

    dashboard_button = tk.Button(
        header_frame,
        text="Return to Dashboard",
        command=window.destroy,
        bg="white",
        fg="blue",
        relief="flat",
    )
    dashboard_button.pack(side="right", padx=10)
    #################################################################
    edit_user_frame = tk.Frame(
        window, bg="red", padx=20, pady=10, height=header_frame.winfo_height()
    )
    edit_user_frame.pack(side="top", fill="both", expand=True)

    button1 = tk.Button(
        edit_user_frame,
        text="Add User",
        bg="white",
        fg="blue",
        relief="flat",
        width=dashboard_button["width"],
        height=dashboard_button["height"],
    )
    button1.pack(side="left", padx=20)

    button2 = tk.Button(
        edit_user_frame,
        text="Delete User",
        bg="white",
        fg="blue",
        relief="flat",
        width=dashboard_button["width"],
        height=dashboard_button["height"],
    )
    button2.pack(side="right", padx=20)
    #################################################################

    # Create a user table using the Treeview widget
    user_table = ttk.Treeview(
        window,
        columns=("username", "password", "first_name", "last_name", "email", "actions"),
        show="headings",
    )
    user_table.heading("username", text="Username")
    user_table.column("username", anchor="center")  # Set anchor to center
    user_table.heading("password", text="Password")
    user_table.column("password", anchor="center")  # Set anchor to center
    user_table.heading("first_name", text="First name")
    user_table.column("first_name", anchor="center")  # Set anchor to center
    user_table.heading("last_name", text="Last name")
    user_table.column("last_name", anchor="center")  # Set anchor to center
    user_table.heading("email", text="Email")
    user_table.column("email", anchor="center")  # Set anchor to center
    user_table.heading("actions", text="Actions")
    user_table.column("actions", anchor="center")  # Set anchor to center
    user_table.pack(side="top", fill="both", expand=True)

    # Create a button widget for each user in the table

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

    window.mainloop()
