from service.plant_service import PlantService

# dodati import paketa za view (tkinter)
# pozivati iskljucivo kontroller iz tkintera (view, u ovom slucaj plantView)
# na isti nacin napraviti potController


class PlantController:
    # Constructor prima 3 parama, svaki je tipa String https://www.geeksforgeeks.org/constructors-in-python/
    # kasnije kad napravimo plantView dodat plantView u konstruktor
    def __init__(self, plant_service: PlantService):
        self.service = plant_service

    def get_all_plants(self):
        plants = self.service.get_all_plants()
        return plants

    def get_plant_by_id(self, plant_id):
        plant_dict = self.service.get_plant_by_id(plant_id)
        return plant_dict

    def delete_plant_by_id(self, plant_id):
        # vidjet sta delete vraca
        return self.service.delete_plant_by_id(plant_id)

    def update_plant_notes(self, notes):
        # vidjet sta vraca update
        return self.service.update_plant_notes(notes)
