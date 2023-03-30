from bson import ObjectId
from service_prema_db.pot_service import PotService


class PotController:
    def __init__(self, connection_uri, database_name, collection_name_pots):
        self.service = PotService(connection_uri, database_name, collection_name_pots)

    # get_all_pots
    def get_all_pots(self):
        return self.service.get_all_pots()

    # get_pot_by_id
    def get_pot_by_id(self, pot_id):
        return self.service.get_pot_by_id(pot_id)

    # get_pot_by_name
    def get_pot_by_name(self, pot_name):
        return self.service.get_pot_by_name(pot_name)

    #  delete_pot_by_id
    def delete_pot_by_id(self, pot_id):
        return self.service.delete_pot_by_id(pot_id)
