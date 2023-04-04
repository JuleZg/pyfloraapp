import tkinter as tk
from tkinter import ttk
import requests


class PlantMonitorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Plant Monitor")

        self.sensors_frame = ttk.LabelFrame(self.root, text="Sensors Data")
        self.sensors_frame.grid(column=0, row=0, padx=10, pady=10)

        self.sync_button = ttk.Button(self.root, text="Sync", command=self.sync_data)
        self.sync_button.grid(column=1, row=0, padx=10, pady=10)

        self.moisture_label = ttk.Label(self.sensors_frame, text="Moisture: N/A")
        self.moisture_label.grid(column=0, row=0)

        self.ph_label = ttk.Label(self.sensors_frame, text="pH: N/A")
        self.ph_label.grid(column=0, row=1)

        self.salinity_label = ttk.Label(self.sensors_frame, text="Salinity: N/A")
        self.salinity_label.grid(column=0, row=2)

        self.light_label = ttk.Label(self.sensors_frame, text="Light: N/A")
        self.light_label.grid(column=0, row=3)

        self.temp_label = ttk.Label(self.sensors_frame, text="Temperature: N/A")
        self.temp_label.grid(column=0, row=4)

    def sync_data(self):
        # Code to sync sensor data from the pots
        # Code to sync temperature data from the weather station

        # Update labels with new data
        self.moisture_label["text"] = "Moisture: {}".format(moisture_data)
        self.ph_label["text"] = "pH: {}".format(ph_data)
        self.salinity_label["text"] = "Salinity: {}".format(salinity_data)
        self.light_label["text"] = "Light: {}".format(light_data)
        self.temp_label["text"] = "Temperature: {}".format(temp_data)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = PlantMonitorApp()
    app.run()
