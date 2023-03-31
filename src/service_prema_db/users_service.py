from ast import NotIn
from os import name
from typing import Collection
import pymongo
from pymongo.errors import PyMongoError
from tkinter import messagebox


class UsersService:
    def __init__(self, connection_uri: str, database_name: str, collection_name: str):
        self.client = pymongo.MongoClient(connection_uri)
        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

    # get_all_users
    def get_all_users(self):
        try:
            users = self.collection.find()
            print("\n".join([str(user) for user in users]))
            return [user for user in users]
        except PyMongoError as e:
            print(f"An error occurred while getting all users {e}")
            return []

    # find_user
    def find_user(self, username):
        try:
            user = self.collection.find_one({"username": username})
            if user:
                print(user)
                return user
            else:
                print("User not found")
                return None
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
        print(user_data["username"])
        return user_data

    # delete_user_by_username
    def del_user(self, username):
        user_dict = self.collection.find_one_and_delete({"username": username})
        if user_dict is not None:
            print("Deleted user:", user_dict["username"])
        else:
            print("User not found")
        return user_dict
