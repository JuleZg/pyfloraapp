from bson import ObjectId
from service.pot_service import PotService


class PotController:
    def __init__(self, pot_service: PotService):
        self.service = pot_service

    def get_all_pots(self):
        pots = self.service.get_all_pots()
        return pots

    def get_pot_by_id(self, pot_id):
        id_obj = ObjectId(pot_id)
        pot_dict = self.service.get_pot_by_id({"_id": pot_id})
        print(f"NASLI POT  {pot_dict['name']}")
        return pot_dict

    def delete_pot_by_id(self, pot_id):
        return self.service.delete_pot_by_id(pot_id)

    def update_pot_size(self, size):
        return self.service.update_pot_size(size)
