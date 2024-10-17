from database.database import Database
from datetime import datetime


class PaymentReceipt:
    """ Class to represent a payment receipt """
    db = Database()
    
    def __init__(self, name: str, amount: float, date: datetime, account_sender: str, account_receiver: str, message: str):
        self.id = None
        self.name = name
        self.amount = amount
        self.date = date
        self.account_sender = account_sender
        self.account_receiver = account_receiver
        self.message = message
        
    def __str__(self):
        return f'{self.date.strftime("%d-%m-%Y")} - {self.name} - {self.amount} - {self.account_sender} - {self.account_receiver} - {self.message}'
    
    def save(self):
        """ Save the payment to the database """
        query = '''
        INSERT INTO Payments_Received (name, amount, payment_date, account_sender, account_receiver, message)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        params = (self.name, self.amount, self.date.strftime("%d-%m-%Y"), self.account_sender, self.account_receiver, self.message)
        self.db.connect()
        self.db.execute_query(query, params)
        self.db.close()
        
    @staticmethod
    def save_payments_to_database(payment_list : list):
        """ Save the payments to the database """
        # MAke sure the table exists
        db = Database()
        db.create_tables()
        
        for payment in payment_list:
            payment.save()
            
    @staticmethod
    def get_payment_receipts():
        """ Get all the payment receipts from the database """
        db = Database()
        db.connect()
        query = '''
        SELECT * FROM Payments_Received
        '''
        result = db.execute_read_query(query)
        db.close()
        return result
    

print(PaymentReceipt.get_payment_receipts())