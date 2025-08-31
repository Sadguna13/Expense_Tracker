# Expense Tracker - Simple Python Console Application

expenses = []

def add_expense():
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    expenses.append((category, amount))
    print("Expense added.")

def view_expenses():
    total = 0
    for category, amount in expenses:
        print("Category:", category, "| Amount:", amount)
        total += int(amount)
    print("Total Expense:", total)

def main():
    while True:
        print("1. Add Expense\n2. View Expenses\n3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            break

main()