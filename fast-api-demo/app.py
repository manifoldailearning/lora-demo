from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import asyncio
import time

app = FastAPI(title="Demo App")

class demo_item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

@app.get("/") # Root endpoint
def read_root():
    return {"message": "Welcome to the Demo App using FASTAPI!"}

@app.post("/items")
def create_item(item: demo_item):
    return {"item_name": item.name, "item_price": item.price, "item_offer": item.is_offer}

@app.get("/sync")
def wait():
    time.sleep(5) # block the server for 5 seconds
    return {"message": "Sync done after 5 seconds"}

@app.get("/async")
async def async_wait():
    await asyncio.sleep(5) # non blocking wait for 5 seconds
    return {"message": "Async Sync done after 5 seconds"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Run the app on all interfaces at port 8000