import re
from tools.pdf_reader import read_pdf
from model.payment_receipts import PaymentReceipt

account_receiver = ''

def get_global_account_receiver(pages):
    """ Get the account of the receiver """
    global account_receiver
    account_receiver_match = re.search(r'rekening\n([A-Z0-9 ]+)', pages[0])
    if account_receiver_match:
        account_receiver = account_receiver_match.group(1)[:-4] 

def split_data(pages):
    """ Split the data into a list of transactions """
    # split the data into a list of transactions
    pattern = re.compile(r'\d{2}-\d{2}-\d{4} .+? \d{1,6},\d{2} EUR')
    transactions = []
    for page in pages:
        matches = list(pattern.finditer(page))
        start = 0

        for i, match in enumerate(matches):
            end = match.end()
            if i < len(matches) - 1:
                next_start = matches[i + 1].start()
                transactions.append(page[start:next_start].strip())
                start = next_start
            else:
                transactions.append(page[start:].strip())
    return transactions

def convert_to_payment(transaction):
    """ Convert a transaction string to a Payment object """
    # Extract date
    date = transaction[:10]
    
    # Extract name
    name_match = re.search(r'\d{2}-\d{2}-\d{4} (.+?) \d{1,6},\d{2} EUR', transaction)
    name = name_match.group(1) if name_match else None
    
    # Extract amount
    amount_match = re.search(r'\d{1,6},\d{2} EUR', transaction)
    amount = amount_match.group(0) if amount_match else None
    
    # Extract account number
    account_number_match = re.search(r'Rekeningnummer\n([A-Z0-9 ]+)', transaction)
    account_number = account_number_match.group(1) if account_number_match else None
    
    # Extract message
    message_match = re.search(r'Mededeling\n(.+)', transaction, re.DOTALL)
    message = message_match.group(1) if message_match else None
    
    # Remove "overschrijving" or "Tijdstip\n17.39 uur\nInstantoverschrijving" and anything after it if they are at the end of the message
    if message:
        message = re.sub(r'(\nOverschrijving|\nTijdstip\n\d{2}\.\d{2} uur\nInstantoverschrijving).*$', '', message, flags=re.DOTALL).strip()
    
    # Create Receipt object
    payment = PaymentReceipt(name, amount, date, account_number, account_receiver, message)
    
    return payment
    

def save_to_database(pages):
    """ Save the transactions to the database """
    get_global_account_receiver(pages)
    list = split_data(pages)
    PaymentReceipt.save_payments_to_database([convert_to_payment(transaction) for transaction in list])
            
if __name__ == "__main__":
    file_path = 'kbc_dummy.pdf'
    pdf_pages = read_pdf(file_path)
    save_to_database(pdf_pages)  