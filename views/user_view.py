import tkinter as tk
from tkinter import ttk
import random
import requests
import datetime
from matplotlib.figure import Figure
from model.plant_widget import PlantWidget
from model.pot_widget import PotWidget
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def user_view(my_plant_service, current_user, current_user_id):
    def sync_data():
        # LIGHT SENSOR READINGS
        num_values = 7
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

        num_values = 7

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
        print("SYNC HUMIDITIY VALUES 0", sync_humidity_values)
        label = ""
        for r in ranges:
            if r["min"] <= sync_humidity_values <= r["max"]:
                label = r["label"]
                break
        sync_humidity_values_grade = label
        print("HUMIDITIY VALUES 1 :", humidity_values)
        ## PH & SALINITY
        pH_range = (4.5, 8.5)
        salinity_range = (0.1, 1.0)

        num_values = 7

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
            "light": {
                "value": sync_value_light,
                "grade": sync_value_grade_light,
            },
            "humidity": {
                "value": sync_humidity_values,
                "grade": sync_humidity_values_grade,
            },
            "ph": {
                "value": sync_value_ph,
                "grade": sync_value_ph_grade,
            },
            "salinity": {
                "value": sync_value_salinity,
                "grade": sync_value_salinity_grade,
            },
            "chart_light_values_list": {
                "value": light_values,
            },
            "chart_humidity_values_list": {
                "value": humidity_values,
            },
        }

    def on_closing():
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            # window.destroy()
            sys.exit(0)

    def temp_data():
        MY_LAT = 45.790152
        MY_LONG = 16.005303
        MY_API = "b8fe2d48edaec121636871ffc793be7e"

        # Construct the API request URL
        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={MY_LAT}&lon={MY_LONG}&appid={MY_API}&units=metric"

        # Send the API request and get the response
        response = requests.get(api_url)
        response_data = response.json()

        # temperature from the response data for the current hour
        temperature = response_data["main"]["temp"]

        return temperature

    def update_time():
        now = datetime.datetime.now()
        date_time_label.config(
            text=now.strftime("%d.%m.%Y %H:%M:%S")
            + "\n\n Temperature: {:.1f}°C".format(temp_data())
        )
        window.after(1000, update_time)

    def load_plants():
        for widget in plant_frame.winfo_children():
            widget.destroy()
        user_plants = my_plant_service.get_user_plants(current_user_id, False)

        for plant in user_plants:
            plant_widget = PlantWidget(
                plant_frame,
                plant,
                my_plant_service,
                load_planted_plants,
                update_pie_chart,
            )

            # add the PlantWidget to the GUI
            plant_widget.pack(
                side="top", padx=2, pady=2, fill="both", expand=True, anchor="nw"
            )

    def load_planted_plants():
        for widget in pot_frame.winfo_children():
            widget.destroy()
        user_plants = my_plant_service.get_user_plants(current_user_id, True)

        for plant in user_plants:
            pot_widget = PotWidget(
                pot_frame,
                plant,
                my_plant_service,
                load_planted_plants,
                load_plants,
                update_pie_chart,
            )

            pot_widget.pack(
                side="top", padx=2, pady=2, fill="both", expand=True, anchor="nw"
            )

    def add_new_plant():
        window = tk.Tk()
        window.geometry("1700x600")

        def add_plant():
            item = plants_table.selection()[0]
            values = plants_table.item(item, "values")
            plant_id = values[0]
            my_plant_service.save_plant_for_user(current_user_id, plant_id)
            load_plants()
            update_pie_chart()
            return None

        plants = my_plant_service.find_all_plants()
        plants_table_frame = tk.Frame(window)
        plants_table_frame.pack(side="bottom", fill="both", expand=True)
        add_plant_button = tk.Button(
            plants_table_frame, text="Add Plant", command=add_plant, width=15
        )
        add_plant_button.pack(side="top", padx=10, pady=10)

        def close_add_new_plant():
            window.destroy()

        close_button = tk.Button(
            plants_table_frame, text="Close", command=close_add_new_plant, width=15
        )
        close_button.pack(side="top", anchor="n", padx=10, pady=10)
        plants_table = ttk.Treeview(
            plants_table_frame,
            columns=("_id", "name", "type", "watering", "description"),
            show="headings",
        )
        plants_table.heading("_id", text="plant id")
        plants_table.column("_id", anchor="w")
        plants_table.heading("name", text="Name")
        plants_table.column("name", anchor="w")
        plants_table.heading("type", text="Type")
        plants_table.column("type", anchor="w")
        plants_table.heading("watering", text="Watering")
        plants_table.column("watering", anchor="w")
        plants_table.heading("description", text="Description")
        plants_table.column("description", anchor="w", minwidth=0, width=1000)
        plants_table.pack(side="top", fill="y", expand=True)

        for plant in plants:
            plants_table.insert(
                "",
                "end",
                values=(
                    plant["_id"],
                    plant["name"],
                    plant["type"],
                    plant["watering"],
                    plant["desc"],
                ),
            )

        window.mainloop()

    def update_pie_chart():
        user_plants = my_plant_service.get_user_plants(current_user_id, False)
        user_planted_plants = my_plant_service.get_user_plants(current_user_id, True)

        total_plants = len(user_plants) + len(user_planted_plants)

        if total_plants == 0:
            # Hide or remove the pie chart
            ax3.clear()
            canvas_pie_chart.get_tk_widget().pack_forget()
            ax3.set_title("No User Plants")
        else:
            # percentage_user_plants = (len(user_plants) / total_plants) * 100
            # percentage_user_planted_plants = (
            #    len(user_planted_plants) / total_plants
            # ) * 100
            labels = [
                f"User Plants {len(user_plants)}",
                f"Planted Plants {len(user_planted_plants)}",
            ]
            sizes = [len(user_plants), len(user_planted_plants)]
            colors = ["lightblue", "lightgreen"]
            # labels = ["User Plants", "User Planted Plants"]
            # sizes = [percentage_user_plants, percentage_user_planted_plants]
            # colors = ["lightblue", "lightgreen"]

            ax3.clear()
            ax3.pie(
                sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140
            )

            ax3.set_title("User Plants vs User Planted Plants")
            fig.set_facecolor(sensor_monitor_frame_bg)
            ax3.set_facecolor(sensor_monitor_frame_bg)

            # Redraw the pie chart
            canvas_pie_chart.draw()
            canvas_pie_chart.get_tk_widget().pack(
                side=tk.LEFT, fill=tk.BOTH, expand=True
            )

    header_bg = "#66c644"
    header_font = 9
    log_out_btn_bg = "#679436"
    header_font_fg = "#ffffff"
    sensor_monitor_frame_bg = "#F7E8AF"
    FONT = ("Roboto Mono", 12)
    plant_list_bg = "#8BC34A"  # "#F5F5F5"
    plant_list_fg = "#000000"
    pot_list_bg = "#8FC1E3"
    pot_list_fg = "#FFFFFF"

    """For plant list:

    Text color: #FFFFFF (white)
    Background color: #8BC34A (light green)
    For pot list:

    Text color: #000000 (black)
    Background color: #D7CCC8 (light brown)"""

    window = tk.Tk()
    window.geometry("1920x1000")
    window.attributes("-fullscreen", True)
    window.protocol("WM_DELETE_WINDOW", on_closing)

    # ####################  header_frame  ####################
    header_frame = tk.LabelFrame(
        window,
        height=60,
        labelanchor="s",
        borderwidth=2,
        relief="groove",
        bg=header_bg,
    )

    # header - date, time, temperature
    date_time_label = tk.Label(
        header_frame,
        bg=header_bg,
        font=header_font,
        fg=header_font_fg,
    )
    # header app name
    app_title_label = tk.Label(
        header_frame,
        text="PyFlora - User View",
        font=header_font,
        padx=20,
        pady=10,
        bg=header_bg,
        fg=header_font_fg,
    )
    # header logout button
    log_out_btn = tk.Button(
        header_frame,
        text="Log Out",
        font=header_font,
        command=on_closing,
        relief="raised",
        bg=log_out_btn_bg,
        fg=header_font_fg,
    )
    header_frame.pack(fill="x")
    date_time_label.pack(side="left", padx=20, pady=10)
    app_title_label.place(relx=0.5, rely=0.5, anchor="center")
    log_out_btn.pack(side="right", padx=20, pady=10)

    # ####################  sensor&chart_frame  ####################
    sensor_chart_frame = tk.Frame(window, bg=sensor_monitor_frame_bg)

    # sensor_monitor_frame gui
    sensor_monitor_frame = tk.LabelFrame(
        sensor_chart_frame, text="Sensors Data", bg=sensor_monitor_frame_bg
    )
    sync_button = tk.Button(
        sensor_monitor_frame,
        text="Sync",
        command=sync_data,
        bg=sensor_monitor_frame_bg,
        activebackground=sensor_monitor_frame_bg,
    )
    moisture_label = tk.Label(
        sensor_monitor_frame,
        text="Moisture: N/A",
        justify="left",
        bg=sensor_monitor_frame_bg,
    )
    ph_label = tk.Label(
        sensor_monitor_frame, text="pH: N/A", justify="left", bg=sensor_monitor_frame_bg
    )
    salinity_label = tk.Label(
        sensor_monitor_frame,
        text="Salinity: N/A",
        justify="left",
        bg=sensor_monitor_frame_bg,
    )
    light_label = tk.Label(
        sensor_monitor_frame,
        text="Light: N/A",
        justify="left",
        bg=sensor_monitor_frame_bg,
    )
    temp_label = tk.Label(
        sensor_monitor_frame,
        text="Temperature: N/A",
        justify="left",
        bg=sensor_monitor_frame_bg,
    )
    # sensor_monitor_frame positioning
    sensor_monitor_frame.pack(side="left", padx=10)
    sensor_monitor_frame.columnconfigure(0, weight=1, minsize=400)
    sync_button.grid(column=0, row=5, padx=10, pady=10, sticky="ew")
    moisture_label.grid(column=0, row=0, sticky="w", padx=10)
    ph_label.grid(column=0, row=1, sticky="w", padx=10)
    salinity_label.grid(column=0, row=2, sticky="w", padx=10)
    light_label.grid(column=0, row=3, sticky="w", padx=10)
    temp_label.grid(column=0, row=4, sticky="w", padx=10)
    # ####################sensor_chart_frame positioning####################
    sensor_chart_frame.pack(fill="x")
    sensor_chart_frame.columnconfigure(0, weight=1, uniform="col")
    sensor_chart_frame.columnconfigure(1, weight=1, uniform="col")
    sensor_chart_frame.columnconfigure(2, weight=1, uniform="col")
    sensor_chart_frame.columnconfigure(3, weight=1, uniform="col")
    sensor_chart_frame.rowconfigure(0, weight=1, minsize=250, uniform="row")
    # ####################charts####################
    # chart frame
    chart_frame = tk.Frame(sensor_chart_frame, bg=sensor_monitor_frame_bg)
    chart_frame.pack(fill="both", expand=True)

    chart_width = 400
    chart_min_height = 250
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    # light chart
    chart_light_values = sync_data()["chart_light_values_list"]["value"]
    chart_light = plt.figure(figsize=(chart_width / 100, chart_min_height / 100))
    ax1 = chart_light.add_subplot(111)
    ax1.bar(days_of_week, chart_light_values)
    ax1.set_title("Light Chart")
    chart_light.set_facecolor(sensor_monitor_frame_bg)
    ax1.set_facecolor(sensor_monitor_frame_bg)

    canvas1 = FigureCanvasTkAgg(chart_light, master=chart_frame)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # humidity chart
    chart_humidity_values = sync_data()["chart_humidity_values_list"]["value"]
    chart_humidity = plt.figure(figsize=(chart_width / 100, chart_min_height / 100))
    ax2 = chart_humidity.add_subplot(111)
    ax2.plot(days_of_week, chart_humidity_values, marker="o")
    ax2.set_title("Humidity Chart")
    chart_humidity.set_facecolor(sensor_monitor_frame_bg)
    ax2.set_facecolor(sensor_monitor_frame_bg)

    canvas2 = FigureCanvasTkAgg(chart_humidity, master=chart_frame)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # pie chart
    fig, ax3 = plt.subplots(
        figsize=(chart_width / 100, chart_min_height / 100),
        dpi=100,
    )
    canvas_pie_chart = FigureCanvasTkAgg(fig, master=chart_frame)

    """user_plants = my_plant_service.get_user_plants(current_user_id, False)
    user_planted_plants = my_plant_service.get_user_plants(current_user_id, True)

    fig = plt.figure(figsize=(chart_width / 100, chart_min_height / 100))
    ax3 = fig.add_subplot(111)

    labels = ["User Plants", "Planted Plants"]
    sizes = [len(user_plants), len(user_planted_plants)]

    # Check if either user_plants or user_planted_plants is 0
    if 0 in sizes:
        # Display a message indicating there are no data points
        no_data_message = "No data available"
        ax3.text(
            0.5,
            0.5,
            no_data_message,
            horizontalalignment="center",
            verticalalignment="center",
            transform=ax3.transAxes,
            fontsize=12,
            color="gray",
        )
    else:
        total_plants = sum(sizes)
        percentages = [f"{(size / total_plants) * 100:.2f}%" for size in sizes]
        labels = [
            f"{label}\n({sizes[i]} plants, {percentages[i]})"
            for i, label in enumerate(labels)
        ]

        # Plot the pie chart with the available data
        ax3.pie(sizes, labels=labels)
        ax3.set_title("User Plants")

    fig.set_facecolor(
        sensor_monitor_frame_bg
    )  # Set the background color of the entire figure
    ax3.set_facecolor(
        sensor_monitor_frame_bg
    )  # Set the background color of the pie chart

    canvas3 = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas3.draw()
    canvas3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)"""

    """    # chart frame positioning
    chart_frame.pack(fill="both", expand=True)
    chart_frame.pack_propagate = False
    chart_frame.rowconfigure(0, minsize=300, uniform="row")
    chart_frame.columnconfigure(0, weight=1, uniform="col")
    chart_frame.columnconfigure(1, weight=1, uniform="col")
    chart_frame.columnconfigure(2, weight=1, uniform="col")"""

    ##############################################################
    # ####################plant_pot_list_frame####################
    plant_pot_list_frame = tk.LabelFrame(window, padx=10, pady=10)
    plant_pot_list_frame.pack(fill="both", expand=True)
    plant_pot_list_frame.columnconfigure(0, weight=1, uniform="col")
    plant_pot_list_frame.columnconfigure(1, weight=1, uniform="col")
    plant_pot_list_frame.rowconfigure(0, weight=1)

    plant_list_label_frame = tk.LabelFrame(
        plant_pot_list_frame,
        text="PLANT LIST",
        borderwidth=2,
        relief="groove",
        labelanchor="n",
        padx=5,
        pady=5,
    )
    plant_list_label_frame.grid(row=0, column=0, sticky="nsew")
    plant_list_label_frame.columnconfigure(0, weight=1)

    # plant_list_label_frame widgets
    add_new_plant_btn = tk.Button(
        plant_list_label_frame,
        text="Add New Plant",
        padx=5,
        pady=5,
        width=20,
        command=add_new_plant,
    )
    add_new_plant_btn.pack(side="top", anchor="nw", pady=10)

    scrollable_canvas = tk.Canvas(
        plant_list_label_frame, borderwidth=0, highlightthickness=0
    )
    scrollable_canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(
        plant_list_label_frame, orient="vertical", command=scrollable_canvas.yview
    )
    scrollbar.pack(side="right", fill="y")
    scrollable_canvas.config(yscrollcommand=scrollbar.set)

    plant_frame = tk.Frame(scrollable_canvas, pady=5)
    plant_frame.pack(side="top", fill="both", anchor="w", expand=True)

    scrollable_canvas.create_window((454, 0), window=plant_frame)

    def enable_scroll(event):
        scrollable_canvas.bind_all(
            "<MouseWheel>",
            lambda event: scrollable_canvas.yview_scroll(
                int(-1 * (event.delta / 120)), "units"
            ),
        )

    def disable_scroll(event):
        scrollable_canvas.unbind_all("<MouseWheel>")

    scrollable_canvas.bind("<Enter>", enable_scroll)
    scrollable_canvas.bind("<Leave>", disable_scroll)

    plant_frame.bind(
        "<Configure>",
        lambda event, canvas=scrollable_canvas: canvas.configure(
            scrollregion=canvas.bbox("all")
        ),
    )

    # pot_list_label_frame widgets
    pot_list_label_frame = tk.LabelFrame(
        plant_pot_list_frame,
        text="POT LIST",
        borderwidth=2,
        relief="groove",
        labelanchor="n",
        padx=5,
        pady=5,
    )
    pot_list_label_frame.grid(row=0, column=1, sticky="nsew")
    pot_list_label_frame.columnconfigure(1, weight=1)

    scrollable_pot_canvas = tk.Canvas(
        pot_list_label_frame, borderwidth=0, highlightthickness=0
    )
    scrollable_pot_canvas.pack(side="left", fill="both", expand=True)

    scrollbar_pot = tk.Scrollbar(
        pot_list_label_frame, orient="vertical", command=scrollable_pot_canvas.yview
    )
    scrollbar_pot.pack(side="right", fill="y")
    scrollable_pot_canvas.config(yscrollcommand=scrollbar_pot.set)

    pot_frame = tk.Frame(scrollable_pot_canvas, pady=5)
    pot_frame.pack(side="top", fill="both", anchor="w", expand=True)

    scrollable_pot_canvas.create_window((0, 0), window=pot_frame)

    def enable_pot_scroll(event):
        scrollable_pot_canvas.bind_all(
            "<MouseWheel>",
            lambda event: scrollable_pot_canvas.yview_scroll(
                int(-1 * (event.delta / 120)), "units"
            ),
        )

    def disable_scroll(event):
        scrollable_pot_canvas.unbind_all("<MouseWheel>")

    scrollable_pot_canvas.bind("<Enter>", enable_pot_scroll)
    scrollable_pot_canvas.bind("<Leave>", enable_pot_scroll)

    pot_frame.bind(
        "<Configure>",
        lambda event, canvas=scrollable_pot_canvas: canvas.configure(
            scrollregion=canvas.bbox("all")
        ),
    )

    update_time()  # start updating the time label
    load_plants()
    load_planted_plants()
    update_pie_chart()
    window.update()
    window.mainloop()
