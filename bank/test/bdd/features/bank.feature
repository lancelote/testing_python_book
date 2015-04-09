Feature: Bank web application to retrieve
  and update customer accounts

  As a customer I wish to be able to view my balance
  and update
  and withdraw from my balance

  @customer_balance
  Scenario Outline: Retrieve customer balance
    Given I create account "<account_number>" with balance of "<balance>"
    When I visit the homepage
    When I enter the account number "<account_number>"
    Then I see a balance of "<balance>"
    Examples:
      | account_number | balance |
      | 1111           | 50      |