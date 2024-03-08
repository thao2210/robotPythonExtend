from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary.keywords import BrowserManagementKeywords
from SeleniumLibrary.errors import ElementNotFound
import time

class PluginDemo(LibraryComponent):
    wait_time = 10
    def __init__(self, ctx, **arg1):
        LibraryComponent.__init__(self, ctx)
        ctx._original_browser_management = BrowserManagementKeywords(ctx)
        self.arg1 = arg1

    def log_console(self):
        self.log("test keyword")

    @keyword()
    def open_browser(self, url, browser, locator):
        """Overwrite existing keyword."""
        self.log(self.arg1)
        self.ctx._original_browser_management.open_browser(browser=browser, url=url)
        self.ctx.maximize_browser_window()
        self.ctx.set_browser_implicit_wait(self.wait_time)
        self.ctx.wait_until_element_is_visible(locator=locator, timeout=self.wait_time)

    @keyword()
    def add_item_into_cart(self, shopIcon, addToCartButton, titleItem, priceItem):
        """Adding new keyword."""
        self.ctx.click_element(shopIcon)
        time.sleep(1)
        addToCartButtonList = self.ctx.find_elements(addToCartButton)
        titleList = self.ctx.find_elements(titleItem)
        priceList = self.ctx.find_elements(priceItem)

        for _ in addToCartButtonList:
            self.ctx.click_element(_)
            time.sleep(1)

        listTitlePrice = []
        for _ in range(len(titleList)):
            listTitlePrice.append({titleList[_].text: priceList[_].text})

        self.info(listTitlePrice)
        return listTitlePrice

    @keyword()
    def verify_item_in_cart(self, cartIcon, titleItem, priceItem, listExpected):
        """Adding new keyword."""
        self.ctx.click_element(cartIcon)
        time.sleep(2)
        titleList = self.ctx.find_elements(titleItem)
        priceList = self.ctx.find_elements(priceItem)
        listTitlePrice = []
        for i in range(len(titleList)):
            listTitlePrice.append({titleList[i].text: priceList[i].text})

        self.info(listTitlePrice)
        self.info(listExpected)
        assert listTitlePrice == listExpected
