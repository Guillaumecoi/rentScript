# PDF Bank Statement Processor

This repository is a rapid prototype designed to handle PDF information from bank statements and store the extracted data in a SQLite database. The primary goal is to automate the processing of bank statements to make life easier, rather than to build a polished application.

## Features

- **PDF Reading**: Extracts text from PDF bank statements.
- **Data Parsing**: Splits the extracted text into individual transactions.
- **Data Conversion**: Converts strings into objects.
- **Database Storage**: Saves the transactions into a SQLite database.

## Requirements

- Python 3.x

Install the required libraries using:
(Tip: You can also use a virtual environment)

```sh
pip install -r requirements.txt
```

## Usage

1. **Prepare the Environment**:
   - Ensure you have Python 3.x installed.
   - Install the required libraries using the command above.

2. **Run the Script**:
   - Place your bank statement PDF in the root directory of the project.
   - Update the `file_path` variable in [`src/import_scripts/read_kbc_bank_income.py`](src/import_scripts/read_kbc_bank_income.py) to point to your PDF file.
   - Execute the script:

   ```sh
   python src/import_scripts/read_kbc_bank_income.py
   ```

3. **Database**:
   - The transactions will be stored in a SQLite database named `rent.db`.
   - The database schema is defined in [`src/database/createDb.py`](src/database/createDb.py).


## Important Notes

- **You need to use your own bank statement!** 
    - If you are with the bank, you can download an income-only sheet from them and use the script on it.
- **Dummy documents do not work**, they are used to show the layout. The script may not work on these dummy documents. When I modified the original documents into dummy documents, the script stopped working since editing PDFs have side effects (if you know how to edit PDFs without side effects, please let me know). **No I am not going to provide the original bank statements.**
