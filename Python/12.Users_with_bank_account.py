class BankAccount:
    def __init__(self,sub_account, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        self.sub_account = sub_account

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("You withdraw a:", amount)
        else:
            print("Insufficient funds: Your balance is:", self.balance)
        return self

    def yield_interset(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print("Your balance is negative")
        return self

    def display_account_info(self):
        print("Your Balance is:", self.balance)
        return self
    

class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email 
        self.account = BankAccount(sub_account=1, int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount) 
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount) 
        return self

    def display_user_balance(self):
        self.account.display_account_info()



ahmad = User("Ahmad", "ahmadw34@gmail.com")
ahmad.make_deposit(400)
ahmad.display_user_balance()


