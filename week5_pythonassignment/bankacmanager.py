class BankAccount: #creating a class
    def __init__(self,name,account,balance=0): #default balance is zero, if object not called of balance.
        self.name = name 
        self.account_number = account 
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"The deposited NPR is {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money to withdraw")
        else:
            self.balance -= amount
            print(f"Withdraw NPR is {amount}")

    def get_balance(self):
        print(f"{self.name} : {self.balance}")

#Now I will create object for client 
acc_info = [('Ashim Acharya','AA1',500000000),
            ('Hom Nath Acharya','HNA2',1000000),
            ('Susmita Subedi','SS3',500000)]

accounts = [BankAccount(n,a,b) for n, a, b in acc_info]
AA1, HNA2, SS3 = accounts    #unpacking object eg: [obj1: AA1, Obj2: HNA2 and so forth..)

AA1.deposit(30000)
HNA2.withdraw(1000)
for acc in accounts:
    acc.get_balance()