from pymongo import MongoClient
from bson.objectid import ObjectId
from PIL import Image
import io
from bson.binary import Binary
import os

"""# read from mongodb and display

# Connect to the MongoDB database
client = MongoClient("mongodb://localhost:27017/")
db = client["pyflora"]
collection = db["plants"]

# Retrieve the document containing the image by ID
doc_id = ObjectId("644ad480ceb4b96a0648fd86")
doc = collection.find_one({"_id": doc_id})

# Retrieve the binary image data from the document
image_data = doc.get("image", None)

if image_data:
    # Convert the binary image data to an image object using Pillow
    img = Image.open(io.BytesIO(image_data))
    img = img.convert("RGB")
    img.show()


else:
    print("No image data found for document ID", doc_id)
"""


# connect to MongoDB
client = MongoClient()
db = client["pyflora"]
collection = db["plants"]
"""
# iterate over images in the 'plant_img/' folder
for filename in os.listdir("plant_img/"):
    # check if file is an image
    if filename.endswith(".png"):
        # check if image filename matches a document in MongoDB
        matching_doc = collection.find_one({"name": filename})
        if matching_doc:
            # convert image to binary
            with open("plant_img/" + filename, "rb") as f:
                img_binary = Binary(f.read())

            # update matching document with binary image data
            collection.update_one(
                {"_id": matching_doc["_id"]}, {"$set": {"image_data": img_binary}}
            )"""




# connect to MongoDB database
client =MongoClient("mongodb://localhost:27017/")
db = client["pyflora"]
collection = db["plants"]

# get a list of all image files in the "plant_img" folder
img_folder = "plant_img/"
img_files = [f for f in os.listdir(img_folder) if os.path.isfile(os.path.join(img_folder, f)) and f.endswith('.png')]

# loop through each image file
for img_file in img_files:
    # get the name of the file without the ".png" extension
    name = os.path.splitext(img_file)[0]
    # check if there is a document in the collection with a matching "name" field
    doc = collection.find_one({"name": name})
    if doc:
        # if there is a matching document, read the image file and convert it to binary data
        with open(os.path.join(img_folder, img_file), 'rb') as f:
            binary_data = Binary(f.read())
        # add the binary data as a new field called "image_data" to the matching document
        collection.update_one({"_id": doc["_id"]}, {"$set": {"image_data": binary_data}})
