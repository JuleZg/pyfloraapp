import pymongo
import random
from bson.binary import Binary
from pymongo import MongoClient
from bson.objectid import ObjectId
from PIL import Image
import os
from bson.binary import Binary
import io


# drops collection if it exists
def drop_collection(collection_name, db):
    if collection_name in db.list_collection_names():
        db[collection_name].drop()
        print(f"Collection '{collection_name}' dropped successfully.")
    else:
        print(f"Collection '{collection_name}' does not exist.")


# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")


# Create a database for the pyflora
db = client["pyflora"]

# Create a collection for the users
collection_name = "users"
collection = db[collection_name]
# drop_collection(collection_name, db)
users = [
    {
        "username": "admin",
        "password": "admin",
        "first_name": "Julijan",
        "last_name": "Rajic",
        "email": "email@mail.com",
    }
]


# Insert the user data into the collection
collection.insert_many(users)

# Print the inserted data
for user in collection.find():
    print(user)

# Create a collection for the plants
collection_name = "plants"
collection = db[collection_name]
drop_collection(collection_name, db)

# Define the plant data


plants = [
    {
        "name": "Rose",
        "type": "Flower",
        "watering": "Twice a week",
        "desc": "A popular flowering plant known for its sweet fragrance and variety of colors. Roses require regular watering and pruning to maintain their health and appearance.",
    },
    {
        "name": "Tomato",
        "type": "Vegetable",
        "watering": "Once a day",
        "desc": "A commonly grown vegetable that is used in many different types of cuisine. Tomatoes require full sun and regular watering to produce ripe, juicy fruit.",
    },
    {
        "name": "Basil",
        "type": "Herb",
        "watering": "Every other day",
        "desc": "An aromatic herb that is commonly used in Italian and other Mediterranean cuisine. Basil requires regular watering and pruning to maintain its flavor and appearance.",
    },
    {
        "name": "Lavender",
        "type": "Flower",
        "watering": "Once a week",
        "desc": "A fragrant flowering plant that is often used in perfumes and soaps. Lavender requires full sun and well-draining soil to thrive.",
    },
    {
        "name": "Mint",
        "type": "Herb",
        "watering": "Every other day",
        "desc": "A versatile herb that is used in a variety of dishes and beverages. Mint prefers partial shade and regular watering to keep its leaves from drying out.",
    },
    {
        "name": "Succulent",
        "type": "Cactus",
        "watering": "Once a month",
        "desc": "A type of cactus that stores water in its leaves and stems, allowing it to survive in dry conditions. Succulents prefer bright, indirect light and infrequent watering to avoid root rot.",
    },
    {
        "name": "Snake plant",
        "type": "Indoor plant",
        "watering": "Once a month",
        "desc": "A hardy indoor plant that is tolerant of low light and infrequent watering. Snake plants are known for their tall, upright leaves and air-purifying properties.",
    },
    {
        "name": "Fern",
        "type": "Indoor plant",
        "watering": "Twice a week",
        "desc": "A common indoor plant that is known for its lush, green fronds. Ferns require high humidity and regular watering to keep their leaves from drying out.",
    },
    {
        "name": "Spider plant",
        "type": "Indoor plant",
        "watering": "Once a week",
        "desc": "A popular indoor plant that is known for its long, spindly leaves and ability to tolerate low light and infrequent watering. Spider plants are also great air purifiers.",
    },
    {
        "name": "Aloe vera",
        "type": "Cactus",
        "watering": "Once a week",
        "desc": "A succulent plant that is known for its medicinal properties and gel-filled leaves. Aloe vera plants prefer bright, indirect light and infrequent watering to avoid root rot.",
    },
    {
        "name": "Sunflower",
        "type": "Flower",
        "watering": "Once a week",
        "desc": "A large, cheerful flower that is popular in gardens and as a cut flower. Sunflowers require full sun and regular watering to reach their full potential.",
    },
    {
        "name": "Zucchini",
        "type": "Vegetable",
        "watering": "Once a day",
        "desc": "A summer squash that is versatile in cooking and easy to grow. Zucchini plants require full sun and regular watering to produce their edible fruit.",
    },
    {
        "name": "Rosemary",
        "type": "Herb",
        "watering": "Once a week",
        "desc": "An aromatic herb that is commonly used in Mediterranean cuisine. Rosemary prefers full sun and well-draining soil.",
    },
    {
        "name": "Daisy",
        "type": "Flower",
        "watering": "Twice a week",
        "desc": "A classic, cheerful flower that is commonly found in gardens and floral arrangements. Daisies prefer full sun and regular watering.",
    },
    {
        "name": "Thyme",
        "type": "Herb",
        "watering": "Every other day",
        "desc": "A flavorful herb that is commonly used in Mediterranean and Middle Eastern cuisine. Thyme prefers full sun and well-draining soil.",
    },
    {
        "name": "Jade plant",
        "type": "Cactus",
        "watering": "Once a month",
        "desc": "A succulent plant with small, round leaves that is commonly grown as a houseplant. Jade plants prefer bright, indirect light and infrequent watering.",
    },
    {
        "name": "Pothos",
        "type": "Indoor plant",
        "watering": "Once a week",
        "desc": "A trailing indoor plant with variegated leaves that is easy to care for. Pothos prefer bright, indirect light and regular watering.",
    },
    {
        "name": "Peace lily",
        "type": "Indoor plant",
        "watering": "Once a week",
        "desc": "A tropical indoor plant with large, glossy leaves and white flowers. Peace lilies prefer bright, indirect light and regular watering.",
    },
    {
        "name": "Eucalyptus",
        "type": "Herb",
        "watering": "Every other day",
        "desc": "An aromatic herb with silver-green leaves that is commonly used in aromatherapy and as a decorative accent. Eucalyptus prefers full sun and well-draining soil.",
    },
    {
        "name": "Cactus",
        "type": "Cactus",
        "watering": "Once a month",
        "desc": "A type of succulent plant that comes in many shapes and sizes, often with prickly spines. Cacti prefer bright, indirect light and infrequent watering.",
        "img_data": "",
    },
]


# Insert the plant data into the collection
collection.insert_many(plants)
# get a list of all image files in the "plant_img" folder
img_folder = "plant_img/"
img_files = [
    f
    for f in os.listdir(img_folder)
    if os.path.isfile(os.path.join(img_folder, f)) and f.endswith(".png")
]

# loop through each image file
for img_file in img_files:
    # get the name of the file without the ".png" extension
    name = os.path.splitext(img_file)[0]
    # check if there is a document in the collection with a matching "name" field
    doc = collection.find_one({"name": name})
    if doc:
        # if there is a matching document, read the image file and convert it to binary data
        with open(os.path.join(img_folder, img_file), "rb") as f:
            binary_data = Binary(f.read())
        # add the binary data as a new field called "image_data" to the matching document
        collection.update_one(
            {"_id": doc["_id"]}, {"$set": {"image_data": binary_data}}
        )

#Print the inserted data
for plant in collection.find():
    print(plant["name"])



