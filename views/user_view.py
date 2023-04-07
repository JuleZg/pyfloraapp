import tkinter as tk


def user_view(user, my_pot_service, my_plant_service):
    window = tk.Tk()
    user_id = str(user["_id"])
    window.title("User View")
    all_pots = my_pot_service.find_all_pots(user_id)  # TODO OVO SMO PROMIJENILI
    window.geometry("1920x1080")

    # get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate the x and y coordinates to center the window
    x = (screen_width // 2) - (1920 // 2)
    y = (screen_height // 2) - (1080 // 2)
    window.geometry(f"+{x}+{y}")

    # create a label widget for each pot
    for pot in all_pots:
        # get the plant associated with the pot
        plant = my_plant_service.find_plant_by_id(str(pot["plant_id"]))

        # create a label widget with information about the pot and its plant
        pot_label = tk.Label(
            window,
            text=f"Pot ID: {pot['_id']}, Pot Name: {pot['name']}, Plant Name: {plant['name']}, Watering Frequency: {plant['watering_frequency']}",
        )
        pot_label.pack()

    window.mainloop()
