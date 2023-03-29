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
            documents = self.collection.find()
            for user in documents:
                print(user)
            return [user for user in documents]
        except PyMongoError as e:
            print(f"An error occurred while getting all users {e}")
            return []

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
        return print("Added new user: "), {new_user["first_name"]}

    # delete_user_by_username
    def del_user(self, username):
        user_dict = self.collection.find_one_and_delete({"username": username})
        if user_dict is not None:
            print("Deleted user:", user_dict["username"])
        else:
            print("User not found")
        return user_dict
