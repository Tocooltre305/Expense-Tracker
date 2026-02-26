expenses = []
def show_highest_expense():
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    highest = expenses[0]
    for expense in expenses:
        if expense["Amount"] > highest["Amount"]:
            highest = expense
    print("\n--- Highest Expense ---")
    print(f"Name: {highest['Name']}")
    print(f"Category: {highest['Category']}")
    print(f"Amount: ${highest['Amount']:.2f}")