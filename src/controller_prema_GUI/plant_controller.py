from service_prema_db.plant_service import PlantService

# dodati import paketa za view (tkinter)
# pozivati iskljucivo kontroller iz tkintera (view, u ovom slucaj plantView)
# na isti nacin napraviti potController


class PlantController:
    # Constructor prima 3 parama, svaki je tipa String https://www.geeksforgeeks.org/constructors-in-python/
    # kasnije kad napravimo plantView dodat plantView u konstruktor
    def __init__(self, connection_uri, database_name, collection_name_plants):
        self.service = PlantService(
            connection_uri, database_name, collection_name_plants
        )

    def get_all_plants(self):
        return self.service.get_all_plants()

    def get_plant_by_id(self, plant_id):
        return self.service.get_plant_by_id(plant_id)

    def get_plant_by_name(self, plant_name):
        return self.service.get_plant_by_name(plant_name)

    def delete_plant_by_id(self, plant_id):
        return self.service.delete_plant_by_id(plant_id)

    def update_plant_notes(self, id, notes):
        return self.service.update_plant_notes(id, notes)
