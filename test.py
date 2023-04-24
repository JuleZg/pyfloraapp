from service_prema_db.plant_service import PlantService
from service_prema_db.pot_service import PotService
from service_prema_db.users_service import UsersService

connection_uri = "mongodb://localhost:27017/"
database_name = "pyflora"
collection_name_plants = "plants"
collection_name_pots = "pots"
collection_name_users = "users"
collection_name_user_plant = "user_plant"


def main():
    my_plant_service = PlantService(
        connection_uri,
        database_name,
        collection_name_plants,
        collection_name_user_plant,
    )
    # my_plant_service.find_all_plants()
    my_pot_service = PotService(connection_uri, database_name, collection_name_pots)

    my_users_service = UsersService(
        connection_uri, database_name, collection_name_users
    )

    # my_plant_service.save_plant_for_user( "6436d92c71034b4156556e28", "643ea5a565423be96a729c5a"    )

    some_data = my_plant_service.get_user_plants("64355ec03a881fc338fadc5d")

    my_plant_service.delete_user_plant(
        "64418c1b211c7806cace8b61"
    )  # tu saljes id od pot_plant "dokumenta"

    print("test gotov")


if __name__ == "__main__":
    main()
"""canvas_plant_list = tk.Canvas(
        plant_list_label_frame,
        bg="red",
        width=948,
        height=400,
    )
    canvas_plant_list.grid(row=1, column=0, sticky="nsew")

    my_scrollbar = tk.Scrollbar(
        plant_list_label_frame,
        orient="vertical",
        command=canvas_plant_list.yview,
    )
    my_scrollbar.grid(row=1, column=1, sticky="ns")
    canvas_plant_list.configure(yscrollcommand=my_scrollbar.set)
    plant_list_frame = tk.Frame(canvas_plant_list)
    canvas_plant_list.create_window((0, 0), window=plant_list_frame, anchor="nw")

    canvas_plant_list.configure(scrollregion=canvas_plant_list.bbox("all"))
    canvas_plant_list.configure(scrollregion=plant_list_frame.bbox("all"))

    canvas_plant_list.bind(
        "<Configure>",
        lambda event: canvas_plant_list.configure(
            scrollregion=canvas_plant_list.bbox("all")
        ),
    )
    my_scrollbar.bind(
        "<MouseWheel>",
        lambda event: canvas_plant_list.yview_scroll(
            -1 * (event.delta // 120), "units"
        ),
    )"""
