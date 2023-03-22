from controller.plant_contoller import PlantController
from controller.pot_contoller import PotController
from service.plant_service import PlantService
from service.pot_service import PotService


connection_uri = "mongodb://localhost:27017/"

database_name = "pyflora"

collection_name_plants = "plants"
collection_name_pots = "pots"


def main():

    # plant service
    my_plant_service = PlantService(
        connection_uri, database_name, collection_name_plants
    )  # connection on plant collection
    plants = my_plant_service.get_all_plants()  # get all plants
    print(f"ALL PLANTS:\n", plants)
    print("_" * 150)
    plant = my_plant_service.get_plant_by_id(
        "6419f0ed371b2b9e7c70d494"
    )  # get plant by id
    print(f"PLANT BY ID:\n", plant)
    print("_" * 150)

    del_plant_by_id = my_plant_service.delete_plant_by_id("641b27ec6601e414fdcc11c5")
    print("_" * 150)

    # pot service
    my_pot_service = PotService(
        connection_uri, database_name, collection_name_pots
    )  # connection on pot collection
    pots = my_pot_service.get_all_pots()  # get all pots
    print(f"ALL POTS:\n", pots)
    print("_" * 150)

    pot = my_pot_service.get_pot_by_id("641b1c565b7a33ba48cd282e")  # get pot by id
    print(f"POT BY ID:\n", pot)
    print("_" * 150)


if __name__ == "__main__":
    main()
