from service.plant_service import PlantService


connection_uri = "mongodb://localhost:27017/"

database_name = "pyflora"

collection_name = "plants"


def main():

    my_plant_service = PlantService(connection_uri, database_name, collection_name)

    plants = my_plant_service.get_all_plants()
    print(plants)

    plant = my_plant_service.get_plant_by_id("64160b3daf13e5b0efceb51e")
    print(plant)


if __name__ == "__main__":
    main()
