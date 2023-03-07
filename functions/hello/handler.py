import json
from pymongo.mongo_client import MongoClient

MONGO_PASSWORD = "eyChOZKdtPaxlmps"
MONGO = MongoClient(f"mongodb+srv://ii887522:{MONGO_PASSWORD}@ii887522.odlxcf8.mongodb.net/?retryWrites=true&w=majority")
TEST_DB = MONGO.get_database("test")
PET_COLL = TEST_DB.get_collection("pets")

def handle(event, context):
    PET_COLL.insert_one({"name": "Betty", "gender": "F", "age": 5})

    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
