from database.database import Database
from datetime import datetime


class PaymentReceipt:
    """ Class to represent a payment receipt """
    db = Database()
    
    def __init__(self, name: str, amount: float, date: datetime, account_sender: str, account_receiver: str, message: str, id = None):
        self.id = id
        self.name = name
        self.amount = amount
        self.date = date
        self.account_sender = account_sender
        self.account_receiver = account_receiver
        self.message = message
        
    def __str__(self):
        return f'{self.date.strftime("%d-%m-%Y")} - {self.name} - {self.amount} - {self.account_sender} - {self.account_receiver} - {self.message}'
    
    def insert(self):
        """ Save the payment to the database """
        query = '''
        INSERT INTO Payments_Received (name, amount, payment_date, account_sender, account_receiver, message)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        params = (self.name, self.amount, self.date.strftime("%d-%m-%Y"), self.account_sender, self.account_receiver, self.message)
        self.db.connect()
        self.db.execute_query(query, params)
        self.db.close()
        
    def update(self):
        """ Update the payment in the database """
        query = '''
        UPDATE Payments_Received
        SET name = ?, amount = ?, payment_date = ?, account_sender = ?, account_receiver = ?, message = ?
        WHERE id = ?
        '''
        params = (self.name, self.amount, self.date.strftime("%d-%m-%Y"), self.account_sender, self.account_receiver, self.message, self.id)
        self.db.connect()
        self.db.execute_query(query, params)
        self.db.close()
        
    def delete(self):
        """ Delete the payment from the database """
        query = '''
        DELETE FROM Payments_Received
        WHERE id = ?
        '''
        params = (self.id,)
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
            payment.insert()
            
    @staticmethod
    def get_payment_receipts_raw():
        """ Get all the payment receipts from the database """
        db = Database()
        db.connect()
        query = '''
        SELECT * FROM Payments_Received
        '''
        result = db.execute_read_query(query)
        db.close()
        return result
    
    @staticmethod
    def get_payment_receipts():
        """ Get all the payment receipts from the database """
        return PaymentReceipt.convert_listof_tuples_to_listof_objects(PaymentReceipt.get_payment_receipts_raw())
    
    @staticmethod
    def convert_listof_tuples_to_listof_objects(list_of_tuples):
        """ Convert a list of tuples to a list of PaymentReceipt objects """
        payment_list = []
        for payment in list_of_tuples:
            payment_list.append(PaymentReceipt(payment[1], payment[2], datetime.strptime(payment[3], '%d-%m-%Y'), payment[4], payment[5], payment[6], payment[0]))
        return payment_list