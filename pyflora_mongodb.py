import pymongo
import random


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
        "watering": "Twice a week,",
        "notes": "",
    },
    {
        "name": "Tomato",
        "type": "Vegetable",
        "watering": "Once a day",
        "notes": "",
    },
    {
        "name": "Basil",
        "type": "Herb",
        "watering": "Every other day",
        "notes": "",
    },
    {
        "name": "Lavender",
        "type": "Flower",
        "watering": "Once a week",
        "notes": "",
    },
    {
        "name": "Mint",
        "type": "Herb",
        "watering": "Every other day",
        "notes": "",
    },
    {
        "name": "Succulent",
        "type": "Cactus",
        "watering": "Once a month",
        "notes": "",
    },
    {
        "name": "Snake plant",
        "type": "Indoor plant",
        "watering": "Once a month",
        "notes": "",
    },
    {
        "name": "Fern",
        "type": "Indoor plant",
        "watering": "Twice a week",
        "notes": "",
    },
    {
        "name": "Spider plant",
        "type": "Indoor plant",
        "watering": "Once a week",
        "notes": "",
    },
    {
        "name": "Aloe vera",
        "type": "Cactus",
        "watering": "Once a week",
        "notes": "",
    },
]

# Insert the plant data into the collection
collection.insert_many(plants)

# Print the inserted data
for plant in collection.find():
    print(plant)


# Create a collection for the pots
collection_name = "pots"
collection = db[collection_name]
drop_collection(collection_name, db)

pots = []
for i in range(10):
    pot = {
        "name": f"Pot{i}",
        "color": random.choice(["red", "blue", "green", "yellow"]),
        "material": random.choice(["clay", "ceramic", "metal", "plastic"]),
        "size": random.randint(5, 20),
    }
    pots.append(pot)

# Insert the plant data into the collection
collection.insert_many(pots)


# Print the inserted data
for pot in collection.find():
    print(pot)
