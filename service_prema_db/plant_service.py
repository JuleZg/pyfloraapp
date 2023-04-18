from unicodedata import name
from aiohttp import TraceRequestExceptionParams
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
    ):
        self.client.close()

    # get_all_plants
    def find_all_plants(self):
        try:
            plants = self.collection.find()
            #print("\n".join([str(plant) for plant in plants]))
            return [plant for plant in plants]
        except PyMongoError as e:
            print(f"An error occurred while getting all plants: {e}")
            return []

    # get_plant_by_id
    def find_plant_by_id(self, id):
        id_obj = ObjectId(id)
        plant_dict = self.collection.find_one({"_id": id_obj})
        print(f"Plant found:  {plant_dict['name']}")
        return plant_dict

    # get_plant_by_name
    def find_plant_by_name(self, plant_name):
        plant_dict = self.collection.find_one({"name": plant_name})
        print(f"Plant found: {plant_dict['name']}")
        return plant_dict

    # delete_plant_by_id
    def delete_plant_by_id(self, id): #TODO: U SVAKU FUNCKIJU PROSLIJEDIT ID_USERA KAO U 
        id_obj = ObjectId(id)
        plant_dict_name = self.collection.find_one({"_id": id_obj})
        print(f"Deleted plant : {plant_dict_name['name']}\n{plant_dict_name}")
        plant_dict = self.collection.delete_one({"_id": id_obj})
        return plant_dict

    # update_plant_notes
    def update_plant_notes(self, id, notes):
        id_obj = ObjectId(id)
        plant_dict_name = list(self.collection.find_one({"_id": id_obj})) #TODO: SVE U LIST STAVLJAT GDJE IMAS FIND
        plant_dict_notes = {"$set": {"notes": notes}}
        self.collection.update_one({"_id": id_obj}, plant_dict_notes)
        print(
            f"Notes updated for plant '{plant_dict_name['name']}', and with note '{notes}' "
        )
        return plant_dict_name

    # insert img to plants collection

    def insert_img(self, id):
        with open("src/scripts/plant_img/rose.png", "rb") as f:
            image_data = f.read()
        id_obj = ObjectId(id)
        plant_dict_name = self.collection.find_one({"_id": id_obj})
        plant_dict_img = {"$set": {"image": image_data}}
        self.collection.update_one({"_id": id_obj}, plant_dict_img)

        return print(plant_dict_name["name"], "img inserted.")
