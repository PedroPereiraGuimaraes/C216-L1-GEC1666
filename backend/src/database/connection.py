import os
import pymongo

class Database:
    def __init__(self, database, collection):
        self.connect(database, collection) 

    def connect(self, database, collection):
        try:
            connectionString = f"mongodb+srv://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@cluster.12qyqtj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True 
            )
            self.db = self.clusterConnection[database] 
            self.collection = self.db[collection] 
        except Exception as e:
            print(e)
