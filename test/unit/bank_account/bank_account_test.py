import unittest
from bank_account.bank_account import Account, Bank


class TestAccount(unittest.TestCase):

    def test_account_object_can_be_created(self):
        account = Account("001", 50)
        self.assertEqual(account.account_number, "001")
        self.assertEqual(account.balance, 50)


class BankTest(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()
        account_1 = Account("001", 50)
        account_2 = Account("002", 100)
        self.bank.add_account(account_1)
        self.bank.add_account(account_2)

    def test_bank_is_initially_empty(self):
        bank = Bank()
        self.assertDictEqual({}, bank.accounts)
        self.assertEqual(len(bank.accounts), 0)

    def test_add_account(self):
        self.assertEqual(len(self.bank.accounts), 2)

    def test_get_account_balance(self):
        self.assertEqual(self.bank.get_account_balance("001"), 50)
        self.assertEqual(self.bank.get_account_balance("002"), 100)

if __name__ == '__main__':
    unittest.main()