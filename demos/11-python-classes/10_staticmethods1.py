class Account:
    interest_rate = 10

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_interest_rate1():
        return Account.interest_rate

    get_interest_rate1 = staticmethod(get_interest_rate1)

    @staticmethod
    def get_interest_rate2():
        return Account.interest_rate


print(Account.get_interest_rate1())
print(Account.get_interest_rate2())

account1 = Account("pipo")
account2 = Account("mamaloe")

print(account1.name)
print(account1.get_interest_rate1())

Account.interest_rate = 11

print(account2.name)
print(account2.get_interest_rate1())
print(account2.get_interest_rate2())
print(account1.get_interest_rate2())
