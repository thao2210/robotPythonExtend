from robot.api.deco import keyword
from SeleniumLibrary.base import LibraryComponent

class ImdbHomePage(LibraryComponent):
    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)

    @keyword
    def click_on_menu(self, menu):
        self.ctx.wait_until_element_is_visible(menu)
        self.ctx.click_element(menu)

    @keyword
    def choose_option_in_menu(self, option):
        self.ctx.wait_until_element_is_visible(option)
        self.ctx.click_element(option)