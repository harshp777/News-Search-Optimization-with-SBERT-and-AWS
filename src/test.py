from pymongo import MongoClient
import config
import pandas as pd
conn = MongoClient(config.CONNECTION_STRING)
db = conn.get_database("news_db")
collection = db.get_collection("news")
data = pd.DataFrame(list(collection.find())).drop("_id", axis=1)


