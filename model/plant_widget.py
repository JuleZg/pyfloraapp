import tkinter as tk


class PlantWidget(tk.Canvas):  # tk.Frame
    def delete_widget_and_data(self):
        self.my_plant_service.delete_user_plant(self.values["_id"])
        self.destroy()

    def __init__(self, parent, plant, my_plant_service):
        super().__init__(parent, borderwidth=1, relief="solid")
        self.values = plant
        self.my_plant_service = my_plant_service

        name = tk.Label(
            self,
            justify="left",
            text="Name: \t\t{}".format(self.values["name"]),
        )
        print(name["text"])
        type = tk.Label(
            self,
            justify="left",
            text="Type: \t\t{}".format(self.values["type"]),
        )
        watering = tk.Label(
            self,
            justify="left",
            text="Watering: \t{}".format(self.values["watering"]),
        )
        description = tk.Label(
            self,
            justify="left",
            text="Description: \t{}".format(self.values["desc"]),
            # wraplength=700,
        )

        self.delete_button = tk.Button(
            self,
            text="Delete",
            command=lambda: self.delete_widget_and_data(),
        )

        name.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        type.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        watering.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        description.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.delete_button.grid(row=3, column=1)
