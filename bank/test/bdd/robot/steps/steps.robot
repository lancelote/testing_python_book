*** Settings ***
Documentation    Step definitions

*** Variables ***
${HOME URL}     ''

*** Keywords ***
I create the account ${account_number} with balance ${balance}
    Create Account  ${account_number}   ${balance}

I retrieve the account ${account_number}
    Visit Homepage
    Enter Account   ${account_number}

the balance should be ${balance}
    Get balance     ${balance}