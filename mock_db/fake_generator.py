import csv
import random
from faker import Faker


def generate_fake_information():
    fake = Faker() 

    food_item_ids = []  # Track generated IDs for linking
    # =========Dataset 2: food_items=========
    food_items = []
    for i in range(1, 201):  # Generate more items than needed
        description = fake.word() + " " + fake.word()
        buy_price = round(random.uniform(1.00, 10.00), 2)
        tax = round(random.uniform(0.05, 0.15), 2)
        quantity = random.randint(5, 50)

        food_items.append({
            "id": i,
            "description": description,
            "buy_price": buy_price,
            "tax": tax,
            "quantity": quantity
        })
        food_item_ids.append(i)

    # =========Dataset 1: food_dish=========
    food_dishes = []

    for i in range(1, 151):
        name = fake.word() + " " + fake.word() 
        description = fake.sentence(nb_words=10)
        sell_price = round(random.uniform(8.00, 35.00), 2)

        # Create items dict, ensuring items exist in food_items
        items = {}
        for _ in range(random.randint(2, 5)):
            item_id = random.choice(food_item_ids) 
            items[item_id] = random.randint(1, 4)  # Quantity

        food_dishes.append({
            "id": i,
            "name": name,
            "description": description,
            "sell_price": sell_price,
            "items": items
        })

    # =========CSV Export=========
    with open('food_dish.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'name', 'description', 'sell_price', 'items'])
        writer.writeheader()
        writer.writerows(food_dishes)

    with open('food_items.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'description', 'buy_price', 'tax', 'quantity'])
        writer.writeheader()
        writer.writerows(food_items)

if __name__ == "__main__":
    generate_fake_information()