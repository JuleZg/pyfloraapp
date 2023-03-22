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

    plant_update = my_plant_service.update_plant_notes(
        "641b30a899ff01dc7d7de385", "test"
    )


if __name__ == "__main__":
    main()
