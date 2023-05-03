import imp
import random
import tkinter as tk
from PIL import ImageTk, Image
import io
import random


class PotWidget(tk.Frame):  # tk.Frame
    def remove_from_pot(self, load_planted_plants, load_plants):
        self.my_plant_service.handle_user_plant(self.values["_id"], False)
        self.destroy()
        load_planted_plants()
        load_plants()

    def __init__(
        self, parent, plant, my_plant_service, load_planted_plants, load_plants
    ):
        super().__init__(parent, borderwidth=2, relief="groove")
        self.values = plant
        self.my_plant_service = my_plant_service
        self.load_planted_plants = load_planted_plants
        self.load_plants = load_plants

        def sync_data():
            # LIGHT SENSOR READINGS
            num_values = 5
            light_values = [random.randint(0, 100) for i in range(num_values)]
            # Grade the values based on the provided categories
            light_grades = []
            for value in light_values:
                if value < 20:
                    light_grades.append("Low light intensity")
                elif value < 50:
                    light_grades.append("Moderate light intensity")
                elif value < 80:
                    light_grades.append("High light intensity")
                else:
                    light_grades.append("Very high light intensity")

            sync_value_index = random.randint(0, num_values - 1)
            sync_value_light = light_values[sync_value_index]
            sync_value_grade_light = light_grades[sync_value_index]

            ## SOIL HUMIDITY
            # Define the soil humidity ranges in cb (centibars)
            ranges = [
                {"label": "Over saturated soil", "min": 0, "max": 9},
                {"label": "Adequately moist", "min": 10, "max": 29},
                {"label": "Moderately dry, may require watering", "min": 30, "max": 60},
                {
                    "label": "Very dry, in need of immediate watering",
                    "min": 61,
                    "max": 99,
                },
            ]

            # Define the number of values to generate
            num_values = 5

            # Generate random soil humidity values within the specified ranges
            humidity_values = []
            for i in range(num_values):
                # Choose a random range and generate a value within that range
                range_idx = random.randrange(len(ranges))
                min_val = ranges[range_idx]["min"]
                max_val = ranges[range_idx]["max"]
                humidity_val = random.uniform(min_val, max_val)
                humidity_values.append(humidity_val)

            # Choose a random humidity value and get its grade
            sync_humidity_values_index = random.randint(0, num_values - 1)
            sync_humidity_values = humidity_values[sync_humidity_values_index]
            label = ""
            for r in ranges:
                if r["min"] <= sync_humidity_values <= r["max"]:
                    label = r["label"]
                    break
            sync_humidity_values_grade = label

            ## PH & SALINITY
            pH_range = (4.5, 8.5)
            salinity_range = (0.1, 1.0)

            num_values = 5

            pH_values = [
                random.uniform(pH_range[0], pH_range[1]) for i in range(num_values)
            ]
            salinity_values = [
                random.uniform(salinity_range[0], salinity_range[1])
                for i in range(num_values)
            ]
            salinity_grades = []

            for salinity in salinity_values:
                if salinity >= 0 and salinity <= 0.1:
                    salinity_grades.append("Freshwater")
                elif salinity > 0.1 and salinity <= 0.5:
                    salinity_grades.append("Slightly brackish water")
                elif salinity > 0.5 and salinity <= 5:
                    salinity_grades.append("Brackish water")
                elif salinity > 5 and salinity <= 15:
                    salinity_grades.append("Moderately saline water")
                elif salinity > 15 and salinity <= 30:
                    salinity_grades.append("Saline water")
                elif salinity > 30:
                    salinity_grades.append("Hyper-saline water")

            sync_value_index = random.randint(0, num_values - 1)
            sync_value_salinity = salinity_values[sync_value_index]
            sync_value_salinity_grade = salinity_grades[sync_value_index]

            # Grade the pH values based on the provided categories
            pH_grades = []
            for value in pH_values:
                if value < 5.5:
                    pH_grades.append("Too acidic")
                elif value < 6.5:
                    pH_grades.append("Neutral, ideal for most plants")
                elif value < 7.5:
                    pH_grades.append("Slightly alkaline, acceptable for most plants")
                else:
                    pH_grades.append("Too alkaline for most plants")

            sync_value_index = random.randint(0, num_values - 1)
            sync_value_ph = pH_values[sync_value_index]
            sync_value_ph_grade = pH_grades[sync_value_index]

            # Update labels with new data
            moisture_label["text"] = "Moisture Sensor: \t{} \t{}".format(
                round(sync_humidity_values, 2), sync_humidity_values_grade
            )
            ph_label["text"] = "pH: \t\t{} \t{}".format(
                round(sync_value_ph, 2), sync_value_ph_grade
            )
            salinity_label["text"] = "Salinity: \t\t{}\t{}".format(
                round(sync_value_salinity, 2), sync_value_salinity_grade
            )
            light_label["text"] = "Light Sensor: \t{} \t{}".format(
                sync_value_light, sync_value_grade_light
            )

            temp_label["text"] = "Temperature: \t{:.1f} \t°C".format(temp_data())
            return {
                "light": {"value": sync_value_light, "grade": sync_value_grade_light},
                "humidity": {
                    "value": sync_humidity_values,
                    "grade": sync_humidity_values_grade,
                },
                "ph": {"value": sync_value_ph, "grade": sync_value_ph_grade},
                "salinity": {
                    "value": sync_value_salinity,
                    "grade": sync_value_salinity_grade,
                },
                "chart_light_values_list": {"value": light_values},
            }

        # self.grid_columnconfigure(0, weight=1)
        image_data = self.values.get("image_data")
        if image_data is not None:
            # convert image data to PIL Image object
            image = Image.open(io.BytesIO(image_data))

            # create PhotoImage from PIL Image object
            self.image_photo = ImageTk.PhotoImage(image.resize((150, 170)))

            # create label with image
            image_label = tk.Label(self, image=self.image_photo, height=170, width=150)
            image_label.grid(row=0, column=2, padx=5, pady=5, sticky="nw", rowspan=3)

        name = tk.Label(
            self, justify="left", text="Name: \t\t{}".format(self.values["name"])
        )
        type_label = tk.Label(
            self, justify="left", text="Type: \t\t{}".format(self.values["type"])
        )
        watering_label = tk.Label(
            self, justify="left", text="Watering: \t{}".format(self.values["watering"])
        )

        self.remove_from_pot_button = tk.Button(
            self,
            text="Remove from pot",
            command=lambda: self.remove_from_pot(self.load_planted_plants, load_plants),
            width=20,
            padx=5,
            pady=5,
        )

        # planted_pot_label sensor data
        # sensor_monitor_frame gui
        sensor_monitor_frame = tk.LabelFrame(self, text="Sensors Data")
        self.sync_button = tk.Button(
            sensor_monitor_frame,
            text="Sync",
            command=sync_data,
        )
        moisture_label = tk.Label(
            sensor_monitor_frame, text="Moisture: N/A", justify="left"
        )
        ph_label = tk.Label(sensor_monitor_frame, text="pH: N/A", justify="left")
        salinity_label = tk.Label(
            sensor_monitor_frame, text="Salinity: N/A", justify="left"
        )
        light_label = tk.Label(sensor_monitor_frame, text="Light: N/A", justify="left")
        temp_label = tk.Label(
            sensor_monitor_frame, text="Temperature: N/A", justify="left"
        )

        name.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        type_label.grid(row=1, column=0, padx=10, pady=10, sticky="nw")
        watering_label.grid(row=2, column=0, padx=10, pady=10, sticky="nw")
        self.remove_from_pot_button.grid(
            row=4, column=0, columnspan=3, padx=5, pady=5, sticky="ew"
        )

        sensor_monitor_frame.grid(
            row=0, column=1, rowspan=3, padx=10, pady=10, sticky="nsew"
        )
        sensor_monitor_frame.columnconfigure(0, weight=1, minsize=512)
        moisture_label.grid(column=0, row=0, sticky="w", padx=10)
        ph_label.grid(column=0, row=1, sticky="w", padx=10)
        salinity_label.grid(column=0, row=2, sticky="w", padx=10)
        light_label.grid(column=0, row=3, sticky="w", padx=10)
        temp_label.grid(column=0, row=4, sticky="w", padx=10)
        self.sync_button.grid(column=0, row=5, padx=10, pady=10, sticky="ew")

        if image_data is not None:
            image_label.grid(row=0, column=2, padx=5, pady=5, sticky="nsew", rowspan=4)

        """
        # retrieve image data from MongoDB
        image_data = self.values.get("image_data")
        if image_data is not None:
            # convert image data to PIL Image object
            image = Image.open(io.BytesIO(image_data))

            # create PhotoImage from PIL Image object
            self.image_photo = ImageTk.PhotoImage(image.resize((150, 170)))

            # create label with image
            image_label = tk.Label(self, image=self.image_photo, height=170, width=150)
            image_label.grid(row=0, column=2, padx=5, pady=5, sticky="nw", rowspan=3)

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
            command=lambda: self.remove_from_pot(self.load_planted_plants, load_plants),
            width=20,
            padx=5,
            pady=5,
        )

        # planted_pot_label sensor data

        # sensor_monitor_frame gui
        sensor_monitor_frame = tk.LabelFrame(self, text="Sensors Data")
        self.sync_button = tk.Button(
            self,
            text="Sync",
            # command=sync_data,
        )
        moisture_label = tk.Label(
            self,
            text="Moisture: N/A",
            justify="left",
        )
        ph_label = tk.Label(
            self,
            text="pH: N/A",
            justify="left",
        )
        salinity_label = tk.Label(
            self,
            text="Salinity: N/A",
            justify="left",
        )
        light_label = tk.Label(
            self,
            text="Light: N/A",
            justify="left",
        )
        temp_label = tk.Label(
            self,
            text="Temperature: N/A",
            justify="left",
        )

        name.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        type.grid(row=1, column=0, padx=10, pady=10, sticky="nw")
        watering.grid(row=2, column=0, padx=10, pady=10, sticky="nw")
        self.remove_from_pot_button.grid(row=3, column=2, padx=5, pady=5, sticky="nw")

        sensor_monitor_frame.grid(row=0, column=1,rowspan=4, padx=10, pady=10, sticky="nw")
        sensor_monitor_frame.columnconfigure(1, weight=1, minsize=410)
        self.sync_button.grid(column=0, row=5, padx=10, pady=10, sticky="ew")
        moisture_label.grid(column=0, row=0, sticky="w", padx=10)
        ph_label.grid(column=0, row=1, sticky="w", padx=10)
        salinity_label.grid(column=0, row=2, sticky="w", padx=10)
        light_label.grid(column=0, row=3, sticky="w", padx=10)
        temp_label.grid(column=0, row=4, sticky="w", padx=10)
        """
