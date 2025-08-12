transactions=[]
def add_income():
    source=input("Enter the source of income ")
    amount= int(input("Enter the amount of income "))
    transactions.append({"type":"income", "desc":source, "amount":amount})
    print("income added::\n")

def add_expense():
    category=input("Enter category of expense ")
    amount=float(input("Enter the amount of expense "))
    transactions.append({"type":"expense", "desc": category, "amount":amount})
    print("Expense recorded:: \n")

def view_balance():
    income = sum([t["amount"] for t in transactions if t["type"]=="income"])
    expense = sum([t["amount"] for t in transactions if t["type"]=="expense"])
    balance = income - expense
    print(f"current balance :: {balance}")

def view_history():
    print("\nTransaction History:\n")
    if not transactions:
        print("No transactions")
        return
    for t in transactions:
        sign = "+" if t["type"]=="income" else "-"
        print(f"{t['type'].title()} | {t['desc']} | {sign} {t['amount']:.2f}")

def show_menu():
    print("Budget Tracker")
    print("1 Add Income")
    print("2 Add Expense")
    print("3 View Balance")
    print("4 View History")
while True:
    show_menu()
    option=int(input("CHOOSE OPTION "))
    if option==1:
        add_income()
    elif option==2:
        add_expense()
    elif option==3:
        view_balance()
    elif option==4:
        view_history()
        break
    else:
        print("give valid input")