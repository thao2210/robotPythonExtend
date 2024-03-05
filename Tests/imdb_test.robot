*** Settings ***
Library     ${CURDIR}/../Libraries/DepositionDemo.py

*** Variables ***
${URL}    https://www.imdb.com/
${BROWSER}        Chrome
${Label_Menu}    //span[@class='ipc-responsive-button__text']
${Option_Top250}    //span[@class='ipc-list-item__text' and text()='Top 250 Movies']
${Label_Top250}    //h1[text()='IMDb Top 250 Movies']
${Button_Sort}    //select[@id='sort-by-selector']
${Option_Sort}    //option[@value='USER_RATING']
${Label_Imdb}    //span[@data-testid='ratingGroup--imdb-rating']

*** Test Cases ***
Verify Imdb Rating Sort
    [Documentation]    Example test case for deposition on  using Robot Framework
    Open Browser    ${URL}        ${BROWSER}    ${Label_Menu}
    Click On Menu    ${Label_Menu}
    Choose Option In Menu    ${Option_Top250}
    Click On Sort And Verify    ${Label_Top250}     ${Button_Sort}    ${Option_Sort}    ${Label_Imdb}


