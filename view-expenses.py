expenses = []
def view_all_expenses():
    if not expenses:
        print("\nNo expenses have been recorded yet.")
        return
    print("\n--- All Recorded Expenses ---")
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. Name: {expense['Name']} | Category: {expense['Category']} | Amount: ${expense['Amount']:.2f}")