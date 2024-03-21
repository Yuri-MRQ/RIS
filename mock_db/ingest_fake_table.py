import sqlite3
import csv

def ingest_fake_tables():
    # Connect to the SQLite database (create if it doesn't exist)
    conn = sqlite3.connect('mock_db/food_data.db')
    cursor = conn.cursor()

    # drop table if exists
    cursor.execute('DROP TABLE IF EXISTS food_dish')

    # Create the food_dish table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS food_dish (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            sell_price REAL,
            items TEXT 
        )
    ''')

    # Create the food_items table
    # drop table if exists
    cursor.execute('DROP TABLE IF EXISTS food_items')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS food_items (
            id INTEGER PRIMARY KEY,
            description TEXT,
            buy_price REAL,
            tax REAL,
            quantity INTEGER
        )
    ''')

    # Import data from food_dish.csv
    with open('mock_db/food_dish.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute('''
                INSERT INTO food_dish (id, name, description, sell_price, items)
                VALUES (:id, :name, :description, :sell_price, :items)
            ''', row)

    # Import data from food_items.csv
    with open('mock_db/food_items.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute('''
                INSERT INTO food_items (id, description, buy_price, tax, quantity)
                VALUES (:id, :description, :buy_price, :tax, :quantity)
            ''', row)

    # Save the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    ingest_fake_tables()