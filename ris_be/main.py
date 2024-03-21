from typing import Dict

from fastapi import FastAPI

from utils.objects_class import *
from utils import setors

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/stock/")
async def stock_position(limit: int, offset: int):
    return {'stock': 'test'} # TODO implement iquery in database

@app.post("/food_dish/")
async def create_food_dish(food_dish: FoodDish):
    return {'new_food_dish': 'test'} # TODO implement insertion with verifications in database

@app.post("/items/")
async def creat_new_item(item: FoodItem):
    return item # TODO implement insertion with verifications in database

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id} # TODO: implement query in database

@app.get("/rebuy_order/{rebuy_order_id}")
async def read_rebuy_order(rebuy_order_id: int):
    return {"rebuy_order_id": rebuy_order_id} # TODO: implement query in database

@app.post("/rebuy_order/")
async def edit_rebuy_order(rebuy: EditRebuyOrder):
    return {"rebuy_order_id": 'test'}

@app.post("/approve/{setor}")
async def approve(setor: str, approve_item: Approve):
    assert setor in setors.keys(), 'Not existent setor'

    return setors[setor](approve_item) # TODO: implement insertion with verifications in database
