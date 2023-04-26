from unicodedata import name
from aiohttp import TraceRequestExceptionParams
from bson import ObjectId
from discord import Object
import pymongo
from typing import List
from pymongo.errors import PyMongoError


class PlantService:
    # Constructor prima 3 parama, svaki je tipa String https://www.geeksforgeeks.org/constructors-in-python/
    def __init__(
        self,
        connection_uri: str,
        database_name: str,
        collection_plant: str,
        collection_user_plant: str,
    ):
        self.client = pymongo.MongoClient(connection_uri)  # spajanje na mongo klijent
        self.database = self.client[database_name]  # spajanje na bazu
        self.collection_plant = self.database[
            collection_plant
        ]  # spajanje na collection plants
        self.collection_user_plant = self.database[collection_user_plant]

    # destruktor https://www.geeksforgeeks.org/destructors-in-python/
    def __del__(
        self,
    ):
        self.client.close()

    # get_all_plants
    def find_all_plants(self):
        try:
            plants = self.collection_plant.find()
            # print("\n".join([str(plant) for plant in plants]))
            return [plant for plant in plants]
        except PyMongoError as e:
            print(f"An error occurred while getting all plants: {e}")
            return []

    # get_plant_by_id
    def find_plant_by_id(self, id):
        id_obj = ObjectId(id)
        plant_dict = self.collection_plant.find_one({"_id": id_obj})
        print(f"Plant found:  {plant_dict['name']}")
        return plant_dict

    # get_plant_by_name
    def find_plant_by_name(self, plant_name):
        plant_dict = self.collection_plant.find_one({"name": plant_name})
        print(f"Plant found: {plant_dict['name']}")
        return plant_dict

    # delete_plant_by_id
    def delete_plant_by_id(
        self, id
    ):  # TODO: U SVAKU FUNCKIJU PROSLIJEDIT ID_USERA KAO U
        id_obj = ObjectId(id)
        plant_dict_name = self.collection_plant.find_one({"_id": id_obj})
        print(f"Deleted plant : {plant_dict_name['name']}\n{plant_dict_name}")
        plant_dict = self.collection_plant.delete_one({"_id": id_obj})
        return plant_dict

    # update_plant_notes
    def update_plant_notes(self, id, notes):
        id_obj = ObjectId(id)
        plant_dict_name = list(
            self.collection_plant.find_one({"_id": id_obj})
        )  # TODO: SVE U LIST STAVLJAT GDJE IMAS FIND
        plant_dict_notes = {"$set": {"notes": notes}}
        self.collection_plant.update_one({"_id": id_obj}, plant_dict_notes)
        print(
            f"Notes updated for plant '{plant_dict_name['name']}', and with note '{notes}' "
        )
        return plant_dict_name

    # insert img to plants collection

    def insert_img(self, id):
        with open("src/scripts/plant_img/rose.png", "rb") as f:
            image_data = f.read()
        id_obj = ObjectId(id)
        plant_dict_name = self.collection_plant.find_one({"_id": id_obj})
        plant_dict_img = {"$set": {"image": image_data}}
        self.collection_plant.update_one({"_id": id_obj}, plant_dict_img)

        return print(plant_dict_name["name"], "img inserted.")

    def save_plant_for_user(self, user_id, plant_id):
        document = {"user_id": user_id, "plant_id": plant_id, "pot_id": None}
        # existing_doc = self.collection_user_plant.find_one(document)
        self.collection_user_plant.insert_one(document)

    # dohvati listu id-eva iz users_plant collectiona - OK
    # za svaki id iz liste zovi plant collection kako bi dohvatio ostale podatke od planta
    # vrati sve plantove i njihove podatke
    def get_user_plants(self, user_id):
        user_plants = self.collection_user_plant.find({"user_id": user_id})
        plant_data = []
        for plant in user_plants:
            plant_id_obj = ObjectId(plant["plant_id"])
            plant_details = self.collection_plant.find_one({"_id": plant_id_obj})
            if plant_details:
                plant_data.append({**plant_details, **plant})

        print("*" * 150)
        print(plant_data)
        return plant_data

    def add_plant_to_pot(self, user_plant_id, pot_id):
        """user_id_obj = ObjectId(user_id)
        plant_id_obj = ObjectId(plant_id)
        pot_id_obj = ObjectId(pot_id)"""
        # pronađi redak u tablici gdje se nalazi plant_id i user_id
        # dodaj mu pot_id

    def delete_user_plant(self, user_plant_id):
        #user_plant_id_obj = ObjectId(user_plant_id)  # ovo ako saljes kao string
        result = self.collection_user_plant.delete_one({"_id": user_plant_id})
        return result.deleted_count
