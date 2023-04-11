import tkinter as tk
import datetime
from tkinter import ttk
import random


def user_view():
    FONT = ("Roboto Mono", 12)

    def update_time():
        now = datetime.datetime.now()
        date_time_label.config(text=now.strftime("%d.%m.%Y %H:%M:%S"))
        window.after(1000, update_time)

    window = tk.Tk()
    window.geometry("1920x1000")

    # get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate the x and y coordinates to center the window
    x = (screen_width // 2) - (1920 // 2)
    y = (screen_height // 2) - (1080 // 2)
    window.geometry(f"+{x}+{y}")

    # header frame
    header_frame = tk.Frame(window)
    header_frame.pack(fill="x")

    header_frame = tk.Frame(header_frame, bg="blue", height=60)
    header_frame.pack(fill="x")

    # header date, time, temperature
    date_time_label = tk.Label(header_frame, bg="green", font=FONT)
    date_time_label.pack(side="left", padx=20)

    # header app name
    app_title_label = tk.Label(
        header_frame, text="PyFlora - User View", bg="yellow", font=FONT
    )
    app_title_label.place(relx=0.5, rely=0.5, anchor="center")

    # header logout button
    log_out_btn = tk.Button(
        header_frame,
        text="Log Out",
        bg="red",
        font=FONT,
        command=window.destroy,
        relief="raised",
    )
    log_out_btn.pack(side="right", padx=20)

    # sensor_chart_frame
    sensor_chart_frame = tk.Frame(window)
    sensor_chart_frame.pack()

    # create a sub-frame within the sensor_chart_frame to hold the sensor_monitor_app content
    sensor_monitor_frame = tk.Frame(sensor_chart_frame)
    sensor_monitor_frame.pack(side="left")

    # sensor gui
    def sync_data():
        # LIGHT SENSOR READINGS

        # Define the number of values to generate
        num_values = 5

        # Generate random light sensor values within the range of 0-100
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
        sync_value = light_values[sync_value_index]
        sync_value_grade = light_grades[sync_value_index]

        ## SOIL HUMIDITY
        # Define the soil humidity ranges in cb (centibars)
        ranges = [
            {"label": "Over saturated soil", "min": 0, "max": 9},
            {"label": "Adequately moist", "min": 10, "max": 29},
            {"label": "Moderately dry, may require watering", "min": 30, "max": 60},
            {"label": "Very dry, in need of immediate watering", "min": 61, "max": 99},
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
        # Define the range of pH and salinity values
        pH_range = (4.5, 8.5)
        salinity_range = (0.1, 1.0)

        # Define the number of values to generate
        num_values = 5

        # Generate random pH and salinity values within the specified range
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

        # Code to sync sensor data from the pots
        # Code to sync temperature data from the weather station

        # Update labels with new data
        moisture_label["text"] = "Moisture Sensor: \t{} \tRange: {}".format(
            round(sync_humidity_values, 2), sync_humidity_values_grade
        )
        ph_label["text"] = "pH: \t\t{} \tGrade: {}".format(
            round(sync_value_ph, 2), sync_value_ph_grade
        )
        salinity_label["text"] = "Salinity: \t\t{}\tGrade: {}".format(
            round(sync_value_salinity, 2), sync_value_salinity_grade
        )
        light_label["text"] = "Light Sensor: \t{} \tGrade: {}".format(
            sync_value, sync_value_grade
        )

        temp_label["text"] = "Temperature: {}".format(temp_data)

    sensors_frame = ttk.LabelFrame(sensor_monitor_frame, text="Sensors Data")
    sensors_frame.grid(column=0, row=0, padx=10, pady=10)

    sync_button = ttk.Button(sensor_monitor_frame, text="Sync", command=sync_data)
    sync_button.grid(column=1, row=0, padx=10, pady=10)

    moisture_label = ttk.Label(sensors_frame, text="Moisture: N/A", justify="left")
    moisture_label.grid(column=0, row=0, sticky="w")

    ph_label = ttk.Label(sensors_frame, text="pH: N/A", justify="left")
    ph_label.grid(column=0, row=1, sticky="w")

    salinity_label = ttk.Label(sensors_frame, text="Salinity: N/A", justify="left")
    salinity_label.grid(column=0, row=2, sticky="w")

    light_label = ttk.Label(sensors_frame, text="Light: N/A", justify="left")
    light_label.grid(column=0, row=3, sticky="w")

    temp_label = ttk.Label(sensors_frame, text="Temperature: N/A", justify="left")
    temp_label.grid(column=0, row=4, sticky="w")

    update_time()  # start updating the time label
    window.mainloop()


user_view()
