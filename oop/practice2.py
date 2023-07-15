import random
class BankAccount:
    def __init__(self, account_number:str) -> None:
        self.account_number:str = account_number#-...
        self.balence:int = 0

    def deposit(self, amount:int) -> None:
        """
        Description: Add money to the account
        """
        self.balence = self.balence + amount
        print(f"Deposited ${amount}")

    def withdraw(self, amount:int):
        """
        Description: Remove money from the account
        """
        if amount <= self.balence:
            self.balence = self.balence - amount
            print(f"Withdrawn ${amount}")
        else:
            print("Withdrawal Failed")

    def get_balence(self):
        """
        Description: Returns a bank account's balence
        """
        return(self.balence)
    
class Customer:
    def __init__(self, name:str) -> None:
        self.name:str = name#-...
        self.accounts:list = []

    def add_account(self, account:BankAccount):
        """
        Description: Adds an account to a customer
        """
        self.accounts.append(account)

    def get_total_balence(self):
        """
        Description: Gives the total account balence of a customer
        """
        accumulator = 0
        for i in range(len(self.accounts)):
            accumulator = accumulator + self.accounts[i].get_balence()
        return accumulator

asa_b = BankAccount("asa123")
luciano_b = BankAccount("luciano456")
joe_b = BankAccount("joe789")

test_group = [asa_b, luciano_b, joe_b] 

for i in range(len(test_group)):
    test_group[i].deposit(random.randint(0,1000))

for i in range(len(test_group)):
    test_group[i].withdraw(random.randint(0,100))

for i in range(len(test_group)):
    print(f"{test_group[i].account_number} has ${test_group[i].get_balence()}")  

asa = Customer("asa")
asa.add_account(asa_b)
asa.add_account(joe_b)
luciano = Customer("luciano")
luciano.add_account(luciano_b)
print(asa.get_total_balence() + luciano.get_total_balence())

#HOMEWORK: Make this look more professional - comment and use what learned in preply chat