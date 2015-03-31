class Account(object):

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance


class Bank(object):

    def __init__(self):
        self.accounts = dict()

    def add_account(self, account):
        self.accounts[account.account_number] = account.balance

    def get_account_balance(self, account_number):
        return self.accounts.get(account_number)