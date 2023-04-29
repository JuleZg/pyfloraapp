import tkinter as tk
from PIL import ImageTk, Image
import io

class PlantWidget(tk.Frame):  # tk.Frame
    def delete_widget_and_data(self):
        self.my_plant_service.delete_user_plant(self.values["_id"])
        self.destroy()

    def __init__(self, parent, plant, my_plant_service):
        super().__init__(parent, borderwidth=2, relief="groove")
        self.values = plant
        self.my_plant_service = my_plant_service
        self.grid_columnconfigure(0, weight=1)

        """planted_image = Image.open("planted_pots_img/rose_planted.png")
        self.planted_photo = ImageTk.PhotoImage(planted_image.resize((150, 170)))
        planted_img = tk.Label(self, image=self.planted_photo, height=170, width=150)"""

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
        description = tk.Label(
            self,
            justify="left",
            text="Description: \t{}".format(self.values["desc"]),
            wraplength=720,
        )

        self.delete_button = tk.Button(
            self,
            text="Delete",
            command=lambda: self.delete_widget_and_data(),
            width=20,
            padx=5,
            pady=5,
        )

        name.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        type.grid(row=1, column=0, padx=10, pady=10, sticky="nw")
        watering.grid(row=2, column=0, padx=10, pady=10, sticky="nw")
        description.grid(row=3, column=0, padx=10, pady=10, sticky="nw")
        self.delete_button.grid(row=3, column=1, padx=5, pady=5, sticky="nw")
        #planted_img.grid(row=0, column=1, padx=5, pady=5, sticky="nw", rowspan=3)
