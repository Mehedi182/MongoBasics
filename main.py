import os
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.errors import OperationFailure
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Access the environment variables
username = os.getenv('username')
password = os.getenv('password')
cluster = os.getenv('cluster')

cluster = MongoClient(
    f'mongodb+srv://{username}:{password}@{cluster}.lihjnli.mongodb.net/?retryWrites=true&w=majority')

db = cluster['sldb']
collection = db["employee"]

post = {"name": "Arif", "email": "arif@gmail.com"}
post2 = {"name": "Sajal", "email": "sajal@gmail.com"}
post3 = {"name": "Jony", "email": "mehedi@gmail.com"}

# inser one 
# collection.insert_one(post)
# insert many 
try:
    result = collection.insert_many([post, post2, post3])
    print("Document inserted successfully!")

except OperationFailure as e:
    # Catch the specific OperationFailure exception
    if e.code == 8000:
        print("User is not allowed to insert documents.")
    else:
        # If it's a different OperationFailure, you can handle it accordingly
        print("An error occurred:", e)
# result = collection.update_one({'_id': ObjectId('647ed84d66d80b46b789995b')}, {'$set': {'email': 'jony@gmail.com'}})
# print(result.modified_count)
# find one
# result = collection.find_one({'name': "Mehedi"})
#find all 
# results = collection.find()
# for res in results:
#     print(res["name"] + " " + res["email"])


#delete all 

# results = collection.delete_many({})