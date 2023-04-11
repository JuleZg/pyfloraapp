from ast import NotIn
from os import name
from typing import Collection
import pymongo
from pymongo.errors import PyMongoError


class UsersService:
    def __init__(self, connection_uri: str, database_name: str, collection_name: str):
        self.client = pymongo.MongoClient(connection_uri)
        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

    # find_all_users
    def find_all_users(self):
        try:
            users = list(self.collection.find())
            print("\n".join([str(user) for user in users]))
            count = self.collection.count_documents({})
            print(f"Number of documents in the collection: {count}")
            return users
        except PyMongoError as e:
            print(f"An error occurred while getting all users {e}")
            return []

    # find_user
    def find_user(self, username, password):
        try:
            user = self.collection.find_one(
                {"username": username, "password": password}
            )
            if user:
                print(user)
                return user
            else:
                return print("User not found")
        except PyMongoError as e:
            print(f"An error occurred while getting the user {username}: {e}")
            return None

    # add user
    def add_user(self, username, password, first_name, last_name, email):
        user_data = {
            "username": username,
            "password": password,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
        }
        new_user = self.collection.insert_one(user_data)
        # print(user_data["username"])
        return user_data

    # delete_user_by_username
    def delete_user(self, username):
        user_dict = self.collection.find_one_and_delete({"username": username})
        if user_dict is not None:
            print("Deleted user:", user_dict["username"])
        else:
            print("User not found")
        return user_dict
