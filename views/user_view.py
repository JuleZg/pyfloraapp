import tkinter as tk
import random
from tkinter import font
from tkinter.messagebox import askokcancel
import requests
import datetime
from PIL import ImageTk, Image


def user_view():
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
        }

    def on_closing():
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.destroy()

    def temp_data():
        MY_LAT = 45.790152  # Your latitude
        MY_LONG = 16.005303  # Your longitude
        MY_API = "b8fe2d48edaec121636871ffc793be7e"

        # Construct the API request URL
        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={MY_LAT}&lon={MY_LONG}&appid={MY_API}&units=metric"

        # Send the API request and get the response
        response = requests.get(api_url)
        response_data = response.json()

        # Extract the temperature from the response data for the current hour
        temperature = response_data["main"]["temp"]

        return temperature

    def update_time():
        now = datetime.datetime.now()
        date_time_label.config(
            text=now.strftime("%d.%m.%Y %H:%M:%S")
            + "\n\n Temperature: {:.1f}°C".format(temp_data())
        )
        window.after(1000, update_time)

    window = tk.Tk()
    window.geometry("1920x1000")
    window.configure(bg="red")
    window.attributes("-fullscreen", True)


    window.protocol("WM_DELETE_WINDOW", on_closing)
    FONT = ("Roboto Mono", 12)

    # get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate the x and y coordinates to center the window
    x = (screen_width // 2) - (1920 // 2)
    y = (screen_height // 2) - (1080 // 2)
    window.geometry(f"+{x}+{y}")

    # header frame
    header_frame = tk.LabelFrame(
        window, height=60, labelanchor="s", borderwidth=2, relief="groove"
    )
    header_frame.pack(fill="x")

    # header date, time, temperature
    date_time_label = tk.Label(header_frame)
    date_time_label.pack(side="left", padx=20, pady=10)
    # header app name
    app_title_label = tk.Label(
        header_frame, text="PyFlora - User View", font=FONT, padx=20, pady=10
    )
    app_title_label.place(relx=0.5, rely=0.5, anchor="center")

    # header logout button
    log_out_btn = tk.Button(
        header_frame,
        text="Log Out",
        font=FONT,
        command=on_closing,
        relief="raised",
    )
    log_out_btn.pack(side="right", padx=20, pady=10)

    # sensor_chart_frame
    sensor_chart_frame = tk.Frame(window)
    sensor_chart_frame.pack(fill="x")

    # sensor gui
    sensor_monitor_frame = tk.LabelFrame(sensor_chart_frame, text="Sensors Data")
    sensor_monitor_frame.pack(side="left", padx=10)
    sensor_monitor_frame.columnconfigure(0, weight=1, minsize=410)

    sync_button = tk.Button(sensor_monitor_frame, text="Sync", command=sync_data)
    sync_button.grid(column=0, row=5, padx=10, pady=10, sticky="ew")

    moisture_label = tk.Label(
        sensor_monitor_frame, text="Moisture: N/A", justify="left"
    )
    moisture_label.grid(column=0, row=0, sticky="w", padx=10)

    ph_label = tk.Label(sensor_monitor_frame, text="pH: N/A", justify="left")
    ph_label.grid(column=0, row=1, sticky="w", padx=10)

    salinity_label = tk.Label(
        sensor_monitor_frame, text="Salinity: N/A", justify="left"
    )
    salinity_label.grid(column=0, row=2, sticky="w", padx=10)

    light_label = tk.Label(sensor_monitor_frame, text="Light: N/A", justify="left")
    light_label.grid(column=0, row=3, sticky="w", padx=10)

    temp_label = tk.Label(sensor_monitor_frame, text="Temperature: N/A", justify="left")
    temp_label.grid(column=0, row=4, sticky="w", padx=10)

    # CHART FRAME
    chart_frame = tk.Frame(sensor_chart_frame)
    chart_frame.pack(fill="both", expand=True)
    chart_frame.propagate = False
    chart_frame.rowconfigure(0, minsize=300)
    # Configure the grid to fill the available space
    chart_frame.columnconfigure(0, weight=1)
    chart_frame.columnconfigure(1, weight=1)
    chart_frame.columnconfigure(2, weight=1)
    chart_frame.rowconfigure(0, weight=1)

    chart_label1 = tk.Label(chart_frame, text="chart1")
    chart_label1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    chart_label1.config(anchor="center")

    chart_label2 = tk.Label(chart_frame, text="chart 2")
    chart_label2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    chart_label2.config(anchor="center")

    chart_label3 = tk.Label(chart_frame, text="chart 3")
    chart_label3.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
    chart_label3.config(anchor="center")

    # plant_pot_list_frame
    plant_pot_list_frame = tk.LabelFrame(window, padx=10, pady=10)
    plant_list_label_frame = tk.LabelFrame(
        plant_pot_list_frame,
        text="PLANT LIST",
        borderwidth=2,
        relief="groove",
        labelanchor="n",
        padx=5,
        pady=5,
        width=948,
        height=620,
    )
    add_new_plant_btn = tk.Button(
        plant_list_label_frame, text="Add New Plant", padx=5, pady=5
    )

    # plant_list plant frame
    plant_label = tk.Label(plant_list_label_frame, borderwidth=2, relief="groove")
    plant_name = tk.Label(plant_label, text="Name: \t\tRose", justify="left")
    plant_type = tk.Label(plant_label, text="Type: \t\tFlower", justify="left")
    plant_watering = tk.Label(
        plant_label, text="Watering: \tTwice a week", justify="left"
    )
    plant_desc = tk.Label(plant_label, text="Description: \tA", justify="left")
    image = Image.open("plant_img/rose.png")
    photo = ImageTk.PhotoImage(image.resize((150, 170)))
    plant_img = tk.Label(plant_label, image=photo, height=170, width=150)
    del_my_plant_btn = tk.Button(
        plant_label, text="Delete My Plant", padx=5, pady=5, width=20
    )
    # positioning
    plant_name.grid(row=1, column=0, sticky="w")
    plant_type.grid(row=2, column=0, sticky="w")
    plant_watering.grid(row=3, column=0, sticky="w")
    plant_desc.grid(row=4, column=0, sticky="w")
    plant_img.grid(row=1, column=1, sticky="e", rowspan=3)
    del_my_plant_btn.grid(row=4, column=1)

    # pot list
    pot_list_label_frame = tk.LabelFrame(
        plant_pot_list_frame,
        text="POT LIST",
        borderwidth=2,
        relief="groove",
        labelanchor="n",
        padx=5,
        pady=5,
        width=50,
    )
    add_plant_to_pot = tk.Button(
        pot_list_label_frame, text="Add Plant to Pot", padx=5, pady=5
    )
    planted_pot_label = tk.Label(
        pot_list_label_frame, borderwidth=2, relief="groove", width=50
    )
    del_planted_pot_btn = tk.Button(
        planted_pot_label, text="Delete from Pot", padx=5, pady=5, width=20
    )

    planted_image = Image.open("planted_pots_img/rose_planted.png")
    planted_photo = ImageTk.PhotoImage(planted_image.resize((150, 170)))
    planted_img = tk.Label(
        planted_pot_label, image=planted_photo, height=170, width=150
    )

    light_sens = tk.Label(planted_pot_label, text="N/A", justify="left")
    humidity_sens = tk.Label(planted_pot_label, text="N/A", justify="left")
    ph_sens = tk.Label(planted_pot_label, text="N/A", justify="left")
    salintiy_sens = tk.Label(planted_pot_label, text="N/A", justify="left")

    sensor_data = sync_data()
    light_sens["text"] = "Light Sensor: \t{}".format(
        round(sensor_data["light"]["value"], 2)
    )
    humidity_sens["text"] = "Humidity Sensor: \t{}".format(
        round(sensor_data["humidity"]["value"], 2)
    )
    ph_sens["text"] = "pH Sensor: \t{}".format(round(sensor_data["ph"]["value"], 2))
    salintiy_sens["text"] = "Salinity Sensor: \t{}".format(
        round(sensor_data["salinity"]["value"], 2)
    )

    # planted_pot_label positioning
    planted_img.grid(row=0, column=0, sticky="w", rowspan=3)
    light_sens.grid(row=0, column=1, sticky="w")
    humidity_sens.grid(row=1, column=1, sticky="w")
    ph_sens.grid(row=2, column=1, sticky="w")
    salintiy_sens.grid(row=3, column=1, sticky="w")

    planted_pot_label.columnconfigure(0, weight=1, uniform="col")
    planted_pot_label.columnconfigure(1, weight=1, uniform="col")
    planted_pot_label.columnconfigure(2, weight=1, uniform="col")

    planted_img.columnconfigure(0, weight=1, uniform="col")
    light_sens.columnconfigure(1, weight=1, uniform="col")
    humidity_sens.columnconfigure(2, weight=1, uniform="col")
    salintiy_sens.columnconfigure(3, weight=1, uniform="col")

    # positionong
    plant_pot_list_frame.pack(fill="both", expand=True)
    plant_pot_list_frame.columnconfigure(0, weight=1, uniform="col")
    plant_pot_list_frame.columnconfigure(1, weight=1, uniform="col")
    plant_pot_list_frame.rowconfigure(0, weight=1)

    add_new_plant_btn.grid(row=0, column=0, sticky="w")
    plant_list_label_frame.grid(row=0, column=0, sticky="nsew")
    plant_list_label_frame.propagate(False)
    plant_list_label_frame.columnconfigure(0, weight=1)
    plant_label.grid(row=1, column=0, pady=10, sticky="nsew")
    plant_label.columnconfigure(0, weight=1)

    pot_list_label_frame.grid(row=0, column=1, sticky="nsew")
    pot_list_label_frame.columnconfigure(1, weight=1)
    add_plant_to_pot.grid(row=0, column=0)
    planted_pot_label.grid(row=1, column=0, pady=10, columnspan=2, sticky="nsew")
    del_planted_pot_btn.grid(row=3, column=0, sticky="w")
    planted_pot_label.columnconfigure(0, weight=1)

    pot_list_label_frame.update()
    print(plant_list_label_frame.winfo_width(), plant_list_label_frame.winfo_height())
    print(pot_list_label_frame.winfo_width(), pot_list_label_frame.winfo_height())

    update_time()  # start updating the time label

    window.mainloop()


user_view()
