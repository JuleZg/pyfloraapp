from matplotlib import collections
from controller_prema_GUI.plant_contoller import PlantController
from controller_prema_GUI.pot_contoller import PotController
from scripts.pyflora_mongodb import drop_collection
from service_prema_db.plant_service import PlantService
from service_prema_db.pot_service import PotService
from PIL import Image

connection_uri = "mongodb://localhost:27017/"

database_name = "pyflora"

collection_name_plants = "plants"
collection_name_pots = "pots"


def main():

    # PLANT SERVICE
    # connection on plant collection
    my_plant_service = PlantService(
        connection_uri, database_name, collection_name_plants
    )

    # POT SERVICE
    # connection on pot collection
    my_pot_service = PotService(connection_uri, database_name, collection_name_pots)

    # my_plant_service.update_plant_notes("641b30a899ff01dc7d7de37d", "test_push 2")

    # insert img to plants collection

    # my_plant_service.insert_img("641b88ed057c974b9384ab2e")

    # my_pot_service.delete_pot_by_id("6421d6ca847a39db9a67ca19")

    # my_pot_service.get_pot_by_name("Pot3")


if __name__ == "__main__":
    main()


# Create a collection for the users
collection_name = "users"
collection(db[collection_name])

drop_collection(collection_name, db)
users = []

# Insert the user data into the collection
collection.insert_many(users)

# Print the inserted data
for user in collection.find():
    print(user)
