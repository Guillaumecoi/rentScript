from database.database import Database


class PaymentReceipt:
    """ Class to represent a payment receipt """
    db = Database()
    
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
        """ Save the payment to the database """
        query = '''
        INSERT INTO Payments_Received (name, amount, payment_date, account_sender, account_receiver, message)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        params = (self.name, self.amount, self.date, self.account_sender, self.account_receiver, self.message)
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