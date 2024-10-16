import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('rent.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table with additional columns
cursor.execute('''
CREATE TABLE IF NOT EXISTS Payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    amount REAL NOT NULL,
    payment_date TEXT NOT NULL,
    account_sender TEXT,
    account_receiver TEXT,
    message TEXT,
    unique(name, amount, payment_date, account_sender, account_receiver, message)
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()