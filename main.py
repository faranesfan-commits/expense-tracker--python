import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_expenses():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


expenses = load_expenses()


def add_expense():
    title = input("Expense name: ")
    amount = float(input("Amount: "))
    category = input("Category: ")

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


while True:
    print("\n1. Add expense")
    print("2. Show expenses")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option")
