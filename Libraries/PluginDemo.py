from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary.keywords import BrowserManagementKeywords
import time


class PluginDemo(LibraryComponent):
    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        ctx._original_browser_management = BrowserManagementKeywords(ctx)

    @keyword()
    def open_browser(self, url, browser, locator):
        """Overwrite existing keyword."""
        self.ctx._original_browser_management.open_browser(browser=browser, url=url)
        self.ctx.maximize_browser_window()
        self.ctx.set_browser_implicit_wait("10")
        self.ctx.wait_until_element_is_visible(locator=locator, timeout=10)

    @keyword()
    def add_cart(self, shopIcon, addToCartButton, titleItem, priceItem):
        """Adding new keyword."""
        self.ctx.click_element(shopIcon)
        time.sleep(1)
        addToCartButtonList = self.ctx.find_elements(addToCartButton)
        titleList = self.ctx.find_elements(titleItem)
        priceList = self.ctx.find_elements(priceItem)

        for button in addToCartButtonList:
            self.ctx.click_element(button)
            time.sleep(1)

        listTitlePrice = []
        for i in range(len(titleList)):
            listTitlePrice.append({titleList[i].text: priceList[i].text})

        self.info(listTitlePrice)
        return listTitlePrice

    @keyword()
    def get_item_in_cart(self, cartIcon, titleItem, priceItem, listExpected):
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
