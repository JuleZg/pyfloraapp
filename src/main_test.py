"""from matplotlib import collections
from controller_prema_GUI.plant_contoller import PlantController
from controller_prema_GUI.pot_contoller import PotController
from scripts.pyflora_mongodb import drop_collection
from service_prema_db.plant_service import PlantService
from service_prema_db.pot_service import PotService
from service_prema_db.users_service import UsersService
from PIL import Image"""
from PIL import Image, ImageTk
from turtle import bgpic, position
from controller_prema_GUI.plant_contoller import PlantController
from controller_prema_GUI.pot_contoller import PotController
from service_prema_db.plant_service import PlantService
from service_prema_db.pot_service import PotService
from service_prema_db.users_service import UsersService
import tkinter as tk

connection_uri = "mongodb://localhost:27017/"

database_name = "pyflora"

collection_name_plants = "plants"
collection_name_pots = "pots"
collection_name_users = "users"


def main():

    ## PLANT SERVICE
    # connection on plant collection
    my_plant_service = PlantService(
        connection_uri, database_name, collection_name_plants
    )
    # get all plants
    my_plant_service.get_all_plants()

    # get plant by id
    #    my_plant_service.get_plant_by_id("6424516c9f5578411f95004c")

    # delete_plant_by_id
    #    my_plant_service.delete_plant_by_id("6424516c9f5578411f95004d")

    # update_plant_notes
    #    my_plant_service.update_plant_notes("6424516c9f5578411f95004e", "notes test set")

    # insert_img_plant
    # my_plant_service.insert_img("6424516c9f5578411f95004c")

    ## POT SERVICE
    # connection on pot collection
    my_pot_service = PotService(connection_uri, database_name, collection_name_pots)

    # get all pots
    #    my_pot_service.get_all_pots()

    # get pot by id
    #    my_pot_service.get_pot_by_id("6424516c9f5578411f950056")

    # get pot by name
    #    my_pot_service.get_pot_by_name("Pot4")

    # USER SERVICE
    # connection on pot collection
    my_users_service = UsersService(
        connection_uri, database_name, collection_name_users
    )
    # get_all_users
    my_users_service.get_all_users()

    # add user
    # my_users_service.add_user("maja", "maja", "maja", "majic", "maja@email.com")

    # delete user
    # my_users_service.del_user("maja")


# Create a new tkinter window
window = tk.Tk()

# Set the window title
window.title("Login")

# Set the window size
window.geometry("300x150")

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
bg_img = ImageTk.PhotoImage(img.resize((300, 150)))

# Create a label with the image as the background
bg_label = tk.Label(window, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


# Add an entry field for the username
username_entry = tk.Entry(window)
username_entry.pack()

# Add a label for the password
password_label = tk.Label(window, text="Password:")
password_label.pack()

# Add an entry field for the password
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Add a login button
login_button = tk.Button(window, text="Login")
login_button.pack()

# Start the main loop of the window
window.mainloop()

if __name__ == "__main__":
    main()
