expenses = []
def show_total_spending():
    total = 0
    for expense in expenses:
        total += expense["Amount"]
    print(f"\nTotal Spending: ${total:.2f}")