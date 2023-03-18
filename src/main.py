from controller.plant_contoller import PlantController
from service.plant_service import PlantService
from service.pot_service import PotService


connection_uri = "mongodb://localhost:27017/"

database_name = "pyflora"

collection_name_plants = "plants"
collection_name_pots = "pots"


def main():

    my_plant_service = PlantService(
        connection_uri, database_name, collection_name_plants
    )

    # plants = my_plant_service.get_all_plants()
    # print(plants)
    #
    # plant = my_plant_service.get_plant_by_id("64160b3daf13e5b0efceb51e")
    # print(plant)
    #
    # my_pot_service = PotService(connection_uri, database_name, collection_name_pots)
    # pots = my_pot_service.get_all_pots()
    # pot = my_pot_service.get_pot_by_id("64162158d14c9ab38c704d64")
    # print(pots)
    # print()

    # print(pot)

    my_plant_controller = PlantController(my_plant_service)

    plants = my_plant_controller.get_all_plants()
    print(plants)
    print()
    plant = my_plant_controller.get_plant_by_id("64162158d14c9ab38c704d59")
    print(plant)


if __name__ == "__main__":
    main()
