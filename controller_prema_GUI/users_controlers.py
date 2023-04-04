from pyclbr import Class

from colorama import init
from service_prema_db.users_service import UsersService


class UsersController:
    def __init__(self, connection_uri, database_name, collection_name_users):
        self.service = UsersService(
            connection_uri, database_name, collection_name_users
        )

    def find_all_users(self):
        return self.service.get_all_users()

    def find_user(self, username):
        return self.service.find_user(username)

    def add_user(self, username, password, first_name, last_name, email):
        return self.service.add_user(username, password, first_name, last_name, email)

    def del_user(self, username):
        return self.service.del_user(username)
