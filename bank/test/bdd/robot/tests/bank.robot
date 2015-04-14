*** Settings ***
Documentation   Example Robot test for
...             Bank application

Resource        ../steps/resource.robot
Resource        ../steps/steps.robot

*** Test Cases ***
Retrieve customer balance
    Given I create the account 1111 with balance 50
    When I retrieve the account 1111
    And the balance should be 50