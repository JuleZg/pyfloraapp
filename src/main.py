from controller.plant_contoller import PlantController
from controller.pot_contoller import PotController
from service.plant_service import PlantService
from service.pot_service import PotService


connection_uri = "mongodb://localhost:27017/"

database_name = "pyflora"

collection_name_plants = "plants"
collection_name_pots = "pots"


def main():

    # PLANT SERVICE
    my_plant_service = PlantService(
        connection_uri, database_name, collection_name_plants
    )  # connection on plant collection

    # get all plants
    plants = my_plant_service.get_all_plants()
    print(f"ALL PLANTS:\n", plants)
    # get plant by id
    plant = my_plant_service.get_plant_by_id("641b2b395ca59220a1a90c1f")
    print(f"PLANT BY ID:\n", plant)
    # delete_plant_by_id
    del_plant_by_id = my_plant_service.delete_plant_by_id("641b2b395ca59220a1a90c1b")
    print(f"DELETED PLANT BY ID:\n", del_plant_by_id)
    # POT SERVICE
    my_pot_service = PotService(
        connection_uri, database_name, collection_name_pots
    )  # connection on pot collection
    pots = my_pot_service.get_all_pots()  # get all pots
    print(f"ALL POTS:\n", pots)
    pot = my_pot_service.get_pot_by_id("641b2b395ca59220a1a90c28")  # get pot by id
    print(f"POT BY ID:\n", pot)


if __name__ == "__main__":
    main()
