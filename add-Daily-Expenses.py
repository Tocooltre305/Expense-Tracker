expenses = []
def add_expense():
    name = input("Enter expense name (e.g., Lunch, Bus fare): ")
    category = input("Enter expense category (e.g., Food, Transport): ")
    if not category.strip():
        print("Error: Category cannot be empty.")
        return
    try:
        amount_input = input("Enter expense amount: ")
        amount = float(amount_input)
        if amount <= 0:
            print("Error: Amount must be a positive number and cannot be zero.")
            return
        new_expense = {
            "Name": name,
            "Category": category,
            "Amount": amount
        }
        expenses.append(new_expense)
        print(f"\nSuccess: Expense added!")
        print(f"Amount: ${amount:.2f} | Category: {category}")
    except ValueError:
        print("Error: Letters or symbols are not allowed. Please enter a valid number.")