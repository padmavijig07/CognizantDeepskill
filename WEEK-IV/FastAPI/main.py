from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Sample FastAPI App")


class Item(BaseModel):
    name: str
    price: float


@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}


@app.get("/items")
def list_items():
    return [{"name": "Laptop", "price": 1200.0}, {"name": "Mouse", "price": 20.0}]


@app.post("/items")
def create_item(item: Item):
    return {"message": "Item created", "item": item}
