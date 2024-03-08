*** Settings ***
#Library     SeleniumLibrary    plugins=${CURDIR}/../Libraries/PluginDemo.py
Library     SeleniumLibrary    plugins=Libraries.PluginDemo;arg1=log_console
Resource    ${CURDIR}/../Variables/Shopping.robot

*** Test Cases ***
Verify Shopping Item In Cart
    [Documentation]    Example test case for plugin api on  using Robot Framework
    Open Browser    ${URL}        ${BROWSER}    ${Icon_ShopSeleniumBook}
    ${listItem} =    Add Item Into Cart    ${Icon_Shop}     ${Button_AddToBasKet}    ${Title_Item}    ${Price_Item}
    Verify Item In Cart    ${Button_Cart}    ${Title_Item_Cart}    ${Price_Item_Cart}    ${listItem}