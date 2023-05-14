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
            percentage_user_plants = (len(user_plants) / total_plants) * 100
            percentage_user_planted_plants = (
                len(user_planted_plants) / total_plants
            ) * 100

            labels = ["User Plants", "User Planted Plants"]
            sizes = [percentage_user_plants, percentage_user_planted_plants]
            colors = ["lightblue", "lightgreen"]

            ax3.clear()
            ax3.pie(
                sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140
            )
            ax3.set_title("User Plants vs User Planted Plants")

            # Redraw the pie chart
            canvas_pie_chart.draw()

user_plants = my_plant_service.get_user_plants(current_user_id, False)
user_planted_plants = my_plant_service.get_user_plants(current_user_id, True)

total_plants = len(user_plants) + len(user_planted_plants)
if total_plants != 0:
    percentage_user_plants = (len(user_plants) / total_plants) * 100
    percentage_user_planted_plants = (len(user_planted_plants) / total_plants) * 100

    labels = []
    sizes = []
    colors = []

    if len(user_plants) > 0:
        labels.append("")  # User Plants
        sizes.append(percentage_user_plants)
        colors.append("lightblue")

    if len(user_planted_plants) > 0:
        labels.append("")  # User Planted Plants
        sizes.append(percentage_user_planted_plants)
        colors.append("lightgreen")

    fig, ax3 = plt.subplots(
        figsize=(chart_width / 100, chart_min_height / 100),
        dpi=100,
    )
    ax3.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140)
    ax3.set_title("User Plants vs User Planted Plants")

    canvas_pie_chart = FigureCanvasTkAgg(ax3.figure, master=chart_frame)
    canvas_pie_chart.draw()
    canvas_pie_chart.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
else:
    ax3.clear()

    # Display empty pie chart with a message
    fig, ax3 = plt.subplots(
        figsize=(chart_width / 100, chart_min_height / 100),
        dpi=100,
    )
    # Adjust the size of the empty pie chart as needed
    ax3.set_title("No User Plants")
    ax3.axis("off")  # Hide the axis and labels

    canvas_pie_chart = FigureCanvasTkAgg(ax3.figure, master=chart_frame)
    canvas_pie_chart.draw()
    canvas_pie_chart.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
