import pymongo
import pymongo
from pymongo.errors import PyMongoError


class UsersService:
    def __init__(self, connection_uri: str, database_name: str, collection_name: str):
        self.client = pymongo.MongoClient(connection_uri)
        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

    # get_all_users
    def get_all_users(self):
        try:
            users = self.collection.find()
            return [user for user in users]
        except PyMongoError as e:
            print(f"An error occurred while getting all users {e}")
            return []
