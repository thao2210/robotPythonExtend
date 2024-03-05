*** Settings ***
Documentation    Example test case for searching on DuckDuckGo using Robot Framework
Library           SeleniumLibrary
Library    ../Libraries/Duck.py    book    table

*** Variables ***
${BROWSER}        Chrome
${URL}            https://duckduckgo.com
${URL1}           https://www.wikipedia.org
${SEARCH_TERM}    Robot Framework

*** Test Cases ***
Search on DuckDuckGo
    Open And Maximize Browser    ${URL}    ${BROWSER}    ${SEARCH_TERM}
#    Open Browser    ${URL}    ${BROWSER}
#    Maximize Browser Window
#    Set Browser Implicit Wait    10 seconds
#    Input Text    name=q    ${SEARCH_TERM}
    Click Element    //button[@type='submit']
    Wait Until Element Is Visible    id=search_form_input
    ${search_result}=    Get Element Attribute        id=search_form_input    value
    Should Be Equal As Strings    ${search_result}    ${SEARCH_TERM}
    Capture Page Screenshot
    Close Browser
    ${result}=    GetArgInConstructor    a
    Log    ${result}duckd
    Hello World

Search on Wikipedia
    Open Browser    ${URL1}    ${BROWSER}
    Maximize Browser Window
    Set Browser Implicit Wait    10 seconds
    Input Text    id=searchInput    ${SEARCH_TERM}
    Click Element    xpath=//button[@type='submit']
    Wait Until Page Contains    ${SEARCH_TERM}
    Capture Page Screenshot
    Close Browser
    #Hello World