*** Settings ***
Library     ${CURDIR}/../Libraries/DepositionDemo.py
Resource    ${CURDIR}/../Variables/Imdb.robot

*** Test Cases ***
Verify Imdb Rating Sort
    [Documentation]    Example test case for deposition on  using Robot Framework
    Open Browser    ${URL}        ${BROWSER}    ${Label_Menu}
    Click On Menu Icon    ${Label_Menu}
    Choose Option In Menu    ${Option_Top250}
    Choose Sort Option    ${Label_Top250}     ${Option_Sort}
    Verify Sorted Data    ${Label_Imdb}



