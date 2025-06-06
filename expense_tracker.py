import csv
import os
from datetime import datetime

PASSWORD = "user@123"

def authenticate():
    print("🔒 Expense Tracker Login")
    attempts = 3
    while attempts > 0:
        pwd = input("Enter password: ").strip()
        if pwd == PASSWORD:
            print("✅ Access granted!\n")
            return True
        else:
            attempts -= 1
            print(f"❌ Incorrect password. Attempts left: {attempts}")
    print("🚫 Too many failed attempts. Exiting...\n")
    return False

def initialize_csv():
    if not os.path.exists('expenses.csv'):
        with open('expenses.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Category', 'Amount'])

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')

    categories = ["Food", "Travel", "Bills", "Netflix", "Miscellaneous"]
    print("\n📚 Choose a category:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    while True:
        cat_choice = input("Enter category number: ").strip()
        if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
            category = categories[int(cat_choice) - 1]
            break
        else:
            print("❌ Invalid choice. Please enter a valid number.")

    amount = input("Enter amount: ").strip()

    with open('expenses.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount])
    print("✅ Expense added successfully!\n")

def view_expenses():
    try:
        with open('expenses.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            print("\n📋 All Expenses:\n")
            print(f"{'Date':<12} {'Category':<15} {'Amount':<10}")
            print("-" * 40)
            total = 0
            for row in reader:
                print(f"{row[0]:<12} {row[1]:<15} ₹{row[2]:<10}")
                total += float(row[2])
            print("-" * 40)
            print(f"Total Spending: ₹{total}\n")
    except FileNotFoundError:
        print("⚠ No expenses found. Add some first.\n")

def category_summary():
    try:
        summary = {}
        with open('expenses.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                category = row[1]
                amount = float(row[2])
                summary[category] = summary.get(category, 0) + amount
        print("\n📊 Spending by Category:\n")
        for cat, amt in summary.items():
            print(f"{cat:<15} : ₹{amt}")
        print()
    except FileNotFoundError:
        print("⚠ No expenses to summarize.\n")

def monthly_report():
    month = input("Enter month (MM): ").strip()
    year = input("Enter year (YYYY): ").strip()

    if not (month.isdigit() and year.isdigit() and len(month) == 2 and len(year) == 4):
        print("❌ Invalid month/year format.\n")
        return

    month_expenses = []
    category_totals = {}
    total = 0

    try:
        with open('expenses.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                date_str, category, amount = row
                if date_str.startswith(f"{year}-{month}"):
                    month_expenses.append(row)
                    amount = float(amount)
                    total += amount
                    category_totals[category] = category_totals.get(category, 0) + amount

        if not month_expenses:
            print(f"📭 No expenses found for {month}/{year}.\n")
            return

        print(f"\n📆 Monthly Report for {month}/{year}:\n")
        print(f"{'Date':<12} {'Category':<15} {'Amount':<10}")
        print("-" * 40)
        for row in month_expenses:
            print(f"{row[0]:<12} {row[1]:<15} ₹{row[2]:<10}")
        print("-" * 40)
        print(f"Total: ₹{total}\n")

        print("📊 Category Breakdown:")
        for cat, amt in category_totals.items():
            print(f"{cat:<15} : ₹{amt}")
        print()

    except FileNotFoundError:
        print("⚠ No expense data found.\n")

def main():
    initialize_csv()
    if not authenticate():
        return

    while True:
        print("==== Personal Expense Tracker ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Category Summary")
        print("4. View Monthly Report")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            category_summary()
        elif choice == '4':
            monthly_report()
        elif choice == '5':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
