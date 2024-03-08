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