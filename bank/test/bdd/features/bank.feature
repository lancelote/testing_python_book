Feature: Bank web application to retrieve
  and update customer accounts

  As a customer I wish to be able to view my balance
  and update
  and withdraw from my balance

  Scenario: Retrieve customer balance
    Given I create account "1111" with balance of "50"
    When I visit the homepage
    When I enter the account number "1111"
    Then I see a balance of "50"