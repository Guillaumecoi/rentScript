# src/database.py
import sqlite3
from config import DATABASE_NAME

class Database:
    """ Class to interact with the database """
    def __init__(self, db_name=DATABASE_NAME):
        self.db_name = db_name
        self.conn = None

    def connect(self):
        """ Connect to the database """
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def close(self):
        """ Close the connection to the database """
        if self.conn:
            self.conn.close()

    def execute_query(self, query, params=None):
        """ Execute a query """
        if not self.conn:
            self.connect()
        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.conn.commit()
            return cursor
        finally:
            cursor.close()
            self.close()

    def create_table(self, create_table_sql):
        self.execute_query(create_table_sql)

# Example usage
if __name__ == "__main__":
    db = Database()
    create_payments_table_sql = '''
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
    '''
    db.create_table(create_payments_table_sql)
    db.close()