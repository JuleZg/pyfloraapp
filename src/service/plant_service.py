from bson import ObjectId
import pymongo
from typing import List
from pymongo.errors import PyMongoError
import json
from types import SimpleNamespace


class PlantService:
    # Constructor prima 3 parama, svaki je tipa String
    def __init__(self, connection_uri: str, database_name: str, collection_name: str):
        self.client = pymongo.MongoClient(connection_uri)  # spajanje na mongo klijent
        self.database = self.client[database_name]  # spajanje na bazu
        self.collection = self.database[collection_name]  # spajanje na collection

    def __del__(self) -> None:
        self.client.close()

    def get_all_plants(self) -> List[dict]:
        try:
            plants = self.collection.find()
            return [plant for plant in plants]
        except PyMongoError as e:
            print(f"An error occurred while getting all plants: {e}")
            return []

    def get_plant_by_id(self, id):
        id_obj = ObjectId(id)
        plant_dict = self.collection.find_one({"_id": id_obj})

        print(f"NASLI BILJKU  {plant_dict['name']}")
        return plant_dict
