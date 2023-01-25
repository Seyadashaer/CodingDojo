class BankAccount:
    def __init__(self, int_rate=.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

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
    
    

    
ahmad = BankAccount(.01, 200)
lana = BankAccount(.02, 1000)

ahmad.deposit(1000).deposit(400).deposit(300).yield_interset().display_account_info()
lana.deposit(2000).deposit(1500).withdraw(200).withdraw(50).withdraw(300).withdraw(200).yield_interset().display_account_info()

# make sure that "self.balance += self.balance * self.int_rate" is correct or should be substraction?
