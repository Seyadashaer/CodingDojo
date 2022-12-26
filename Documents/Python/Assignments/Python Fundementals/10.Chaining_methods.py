class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email 
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("User:", (self.name), ",Balance:" ,(self.account_balance),"$")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self


guido = User("Guido Roi", "guido@python.com")
mia = User("Mia Jow" , "miajow@gmail.com")
sia = User("Sia Doe", "siadoe@mail.com")

guido.make_deposit(100).make_deposit(300).make_deposit(250).make_withdrawal(400).display_user_balance()

mia.make_deposit(550).make_deposit(300).make_withdrawal(150).make_withdrawal(70).display_user_balance()

sia.make_deposit(2000).make_withdrawal(250).make_withdrawal(150).make_withdrawal(300).display_user_balance()

guido.transfer_money(sia, 200).display_user_balance()

sia.display_user_balance()


# Why account_balance in line 21 appears like that?





