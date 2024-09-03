from typing import Union
from database.dbCfg import *

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    clusterPassword = "fastapipassword"
    mongoClient = MongoDBClient(clusterPassword)
    result = mongoClient.connect()
    if isinstance(result, dict) and result.get("_isError"):
        return result
    else:
        return "Hello WORLD!! Connected to MongoDB"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    if q is None:
        q = "This is a test"
    return {"item_id": item_id, "q": q}
