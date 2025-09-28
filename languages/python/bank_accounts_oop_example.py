class BankAccount:
    MIN_BALANCE = 0

    def __init__(self, balance=0):
        if balance <= 0:
            balance = BankAccount.MIN_BALANCE
            print('Balance can\'t be negative')
        self.balance = balance

    def withdraw(self, amount):
        if amount < 0:
            print('Withdrawn amount (${}) cannot be negative'.format(amount))
            return
        elif amount > self.balance:
            print('Withdrawn amount (${}) cannot be more than your balance (${})'.format(amount, self.balance))
            return
        self.balance -= amount
        return '${} is withdrawn. Current balance is {}'.format(amount, self.balance)

    def deposit(self, amount):
        if amount <= 0:
            print('Amount can\'t be negative.')
            return
        self.balance += amount

    def get_balance(self):
        return 'Your current balance is {}'.format(self.balance)

b = BankAccount(-10)
b.deposit(-100)
b.deposit(100)
print(b.get_balance())
b.withdraw(-200)
print(b.get_balance())
b.withdraw(200)
print(b.get_balance())
b.withdraw(50)
print(b.get_balance())
 

class SavingsAccount(BankAccount):
    def __init__(self, amount, interest_rate):
        print('Opening a savings account')
        BankAccount.__init__(amount)
        self.interest_rate = interest_rate


s = SavingsAccount(300, 1)
print(s.get_balance())
