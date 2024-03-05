*** Settings ***
Library     SeleniumLibrary    plugins=${CURDIR}/../Libraries/PluginDemo.py

*** Variables ***
${URL}    https://practice.automationtesting.in/
${BROWSER}        Chrome
${Icon_ShopSeleniumBook}    //img[@alt='Shop Selenium Books']
${Icon_Shop}    //a[text()='Shop']
${Button_AddToBasKet}    //a[text()='Add to basket']
${Button_Cart}    //span[@class='cartcontents']
${Title_Item}    //div[@id='content']//h3
${Price_Item}    //ins/span[@class='woocommerce-Price-amount amount'] | //span[@class='price']/span[@class='woocommerce-Price-amount amount']
${Title_Item_Cart}    //div[@id='page-34']//td[@data-title='Product']/a
${Price_Item_Cart}    //td[@data-title='Price']//span[@class='woocommerce-Price-amount amount']
${Total_Price_Cart}    //td[@data-title='Total']//span[@class='woocommerce-Price-amount amount']

*** Test Cases ***
Add Shoping Item To Cart
    [Documentation]    Example test case for plugin api on  using Robot Framework
    Open Browser    ${URL}        ${BROWSER}    ${Icon_ShopSeleniumBook}
    ${listItem} =    Add Cart    ${Icon_Shop}     ${Button_AddToBasKet}    ${Title_Item}    ${Price_Item}
    Get Item In Cart    ${Button_Cart}    ${Title_Item_Cart}    ${Price_Item_Cart}    ${listItem}