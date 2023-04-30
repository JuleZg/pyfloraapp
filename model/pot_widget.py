import tkinter as tk
from PIL import ImageTk, Image
import io


class PotWidget(tk.Frame):  # tk.Frame
    def remove_from_pot(self):
        self.my_plant_service.handle_user_plant(self.values["_id"], False)
        self.destroy()

    def __init__(self, parent, plant, my_plant_service):
        super().__init__(parent, borderwidth=2, relief="groove")
        self.values = plant
        self.my_plant_service = my_plant_service
        self.grid_columnconfigure(0, weight=1)

        # retrieve image data from MongoDB
        image_data = self.values.get("image_data")
        if image_data is not None:
            # convert image data to PIL Image object
            image = Image.open(io.BytesIO(image_data))

            # create PhotoImage from PIL Image object
            self.image_photo = ImageTk.PhotoImage(image.resize((150, 170)))

            # create label with image
            image_label = tk.Label(self, image=self.image_photo, height=170, width=150)
            image_label.grid(row=0, column=1, padx=5, pady=5, sticky="nw", rowspan=3)

        name = tk.Label(
            self, justify="left", text="Name: \t\t{}".format(self.values["name"])
        )
        type = tk.Label(
            self, justify="left", text="Type: \t\t{}".format(self.values["type"])
        )
        watering = tk.Label(
            self, justify="left", text="Watering: \t{}".format(self.values["watering"])
        )

        self.remove_from_pot_button = tk.Button(
            self,
            text="Remove from pot",
            command=lambda: self.handle_user_plant(self.values["_id"], False),
            width=20,
            padx=5,
            pady=5,
        )

        name.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        type.grid(row=1, column=0, padx=10, pady=10, sticky="nw")
        watering.grid(row=2, column=0, padx=10, pady=10, sticky="nw")
        self.remove_from_pot_button.grid(row=3, column=1, padx=5, pady=5, sticky="nw")
