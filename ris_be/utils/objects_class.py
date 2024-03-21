from typing import Dict

from pydantic import BaseModel

class FoodItem(BaseModel):
    name: str
    description: str | None = None
    buy_price: float
    tax: float | None = None
    quantity: int

class FoodDish(BaseModel):
    name: str
    description: str | None = None
    sell_price: float
    items: Dict[str, int]

class EditRebuyOrder(BaseModel):
    order_id: int
    item_id: int
    quantity: int

class Approve(BaseModel):
    id: int
    status: str