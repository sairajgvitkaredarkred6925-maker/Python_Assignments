#Create a class to represent a bank account


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.") 

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")  

    def check_balance(self):
        print(f"Current balance is {self.balance}.")     

      
account = BankAccount("ADT_41", 100000)                
account.check_balance()  
account.deposit(500)   
account.withdraw(200)  
account.withdraw(1500)  
account.check_balance() 