import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_expenses():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


expenses = load_expenses()


def add_expense():
    title = input("Expense name: ").strip()
    category = input("Category: ").strip()

    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    expense = {
        "title": title,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added and saved.")


def show_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Expenses ---")

    total = 0

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['title']} | "
            f"{expense['amount']:.2f} € | "
            f"{expense['category']}"
        )
        total += expense["amount"]

    print(f"\nTotal expenses: {total:.2f} €")


def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return

    show_expenses()

    try:
        number = int(input("\nEnter expense number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if 1 <= number <= len(expenses):
        removed = expenses.pop(number - 1)
        save_expenses()
        print(f"{removed['title']} deleted successfully.")
    else:
        print("Invalid expense number.")


while True:
    print("\n--- Expense Tracker ---")
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Delete expense")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
