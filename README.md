BANK TRANSACTION VALIDATOR - PS No. 14

Run in VS Code:
1. Extract this ZIP and open the extracted folder in VS Code.
2. Open Terminal > New Terminal.
3. Run: python bank_transaction_validator.py

The sample transactions.txt runs Test Case 1.
Expected final balance: 13000 (2 valid, 0 invalid).

To run another test case, replace the contents of transactions.txt with
the transactions from that case, save, and run the command again.

The program starts with balance 10000, accepts Deposit/Withdraw,
requires a numeric positive amount no greater than 100000, prevents
withdrawals above the available balance, and changes the balance only
for valid transactions. Valid transactions are written to
valid_transactions.txt. Missing input files are handled using try-except.
