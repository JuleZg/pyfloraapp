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
from controller_prema_GUI.plant_controller import PlantController
from controller_prema_GUI.pot_controller import PotController
from controller_prema_GUI.users_controler import UsersController
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

    my_plant_service = PlantService(
        connection_uri, database_name, collection_name_plants
    )
    my_pot_service = PotService(connection_uri, database_name, collection_name_pots)

    my_users_service = UsersService(
        connection_uri, database_name, collection_name_users
    )

    my_pot_controller = PotController(
        connection_uri, database_name, collection_name_pots
    )

    my_plant_controller = PlantController(
        connection_uri, database_name, collection_name_plants
    )

    my_users_controller = UsersController(
        connection_uri, database_name, collection_name_users
    )


if __name__ == "__main__":
    main()
