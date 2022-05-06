# fake bank account simmulation

class User:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print('Account created for {0.name}'.format(self))

    def show_details(self):
        details = {'name': self.name, 'age': self.age, 'gender': self.gender}
        for key, value in details.items():
            print(f'{key}: {value}')


class Account(User):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print('your account was credited with {}'.format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient balance | balance = ${0.balance}'.format(self))
        else:
            self.balance = self.balance - amount
            print('your account was debited of {}'.format(self.balance))

    def view_balance(self):
        self.show_details()
        print('Available balance = ${0.balance}'.format(self))


avatar = Account('Lineo', 26, 'female')
avatar.deposit(10000)
avatar.withdraw(400)
avatar.withdraw(1000)
