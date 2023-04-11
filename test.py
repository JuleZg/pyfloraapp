"""MY_LAT = 45.815010  # Your latitude
MY_LONG = 15.981919  # Your longitude
API_KEY = "b8fe2d48edaec121636871ffc793be7e"

import requests
from datetime import datetime, timedelta


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
    city = response_data["name"]
    print(f"The current temperature {city} is {temperature:.1f}°C")
    return temperature


temp_data()
"""

from tkinter import *

root = Tk()

# create a canvas widget
canvas = Canvas(root, width=500, height=500)
canvas.pack(fill=BOTH, expand=YES)

# load the image file
img = PhotoImage(file="plant_img/admin_view_bg.png")


# add the image to the canvas
canvas.create_image(0, 0, image=img, anchor=NW)

# create a label widget
label = Label(root, text="Hello World!")
label.pack()

root.mainloop()
