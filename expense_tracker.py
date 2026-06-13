def show_menu():
    print("\n=== EXPENSE TRACKER ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Exit")


def add_expense(expenses):
    category = input("Enter category (Food/Travel/etc): ")
    amount = float(input("Enter amount: "))

    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- Expense Details ---")
    for category, amount in expenses.items():
        print(category, ":", amount)


def total_expense(expenses):
    total = sum(expenses.values())
    print("\nTotal Expense:", total)


# MAIN PROGRAM
expenses = {}

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        total_expense(expenses)

    elif choice == "4":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")