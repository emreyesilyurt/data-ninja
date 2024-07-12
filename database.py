import sqlite3
from configparser import ConfigParser

# Load configuration
config = ConfigParser()
config.read('config.ini')
database_file = config['DATABASE']['DatabaseFile']

# Initialize SQLite database
conn = sqlite3.connect(database_file)
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS items
             (id INTEGER PRIMARY KEY, name TEXT, description TEXT, specs TEXT, data TEXT)''')

print("Database initialized successfully.")

def save_to_db(details, data):
    print("Saving item details and data to the database...")
    c.execute("INSERT INTO items (name, description, specs, data) VALUES (?, ?, ?, ?)",
              (details['name'], details['description'], details['specs'], data))
    conn.commit()
    print("Item details and data saved successfully.")
