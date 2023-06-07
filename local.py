# Local MongoDB Setup
# Description: This MongoDB setup is installed and running locally on a specific machine.
# Purpose: The local setup is useful for development and testing purposes, allowing you to have a local environment to work with MongoDB without the need for internet connectivity or cloud infrastructure.
# Connection Details: Connect to the MongoDB server using the local IP address or hostname, and the default port (27017). Ensure that the local MongoDB server is running before connecting.

import os
from pymongo import MongoClient
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Access the environment variables
database_name = os.getenv('localDb')
collection_name = os.getenv('localCollection')

# Connection details
host = 'localhost'
port = 27017


# Create a MongoClient instance
client = MongoClient(host, port)

# Connect to the database
db = client[database_name]

# Get the collection
collection = db[collection_name]

# Find documents in the collection
documents = collection.find()

# Process the documents
for doc in documents:
    print(doc)
