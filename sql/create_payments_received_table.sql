CREATE TABLE IF NOT EXISTS Payments_Received (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    amount REAL NOT NULL,
    payment_date TEXT NOT NULL,
    account_sender TEXT,
    account_receiver TEXT,
    message TEXT,
    unique(name, amount, payment_date, account_sender, account_receiver, message)
);