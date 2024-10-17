import os
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
        except sqlite3.IntegrityError as e:
            print(f"IntegrityError: {e}")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Exception in execute_query method: {e}")

    def execute_sql_file(self, file_path):
        with open(file_path, 'r') as file:
            sql = file.read()
        self.execute_query(sql)

    def execute_sql_files(self, file_paths):
        for file_path in file_paths:
            self.execute_sql_file(file_path)
            
    def create_tables(self):
        self.execute_sql_file('sql/create_payments_received_table.sql')
        