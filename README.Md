# How to Run this project

Make sure you pipenv setup.

```bash
pipenv install
pipenv shell
```
Setup your .env and replace asign all the values.

```env
username = ""
password = ""
cluster = ""
localDb = ""
localCollection = ""
```
To run to with local setup:
```bash
python local.py
```

To run to with Cloud/Atlas setup:
```bash
python cloud.py
```
## Please go through the Overview of MongoDB sections for batter understanding abdou Mongo DB

# Overview of MongoDB

This document provides an overview of the MongoDB setups and basic queries performed. It includes information on both the local MongoDB setup and the MongoDB Cloud (Atlas) setup.

## Local MongoDB Setup

- **Description**: This MongoDB setup is installed and running locally on a specific machine.
- **Purpose**: The local setup is useful for development and testing purposes, allowing for a local environment to work with MongoDB without the need for internet connectivity or cloud infrastructure.
- **Connection Details**:
  - Host: `localhost`
  - Port: `27017`
  - Database: `<local_database_name>`

## MongoDB Cloud (Atlas) Setup

- **Description**: This MongoDB setup is hosted in the cloud using MongoDB Atlas, a fully managed database service provided by MongoDB.
- **Purpose**: The cloud setup allows for easy scalability, automatic backups, and high availability. It is ideal for production environments or when you need to access the database from multiple locations.
- **Connection Details**: Use the provided connection string to connect your application to the cloud MongoDB cluster.


## Setup MongoDB With python 

### MongoDB Local Setup

### Installation

To set up the local MongoDB environment, follow these steps:

1. Install MongoDB: Download and install MongoDB from the official MongoDB website based on your operating system. Follow the installation instructions provided.

2. Start MongoDB Server: Once installed, start the MongoDB server by running the appropriate command for your operating system.

#### Connecting to Local MongoDB

To connect to the local MongoDB server using Python, follow these steps:

1. Install the **pymongo** Package: Ensure that the `pymongo` package is installed. If not, install it using the following command:


```bash
   pip install pymongo
```

2. Make a python script. Import the Required Modules and Connect to the local MongoDB server using the following code


```python
import pymongo
from pymongo import MongoClient
# Create a MongoClient instance
client = MongoClient('localhost', 27017)

# Connect to the local MongoDB server
db = client['mydatabase']  # Replace 'mydatabase' with your desired database name
```

## MongoDB Cloud (Atlas) Setup with

### Prerequisites

Before getting started, ensure you have the following:

- MongoDB Cloud (Atlas) account
- Connection string for your MongoDB Atlas cluster

### MongoDB Atlas Account and Connection String

#### Creating a MongoDB Atlas Account

To create a MongoDB Atlas account and set up your cluster, follow these steps:

1. Go to the [MongoDB Atlas website](https://www.mongodb.com/cloud/atlas) and click on the "Get started for free" button.

2. Sign up for an account by providing your email address and creating a password.

3. Complete the registration process and log in to your MongoDB Atlas account.

4. Once logged in, follow the instructions provided by the setup wizard to create your MongoDB Atlas cluster. Specify your preferred settings such as cloud provider, region, and cluster tier.

5. Wait for the cluster creation process to complete. MongoDB Atlas will provision the resources and set up your cluster.

#### Obtaining the Connection String

To obtain the connection string for your MongoDB Atlas cluster, follow these steps:

1. Go to the MongoDB Atlas dashboard and select your cluster.

2. Click on the "Connect" button.

3. Choose "Connect your application".

4. Select your driver (Python) and the appropriate driver version.

5. Copy the connection string provided.

#### Connecting to MongoDB Cloud (Atlas) with python 

```python
import pymongo
from pymongo import MongoClient
# Create a MongoClient instance if you use Atals
client = MongoClient('<connection_string>')
# Connect to the local MongoDB server
db = client['mydatabase']  # Replace 'mydatabase' with your desired database name

```


## Here are some basic queries that were performed on the MongoDB databases:

Once connected to MongoDB you can perform various operations using Python and the `pymongo` package:

connecting to db and collection
```python
import pymongo
from pymongo import MongoClient
# Create a MongoClient instance
client = MongoClient('<connection_string>')

# Connect to the local MongoDB server
db = client['mydatabase']  # Replace 'mydatabase' with your desired database name
collection = db['mycollection']  # Replace 'mycollection' with your desired collection name`
```


replace the client with bellow client if you use local setup

```python 
client = MongoClient('localhost', 27017)
```


* **Inserting Documents**:
   Use the `insert_one()` or `insert_many()` methods to insert documents into a collection. 

```python
#Here is some items to be inserted
post = {"name": "Mehedi", "email": "mehedi@gmail.com"}
post2 = {"name": "Arif", "email": "arif@gmail.com"}
post3 = {"name": "Sajal", "email": "sajal@gmail.com"}

#insert one 
collection.insert_one(post)

#insert many
collection.insert_many([post, post2, post3])
```

- **Querying Documents**: Use the `find()` method to retrieve documents from a collection based on specific criteria.

```python 
results = collection.find()
for result in results:
	print(result)
# To Find one 
collection.find_one({'name': "Mehedi"})
```
    
- **Updating Documents**: Use the `update_one()` methods to update documents in a collection.

```python
# replace objectId with your actual id 
collection.update_one({'_id': ObjectId('647ed84d66d80b46b789995b')}, {'$set': {'email': 'mehedih@gmail.com'}})
```
    
- **Deleting Documents**: Use the `delete_one()` or `delete_many()` methods to remove documents from a collection.

```python
#delete one
collection.delete_one({'_id': ObjectId('647ed84d66d80b46b789995b')})

#delete all
collection.delete_many({})
```


## Conclusion

In this document, we have covered the basics of performing operations on MongoDB Cloud (Atlas) using Python and the `pymongo` package. You have learned how to connect to MongoDB Cloud (Atlas), insert documents into a collection, query documents based on specific criteria, update existing documents, and delete documents from a collection.

MongoDB provides a flexible and powerful way to work with your data, and Python, along with the `pymongo` package, allows you to easily interact with your MongoDB databases.

Feel free to explore the official [pymongo documentation](https://pymongo.readthedocs.io/en/stable/) for more details on advanced querying, indexing, and other features provided by the `pymongo` package.

Happy coding and enjoy working with MongoDB!