import tkinter as tk
from tkinter import ttk
from service_prema_db.plant_service import PlantService


connection_uri = "mongodb://localhost:27017/"
database_name = "pyflora"
collection_name_plants = "plants"
collection_name_pots = "pots"
collection_name_users = "users"

my_plant_service = PlantService(connection_uri, database_name, collection_name_plants)
window = tk.Tk()
window.geometry("1700x600")


def print_selection():
    item = plants_table.selection()[0]
    values = plants_table.item(item, "values")
    name = values[0]
    plant_type = values[1]
    watering = values[2]
    description = values[3]
    
    print("Name:", name)
    print("Type:", plant_type)
    print("Watering:", watering)
    print("Description:", description)

    return name, plant, watering, description


plants = my_plant_service.find_all_plants()
plants_table_frame = tk.Frame(window)
plants_table_frame.pack(side="bottom", fill="both", expand=True)

plants_table = ttk.Treeview(
    plants_table_frame,
    columns=("name", "type", "watering", "description"),
    show="headings",
)
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
            plant["name"],
            plant["type"],
            plant["watering"],
            plant["desc"],
        ),
    )

button = tk.Button(window, text="Add Plant", command=print_selection, width=15)
button.pack(padx=10, pady=10)
window.mainloop()
