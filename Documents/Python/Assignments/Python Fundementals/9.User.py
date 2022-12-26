class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email 
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print("User:", (self.name), ",Balance:" ,(self.account_balance),"$")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


guido = User("Guido Roi", "guido@python.com")
mia = User("Mia Jow" , "miajow@gmail.com")
sia = User("Sia Doe", "siadoe@mail.com")

guido.make_deposit(100)
guido.make_deposit(300)
guido.make_deposit(250)
guido.make_withdrawal(400)
guido.display_user_balance()

mia.make_deposit(550)
mia.make_deposit(300)
mia.make_withdrawal(150)
mia.make_withdrawal(70)
mia.display_user_balance()

sia.make_deposit(2000)
sia.make_withdrawal(250)
sia.make_withdrawal(150)
sia.make_withdrawal(300)
sia.display_user_balance()

guido.transfer_money(sia, 200)
sia.display_user_balance()
guido.display_user_balance()





