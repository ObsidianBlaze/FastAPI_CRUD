from typing import Optional

from fastapi import FastAPI

#Creating an instance of the FastAPI constructor
app = FastAPI()

#Route to the homepage.
@app.get("/")
def read_root():
    return {"Hello": "World"}

#Route to get an item
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}