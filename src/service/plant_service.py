from unicodedata import name
from bson import ObjectId
import pymongo
from typing import List
from pymongo.errors import PyMongoError


class PlantService:
    # Constructor prima 3 parama, svaki je tipa String https://www.geeksforgeeks.org/constructors-in-python/
    def __init__(self, connection_uri: str, database_name: str, collection_name: str):
        self.client = pymongo.MongoClient(connection_uri)  # spajanje na mongo klijent
        self.database = self.client[database_name]  # spajanje na bazu
        self.collection = self.database[collection_name]  # spajanje na collection

    # destruktor https://www.geeksforgeeks.org/destructors-in-python/
    def __del__(
        self,
    ) -> None:
        self.client.close()

    # get_all_plants
    def get_all_plants(self) -> List[dict]:
        try:
            plants = self.collection.find()
            return [plant for plant in plants]
        except PyMongoError as e:
            print(f"An error occurred while getting all plants: {e}")
            return []

    # get_plant_by_id
    def get_plant_by_id(self, id):
        id_obj = ObjectId(id)
        plant_dict = self.collection.find_one({"_id": id_obj})
        print(f"NASLI BILJKU  {plant_dict['name']}")
        return plant_dict

    # delete_plant_by_id
    def delete_plant_by_id(self, id):
        id_obj = ObjectId(id)
        plant_dict_name = self.collection.find_one({"_id": id_obj})
        print(f"Deleted plant : {plant_dict_name['name']}\n{plant_dict_name}")
        plant_dict = self.collection.delete_one({"_id": id_obj})
        return plant_dict

    # TODO: update_plant_notes
    def update_plant_notes(self, id, notes):
        id_obj = ObjectId(id)
        plant_dict_name = self.collection.find_one({"_id": id_obj})
        plant_dict = self.collection.update_one(
            {"plant_dict_name['notes']": notes}, pymongo.UpdateOne
        )
        return plant_dict["notes"]
