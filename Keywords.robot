*** Settings ***
Library    SeleniumLibrary
Variables    xpath.py


*** Keywords ***
login to Automation Exercise and verify new user is available
    Open Browser    https://automationexercise.com/    chrome
    Maximize Browser Window
    Element Should Be Visible     ${Home_Page_header}
    Click Element    ${Login_button}
    Element Should Be Visible    ${New_user_signup}
    Input Text    ${New_user}    manu
    Input Text    ${New_User_email}    manu1007@gmail.com
    Click Element    ${Sign_up_button}

Create new account
    Input Text    ${account_password}    Ma#12345678
    Input Text    ${First_name}    manu
    Input Text    ${Last_name}    SSS
    Input Text    ${address}    banglore
    Input Text    ${Select_state}    Karnataka
    Input Text    ${select_city}    banglore
    Input Text    ${Zipcode}    5600008
    Input Text    ${mobile_number}    9876565445
    Sleep    3s
    Scroll Element Into View    ${Scrollup_to}
    Click Element    ${create_account_button}
    Click Element    ${continue_button}
Delete account
    Click Element    ${Delete_button}
    Click Element    ${Delete_continue}





