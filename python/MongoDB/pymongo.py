import pymongo
from pymongo import MongoClient

myClient = MongoClient()
db = myClient.mydb  # creating a database
users = db.users  # creating a collection

user1 = {"name": "harry", "age": 54, "hobbies": ["music", "reading", "coding"]}

user_id = insert_one(user1).inserted_id
print(user_id)  # displays a particular id

users.find().count()  # displays number of items in a collection
