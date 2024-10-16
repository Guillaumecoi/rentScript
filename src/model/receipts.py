import sqlite3

class Receipt:
    def __init__(self, name, amount, date, account_sender, account_receiver, message):
        self.name = name
        self.amount = amount
        self.date = date
        self.account_sender = account_sender
        self.account_receiver = account_receiver
        self.message = message
        
    def __str__(self):
        return f'{self.date} - {self.name} - {self.amount} - {self.account_sender} - {self.account_receiver} - {self.message}'
    
    def save(self):
        try:
            conn = sqlite3.connect('rent.db')
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO Payments (name, amount, payment_date, account_number, message)
            VALUES (?, ?, ?, ?, ?)
            ''', (self.name, self.amount, self.date, self.account_number, self.message))
            conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"IntegrityError: {e}")
            print(f"Payment: {self}")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            print(f"Payment: {self}")
        except Exception as e:
            print(f"Exception in save method: {e}")
            print(f"Payment: {self}")
        finally:
            conn.close()