from pymongo import MongoClient
from dotenv import dotenv_values

class MongoConnection(object):
    DATABASE = None
    @staticmethod
    def initialize():
        conn = MongoClient("mongodb://jamesandrade:<yourpass>@cluster0-shard-00-00.ipidc.mongodb.net:27017,cluster0-shard-00-01.ipidc.mongodb.net:27017,cluster0-shard-00-02.ipidc.mongodb.net:27017/?ssl=true&replicaSet=atlas-hklkhg-shard-0&authSource=admin&retryWrites=true&w=majority")
        MongoConnection.DATABASE = conn["flask-radar"]
    
    @staticmethod
    def insert(collection, data):
       MongoConnection.DATABASE[collection].insert_one(data) 

mongodb = MongoConnection()