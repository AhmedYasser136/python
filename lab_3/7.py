class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def __del__(self):
        print(f"Account {self.account_number} has been destroyed")
account1 = BankAccount("123", 1000)
