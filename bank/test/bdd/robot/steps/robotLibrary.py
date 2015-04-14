from nose.tools import assert_equal, assert_in
from webtest import TestApp

from bank.bank.bank_app import app, BANK
from bank.bank.bank_account import Account


class robotLibrary(object):

    def __init__(self):
        self.browser = None
        self.response = None
        self.form_response = None

    def Create_Account(self, account_number, balance):
        account = Account(account_number, balance)
        BANK.add_account(account)

    def Visit_Homepage(self):
        self.browser = TestApp(app)
        self.response = self.browser.get('http://localhost:5000/')
        assert_equal(self.response.status_code, 200)

    def Enter_Account(self, account_number):
        form = self.response.forms['account-form']
        form['account_number'] = account_number
        self.form_response = form.submit()
        assert_equal(self.form_response.status_code, 200)

    def Get_Balance(self, expected_balance):
        assert_in("Balance: {}".format(expected_balance), self.form_response.text)