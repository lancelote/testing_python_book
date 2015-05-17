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

Feature: Bank application smoke tests

  As a developer I wish to check that all components are up
  and responding correctly to requests
  and providing correct data

  Scenario: Make GET request to Frontend
    Given I make a GET request to http://frontend.com/
    Then I receive a successful response

  Scenario: Customer logs in and views balance
    When I visit the homepage
    When enter username "david"
    When enter password "12345"
    When I click login
    Then I see a balance of "50"
