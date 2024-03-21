from enum import Enum

from utils.objects_class import Approve

def approve_inventory_write_off(approve_item: Approve):
    return {"setor": "inventory_write_off", "id": approve_item.id, "status": approve_item.status}

def approve_rebuy(approve_item: Approve):
    return {"setor": "rebuy", "id": approve_item.id, "status": approve_item.status}

def approve_food_item_invoice_add(approve_item: Approve):
    return {"setor": "food_item_invoice_add", "id": approve_item.id, "status": approve_item.status}


setors = {
    "inventory_write_off": approve_inventory_write_off,
    "rebuy": approve_rebuy,
    "food_item_invoice_add": approve_food_item_invoice_add
}
