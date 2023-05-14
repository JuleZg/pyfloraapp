from service_prema_db.plant_service import PlantService
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
    my_users_service = UsersService(
        connection_uri, database_name, collection_name_users
    )

    login_gui(my_users_service, my_plant_service)


if __name__ == "__main__":
    main()
