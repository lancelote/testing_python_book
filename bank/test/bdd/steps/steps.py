import requests
from behave import *
from nose.tools import assert_equal, assert_in
from webtest import TestApp
from bank.bank.bank_account import Account
from bank.bank.bank_app import app, BANK


@given('I create account "(?P<account_number>[^"]*)" with balance of "(?P<balance>[^"]*)"')
def step_impl(context, account_number, balance):
    """
    @type context behave.runner.Context
    """
    account = Account(account_number, balance)
    BANK.add_account(account)


@when('I visit the homepage')
def step_impl(context):
    """
    @type context behave.runner.Context
    """
    context.browser = TestApp(app)
    context.response = context.browser.get('http://localhost:5000/')
    assert_equal(context.response.status_code, 200)


@when('I enter the account number "(?P<account_number>[^"]*)"')
def step_impl(context, account_number):
    """
    @type context behave.runner.Context
    @type account_number str
    """
    form = context.response.forms['account-form']
    form['account_number'] = account_number
    context.form_response = form.submit()
    assert_equal(context.form_response.status_code, 200)
    assert_in("Account Number:", context.form_response.text)


@then('I see a balance of "(?P<expected_balance>[^"]*)"')
def step_impl(context, expected_balance):
    """
    @type context behave.runner.Context
    @type expected_balance str
    """
    assert_in("Balance: {}".format(expected_balance), context.form_response.text)


@given('I make a GET request to (?P<url>[^"]*)')
def step_impl(context, url):
    """
    Smoke tests
    """
    context.response = requests.get(url)
    print(context.response)


@then('I receive a successful response')
def step_imp(context):
    """
    Smoke tests
    """
    assert_equal(context.response.status_code, 200)

@when('enter username "(?P<username>[^"]*)"')
def step_impl(context, username):
    """
    Enter the username into right form
    """
    form = context.response.forms['account-form']
    form['username'] = username

@when('enter password "(?P<password>[^"]*)"')
def step_impl(context, password):
    """
    Enter the password into right form
    """
    form = context.response.forms['account-form']
    form['password'] = password

@when('I click login')
def step_impl(context):
    """
    Send form to server
    """
    context.response.click()
