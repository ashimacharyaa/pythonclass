# Given data
accounts = {
    "A001": {"name": "Ashim Acahrya", "balance": 15000, "pin": "1234"},
    "A002": {"name": "Prakash Pande", "balance": 8500, "pin": "5678"},
    "A003": {"name": "Manogya Guragai", "balance": 22000, "pin": "9012"}
}

def atm(account_id, pin, action, amount=0):
    # Check if the account is there or not
    if account_id not in accounts:
        print("Account not found")
        return
    
    # if ac not equal to pin send error
    if accounts[account_id]["pin"] != pin:
        print("Incorrect PIN")
        return
    
    account = accounts[account_id]
    
    # 3. check what user click balance, deposit or withdraw
    if action == "balance":
        print(f"Account Holder: {account['name']} | Current Balance: Rs. {account['balance']}")
        
    elif action == "deposit":
        account["balance"] += amount
        print(f"Successfully deposited Rs. {amount}. New Balance: Rs. {account['balance']}")
        
    elif action == "withdraw":
        if amount > account["balance"]:
            print("Insufficient funds")
        else:
            account["balance"] -= amount
            print(f"Successfully withdrew Rs. {amount}. Remaining Balance: Rs. {account['balance']}")
            
    else:
        print("Invalid action selected")

#checking functio
print("--- ATM Test Runs ---")
atm("A001", "1234", "balance")                
atm("A002", "0000", "withdraw", 2000)          
atm("A002", "5678", "deposit", 3000)           
atm("A003", "9012", "withdraw", 25000)         
atm("A004", "1111", "balance")                 
atm("A003","9012","deposit",3550)