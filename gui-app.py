import tkinter as tk
from tkinter import messagebox
expenses = []
balance = 0.0
def start_tracking():
    global balance
    name = name_entry.get()
    try:
        balance = float(balance_entry.get())
        if not name:
            raise ValueError
        setup_main_menu(name)
    except ValueError:
        messagebox.showerror("Error", "Enter name and numeric balance.")
def add_expense():
    global balance
    desc = desc_ent.get()
    cat = cat_ent.get()
    try:
        amt = float(amt_ent.get())
        balance -= amt
        expenses.append({"desc": desc, "cat": cat, "amt": amt})
        bal_label.config(text=f"Balance: ${balance:.2f}")
        desc_ent.delete(0, tk.END)
        cat_ent.delete(0, tk.END)
        amt_ent.delete(0, tk.END)
        messagebox.showinfo("Success", "Expense added.")
    except ValueError:
        messagebox.showerror("Error", "Invalid amount.")
def show_summary():
    total = sum(e['amt'] for e in expenses)
    messagebox.showinfo("Summary", f"Total Spent: ${total:.2f}\nRemaining: ${balance:.2f}")
def show_history():
    win = tk.Toplevel(root)
    win.title("History")
    if not expenses:
        tk.Label(win, text="Empty").pack(padx=10, pady=10)
    for e in expenses:
        tk.Label(win, text=f"{e['desc']} ({e['cat']}): -${e['amt']:.2f}").pack()
def setup_main_menu(user):
    for w in root.winfo_children():
        w.destroy()
    tk.Label(root, text=f"User: {user}", font=("Arial", 10)).pack()
    global bal_label
    bal_label = tk.Label(root, text=f"Balance: ${balance:.2f}", font=("Arial", 14, "bold"))
    bal_label.pack(pady=5)
    tk.Label(root, text="Description:").pack()
    global desc_ent
    desc_ent = tk.Entry(root)
    desc_ent.pack()
    tk.Label(root, text="Category:").pack()
    global cat_ent
    cat_ent = tk.Entry(root)
    cat_ent.pack()
    tk.Label(root, text="Amount:").pack()
    global amt_ent
    amt_ent = tk.Entry(root)
    amt_ent.pack()
    tk.Button(root, text="Add Expense", command=add_expense, width=15).pack(pady=5)
    tk.Button(root, text="View All", command=show_history, width=15).pack(pady=2)
    tk.Button(root, text="Summary", command=show_summary, width=15).pack(pady=2)
    tk.Button(root, text="Exit", command=root.quit, fg="red").pack(pady=10)
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("300x450")
tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack()
tk.Label(root, text="Starting Balance:").pack(pady=5)
balance_entry = tk.Entry(root)
balance_entry.pack()
tk.Button(root, text="Login", command=start_tracking).pack(pady=20)
root.mainloop()