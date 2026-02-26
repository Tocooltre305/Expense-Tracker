expenses = []
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