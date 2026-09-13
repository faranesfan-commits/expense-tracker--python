expenses = []

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
    print("Expense added.")

def show_expenses():
    for expense in expenses:
        print(expense)

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
        break
    else:
        print("Invalid option")
