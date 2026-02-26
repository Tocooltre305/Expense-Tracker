import sys
expenses = []
def add_expense():
    name = input("Enter expense name (e.g., Lunch): ")
    category = input("Enter category: ")
    if not name.strip() or not category.strip():
        print("Error: Name and Category cannot be empty.")
        return
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Error: Amount must be a positive number.")
            return
        expense = {"Name": name, "Category": category, "Amount": amount}
        expenses.append(expense)
        print(f"\nSuccess: Added {name}! (${amount:.2f} in {category})")
    except ValueError:
        print("Error: Letters or symbols are not allowed for amounts.")
def view_all_expenses():
    if not expenses:
        print("\nNo expenses have been recorded yet.")
        return
    print("\n--- All Recorded Expenses ---")
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. Name: {expense['Name']} | Category: {expense['Category']} | Amount: ${expense['Amount']:.2f}")
def show_total_spending():
    total = sum(exp["Amount"] for exp in expenses)
    print(f"\nTotal Spending: ${total:.2f}")
def show_highest_expense():
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    highest = max(expenses, key=lambda x: x["Amount"])
    print("\n--- Highest Expense ---")
    print(f"Name: {highest['Name']} | Category: {highest['Category']} | Amount: ${highest['Amount']:.2f}")
def clear_expense_history():
    if not expenses:
        print("\nHistory is already empty.")
        return
    confirm = input("Are you sure you want to clear all history? (yes/no): ").lower()
    if confirm == 'yes':
        expenses.clear()
        print("Expense history cleared successfully.")
    else:
        print("Action cancelled.")
def exit_program():
    print("\nThank you for using the Expense Tracker. Goodbye!")
    sys.exit()
def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Spending")
        print("4. Show Highest Expense")
        print("5. Clear Expense History")
        print("6. Exit Program")
        choice = input("Select an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_all_expenses()
        elif choice == '3':
            show_total_spending()
        elif choice == '4':
            show_highest_expense()
        elif choice == '5':
            clear_expense_history()
        elif choice == '6':
            exit_program()
        else:
            print("Invalid selection. Please try again.")
if __name__ == "__main__":
    main_menu()