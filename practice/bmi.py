'''
# --- Storage ---
accounts = {}   # { name: balance }
MIN_BALANCE = 100

# --- Functions ---
def create_account(name, deposit):
    if name in accounts:
        print("Account already exists.")
    elif deposit < MIN_BALANCE:
        print(f"Minimum opening balance is Rs.{MIN_BALANCE}")
    else:
        accounts[name] = deposit
        print(f"Account created for {name}. Balance: Rs.{deposit}")

def deposit(name, amount):
    if name not in accounts:
        print("Account not found.")
    elif amount <= 0:
        print("Amount must be positive.")
    else:
        accounts[name] += amount
        print(f"Deposited Rs.{amount}. New balance: Rs.{accounts[name]}")

def withdraw(name, amount):
    if name not in accounts:
        print("Account not found.")
    elif amount <= 0:
        print("Amount must be positive.")
    elif accounts[name] - amount < MIN_BALANCE:
        print(f"Cannot withdraw. Min balance Rs.{MIN_BALANCE} required.")
    else:
        accounts[name] -= amount
        print(f"Withdrawn Rs.{amount}. Remaining: Rs.{accounts[name]}")

def check_balance(name):
    if name in accounts:
        print(f"{name}'s balance: Rs.{accounts[name]}")
    else:
        print("Account not found.")

def transfer(sender, receiver, amount):
    if sender not in accounts or receiver not in accounts:
        print("One or both accounts not found.")
    elif amount <= 0:
        print("Amount must be positive.")
    elif accounts[sender] - amount < MIN_BALANCE:
        print("Insufficient balance for transfer.")
    else:
        accounts[sender] -= amount
        accounts[receiver] += amount
        print(f"Rs.{amount} transferred from {sender} to {receiver}.")

def view_all():
    print("\n--- All Accounts ---")

    if not accounts:
        print("No accounts found.")
        return

    for name, bal in accounts.items():
        print(f"{name:<10} Rs.{bal}")

# --- Menu ---
while True:
    print("\n[1]Create [2]Deposit [3]Withdraw [4]Balance [5]Transfer [6]View All [7]Quit")

    ch = input("Choice: ")

    if ch == "1":
        create_account(
            input("Name: "),
            float(input("Initial deposit: Rs."))
        )

    elif ch == "2":
        deposit(
            input("Name: "),
            float(input("Amount: Rs."))
        )

    elif ch == "3":
        withdraw(
            input("Name: "),
            float(input("Amount: Rs."))
        )

    elif ch == "4":
        check_balance(input("Name: "))

    elif ch == "5":
        transfer(
            input("From: "),
            input("To: "),
            float(input("Amount: Rs."))
        )

    elif ch == "6":
        view_all()

    elif ch == "7":
        print("Goodbye!")
        break

    else:
        print("Enter 1-7.")
        '''
def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a

print(fibonacci(6))  # 8