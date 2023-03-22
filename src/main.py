from controller.plant_contoller import PlantController
from controller.pot_contoller import PotController
from service.plant_service import PlantService
from service.pot_service import PotService


connection_uri = "mongodb://localhost:27017/"

database_name = "pyflora"

collection_name_plants = "plants"
collection_name_pots = "pots"


def main():

    ## PLANT SERVICE
    # connection on plant collection
    my_plant_service = PlantService(
        connection_uri, database_name, collection_name_plants
    )
    # get all plants
    my_plant_service.get_all_plants()

    # get plant by id
    my_plant_service.get_plant_by_id("641b717fb0e8281b85aa872e")

    # delete_plant_by_id
    my_plant_service.delete_plant_by_id("641b717fb0e8281b85aa872f")

    # update_plant_notes
    my_plant_service.update_plant_notes("641b717fb0e8281b85aa8730", "notes test set")

    ## POT SERVICE
    # connection on pot collection
    my_pot_service = PotService(connection_uri, database_name, collection_name_pots)

    # get all pots
    my_pot_service.get_all_pots()

    # get pot by id
    my_pot_service.get_pot_by_id("641b717fb0e8281b85aa8732")


if __name__ == "__main__":
    main()
