from bson import ObjectId
import pymongo
from typing import List
from pymongo.errors import PyMongoError


class PotService:
    # Constructor prima 3 parama, svaki je tipa String https://www.geeksforgeeks.org/constructors-in-python/
    def __init__(self, connection_uri: str, database_name: str, collection_name: str):
        self.client = pymongo.MongoClient(connection_uri)  # spajanje na mongo klijent
        self.database = self.client[database_name]  # spajanje na bazu
        self.collection = self.database[collection_name]  # spajanje na collection

    def get_all_pots(self):  # -> List[dict]-> JE ZA RETURN TYPE
        try:
            pots = self.collection.find()
            return [pot for pot in pots]
        except PyMongoError as e:
            print(f"An error occurred while getting all plants: {e}")
            return []

    def get_pot_by_id(self, pot_id):
        id_obj = ObjectId(pot_id)  # KREIRAMO ID_OBJECT TIPA ObjectId
        pot_dict = self.collection.find_one({"_id": id_obj})
        print(f"NASLI POT  {pot_dict['name']}")
        return pot_dict

    # TODO: delete_pot_by_id
    def delete_pot_by_id(self, pot_id):
        id_obj = ObjectId(pot_id)
        pot_dict_name = self.collection.find_one({"_id": id_obj})  # delete by id
        print(f"Deleted pot : {pot_dict_name['name']}\n{pot_dict_name}")
        pot_dict = self.collection.delete_one({"_id": id_obj})  # delete by id
        return pot_dict

    # TODO: add_plant_to_pot
    def add_plant_to_pot(self, plant_id, pot_id):
        print("not implemented")
