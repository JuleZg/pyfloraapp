"""from service_prema_db.plant_service import PlantService
from service_prema_db.pot_service import PotService
from service_prema_db.users_service import UsersService
from views.login import login_gui
from views.user_view import user_view
from tkinter import *

connection_uri = "mongodb://localhost:27017/"
database_name = "pyflora"
collection_name_plants = "plants"
collection_name_pots = "pots"
collection_name_users = "users"
collection_name_user_plant = "user_plant"


def main():
    my_plant_service = PlantService(
        connection_uri,
        database_name,
        collection_name_plants,
        collection_name_user_plant,
    )
    # my_plant_service.find_all_plants()
    my_pot_service = PotService(connection_uri, database_name, collection_name_pots)

    my_users_service = UsersService(
        connection_uri, database_name, collection_name_users
    )



if __name__ == "__main__":
    main()"""
from service_prema_db.plant_service import PlantService
from service_prema_db.pot_service import PotService
from service_prema_db.users_service import UsersService
from views.login import login_gui


connection_uri = "mongodb://localhost:27017/"
database_name = "pyflora"
collection_name_plants = "plants"
collection_name_pots = "pots"
collection_name_users = "users"
collection_name_user_plant = "user_plant"


def main():
    my_plant_service = PlantService(
        connection_uri,
        database_name,
        collection_name_plants,
        collection_name_user_plant,
    )
    # my_plant_service.find_all_plants()
    my_pot_service = PotService(connection_uri, database_name, collection_name_pots)

    my_users_service = UsersService(
        connection_uri, database_name, collection_name_users
    )

    # my_plant_service.save_plant_for_user( "6436d92c71034b4156556e28", "643ea5a565423be96a729c5a"    )

    # some_data = my_plant_service.get_user_plants("64355ec03a881fc338fadc5d")

    # my_plant_service.delete_user_plant("64418c1b211c7806cace8b61")  # tu saljes id od pot_plant "dokumenta"

    # print("test gotov")
    # my_plant_service.get_user_plants("644667755556f1581b214a8b")
    # print(some_data)
    # my_plant_service.save_plant_for_user(        "644667755556f1581b214a8b", "64466747b4a5c6af6eae2a54"    )
    login_gui(my_users_service, my_pot_service, my_plant_service)


if __name__ == "__main__":
    main()
