"""
Bank Transaction Validator - PS No. 14
Python 3 | Reads transactions.txt and saves valid transactions.
"""

from decimal import Decimal, InvalidOperation

OPENING_BALANCE = Decimal("10000")
TRANSACTION_LIMIT = Decimal("100000")
INPUT_FILE = "transactions.txt"
VALID_OUTPUT_FILE = "valid_transactions.txt"


def format_amount(amount):
    """Display whole amounts without an unnecessary .0."""
    return f"{amount:f}".rstrip("0").rstrip(".") if "." in f"{amount:f}" else f"{amount:f}"


def validate_transaction(transaction_type, amount, limit, available_balance):
    """Check transaction type, amount, limit, and available balance."""
    if transaction_type not in ("Deposit", "Withdraw"):
        return False, f"unknown type '{transaction_type}'"
    if amount <= 0:
        return False, "amount must be positive"
    if amount > limit:
        return False, f"exceeds limit of {format_amount(limit)}"
    if transaction_type == "Withdraw" and amount > available_balance:
        return False, "insufficient balance"
    return True, "valid"


def main():
    balance = OPENING_BALANCE
    valid_count = 0
    invalid_count = 0
    valid_transactions = []

    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as file:
            transactions = file.readlines()
    except FileNotFoundError:
        print(f"Error: '{INPUT_FILE}' was not found.")
        print("Create it in the same folder as this Python program.")
        return
    except OSError as error:
        print(f"Error reading '{INPUT_FILE}': {error}")
        return

    print("=" * 52)
    print("             BANK TRANSACTION VALIDATOR")
    print("=" * 52)
    print(f"Opening balance: {format_amount(OPENING_BALANCE)}\n")

    for line_number, raw_line in enumerate(transactions, start=1):
        line = raw_line.strip()
        if not line:
            continue

        parts = line.split(",")
        if len(parts) != 2:
            invalid_count += 1
            print(f"Line {line_number}: Invalid - expected Type,Amount.")
            continue

        transaction_type = parts[0].strip().capitalize()
        amount_text = parts[1].strip()

        try:
            amount = Decimal(amount_text)
            if not amount.is_finite():
                raise InvalidOperation
        except (InvalidOperation, ValueError):
            invalid_count += 1
            print(f"Line {line_number}: Invalid - amount '{amount_text}' is not a number.")
            continue

        is_valid, reason = validate_transaction(
            transaction_type, amount, TRANSACTION_LIMIT, balance
        )

        if not is_valid:
            invalid_count += 1
            print(f"Line {line_number}: Invalid - {reason}.")
            continue

        # Update the balance only after the transaction passes every check.
        if transaction_type == "Deposit":
            balance += amount
        else:
            balance -= amount

        valid_count += 1
        valid_transactions.append(f"{transaction_type},{amount}")
        print(f"Line {line_number}: Valid | Balance: {format_amount(balance)}")

    try:
        with open(VALID_OUTPUT_FILE, "w", encoding="utf-8") as file:
            for transaction in valid_transactions:
                file.write(transaction + "\n")
    except OSError as error:
        print(f"Warning: Could not save valid transactions: {error}")

    print("\n" + "-" * 52)
    print("                 TRANSACTION SUMMARY")
    print("-" * 52)
    print(f"Valid transactions   : {valid_count}")
    print(f"Invalid transactions : {invalid_count}")
    print(f"Final balance        : {format_amount(balance)}")
    print(f"Valid transactions saved to: {VALID_OUTPUT_FILE}")
    print("=" * 52)


if __name__ == "__main__":
    main()
