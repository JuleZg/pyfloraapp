from controller_prema_GUI.plant_controller import PlantController
from controller_prema_GUI.pot_controller import PotController
from service_prema_db.plant_service import PlantService
from service_prema_db.pot_service import PotService
from service_prema_db.users_service import UsersService

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
    my_plant_service.get_plant_by_id("6421e008374ca67c01d8647c")

    # delete_plant_by_id
    my_plant_service.delete_plant_by_id("6421e008374ca67c01d8647d")

    # update_plant_notes
    my_plant_service.update_plant_notes("6421e008374ca67c01d8647e", "notes test set")

    ## POT SERVICE
    # connection on pot collection
    my_pot_service = PotService(connection_uri, database_name, collection_name_pots)

    # get all pots
    my_pot_service.get_all_pots()

    # get pot by id
    my_pot_service.get_pot_by_id("6421e008374ca67c01d86480")

    # get pot by name
    my_pot_service.get_pot_by_name("Pot4")

    ## USER SERVICE
    # connection on pot collection
    my_users_service = UsersService(
        connection_uri, database_name, collection_name_users
    )
    # get_all_users
    my_users_service.get_all_users()

    ## POT CONTROLLER
    # connection on pot collection
    my_pot_controller = PotController(
        connection_uri, database_name, collection_name_pots
    )
    my_pot_controller.get_all_pots()
    print()
    my_pot_controller.get_pot_by_name("Pot0")
    print()
    my_pot_controller.get_pot_by_id("642471298f5fbe8430a5c7ad")
    print()
    my_pot_controller.delete_pot_by_id("642471298f5fbe8430a5c7b0")


if __name__ == "__main__":
    main()
