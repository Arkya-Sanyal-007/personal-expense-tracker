# 💸 Personal Expense Tracker

A simple Python-based command-line application for tracking your daily expenses with password protection, CSV storage, and monthly reports.

---

## 🔐 Features

- **Login System** – Secure access with password (default: `user@123`)
- **Add Expense** – Log new expenses with date, category, and amount
- **View All Expenses** – Displays a clean table of all records
- **Category Summary** – Shows how much was spent per category
- **Monthly Report** – Filters expenses by month/year with totals
- **CSV Storage** – All data saved in `expenses.csv` for persistence

---

## 🛠️ Getting Started

### 📦 Prerequisites

- Python 3.x installed
- No third-party libraries required

### 🚀 Run the Application

```bash
python expense_tracker.py
```
## 📂 File Structure
```bash
.
├── expense_tracker.py   # Main Python file
└── expenses.csv         # Auto-created, stores expense data
```
## 🧭 Menu Options
After logging, you can choose from:
==== Personal Expense Tracker ====
  1. Add Expense
  2. View All Expenses
  3. View Category Summary
  4. View Monthly Report
  5. Exit
---

## 📊 Categories
- Food
- Travel
- Bills
- Netflix
- Miscellaneous
You can customize these by modifying the categories list inside the script.

---
## 📆 Example Output

📋 All Expenses:
```
Date         Category        Amount    
----------------------------------------
2025-06-01   Food            ₹120.00    
2025-06-01   Bills           ₹450.00    
----------------------------------------
Total Spending: ₹570.0
```
Monthly Report
```yaml
📆 Monthly Report for 06/2025:

Date         Category        Amount    
----------------------------------------
2025-06-01   Food            ₹120.00    
2025-06-01   Bills           ₹450.00    
----------------------------------------
Total: ₹570.0

📊 Category Breakdown:
Food            : ₹120.0
Bills           : ₹450.0

```
---
## ✅ To Do
-  Add support for deleting/editing expenses
- Add custom category input
- Export reports to Excel/PDF
- Build a simple GUI using Tkinter
---
## ❗ Fix Reminder
Ensure the final block in your Python file is:
```
if __name__ == "__main__":
    main()
```
**(Not _name_)**

---
## 📜 License
This project is open-source and available under the MIT License.

---
## 🙌 Contribute
Contributions are welcome! Fork the repo and submit a pull request 🚀

---
