*** Variables ***
${URL}    https://www.imdb.com/
${BROWSER}        Chrome
${Label_Menu}    //span[@class='ipc-responsive-button__text']
${Option_Top250}    //span[@class='ipc-list-item__text' and text()='Top 250 Movies']
${Label_Top250}    //h1[text()='IMDb Top 250 Movies']
${Button_Sort}    //select[@id='sort-by-selector']
${Option_Sort}    //option[@value='USER_RATING']
${Label_Imdb}    //span[@data-testid='ratingGroup--imdb-rating']