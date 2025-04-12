import csv
from datetime import datetime

def load_transactions(filename):
    transactions = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                row["date"] = datetime.strptime(row["date"], "%Y-%m-%d")
                transactions.append(row)
    except FileNotFoundError:
        print("File not found. Starting with an empty list.")
    return transactions

def save_transaction(filename, transaction):
    fieldnames = ["date", "description", "category", "amount"]
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(transaction)

def calculate_totals(transactions):
    income = sum(t["amount"] for t in transactions if t["amount"] > 0)
    expenses = sum(t["amount"] for t in transactions if t["amount"] < 0)
    return income, abs(expenses), income - abs(expenses)

def summarize_by_category(transactions):
    summary = {}
    for t in transactions:
        cat = t["category"]
        summary[cat] = summary.get(cat, 0) + t["amount"]
    return summary

def get_largest_expense(transactions):
    expenses = [t for t in transactions if t["amount"] < 0]
    if not expenses:
        return None
    return min(expenses, key=lambda t: t["amount"])

def filter_by_date(transactions, start_date, end_date):
    return [t for t in transactions if start_date <= t["date"] <= end_date]

def print_summary(transactions):
    income, expenses, balance = calculate_totals(transactions)
    print(f"Total Income:  R{income:.2f}")
    print(f"Total Expenses: R{expenses:.2f}")
    print(f"Balance:       R{balance:.2f}")
    print("\nCategory Summary:")
    for category, amount in summarize_by_category(transactions).items():
        print(f" - {category}: R{amount:.2f}")
    print("\nLargest Expense:")
    largest = get_largest_expense(transactions)
    if largest:
        print(f"{largest['description']} - R{abs(largest['amount']):.2f} on {largest['date'].strftime('%Y-%m-%d')}")

def main():
    filename = "transactions.csv"
    transactions = load_transactions(filename)

    while True:
        print("\n1. Add Transaction")
        print("2. View Summary")
        print("3. Filter by Date")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            date_str = input("Date (YYYY-MM-DD): ")
            date = datetime.strptime(date_str, "%Y-%m-%d")
            description = input("Description: ")
            category = input("Category: ")
            amount = float(input("Amount (negative for expense): "))
            transaction = {
                "date": date.strftime("%Y-%m-%d"),
                "description": description,
                "category": category,
                "amount": amount
            }
            save_transaction(filename, transaction)
            print("Transaction saved.")
            transactions.append({
                "date": date,
                "description": description,
                "category": category,
                "amount": amount
            })
        elif choice == "2":
            print_summary(transactions)
        elif choice == "3":
            start = input("Start date (YYYY-MM-DD): ")
            end = input("End date (YYYY-MM-DD): ")
            filtered = filter_by_date(transactions, datetime.strptime(start, "%Y-%m-%d"), datetime.strptime(end, "%Y-%m-%d"))
            print_summary(filtered)
        elif choice == "4":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
