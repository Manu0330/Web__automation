*** Settings ***
Library    SeleniumLibrary
Library    AppiumLibrary
Resource   Keywords.robot
Variables    xpath.py
*** Test Cases ***
Register user
    Given login to Automation Exercise and verify new user is available
    When Create new account
    Then Delete account






    




