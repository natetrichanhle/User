class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def make_withdrawal(self,amount):
        self.balance -= amount
    def display_user_balance(self):
        print('User: ', self.name, ', Balance: ', self.balance)
    def transfer_money(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.balance += amount
p1 = User('Nate', 5000)
p1.make_withdrawal(200)
p1.display_user_balance()
p2 = User('Steph', 2000)
p1.transfer_money(p2,200)
p2.display_user_balance()