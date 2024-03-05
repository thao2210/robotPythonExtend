from robot.api.deco import keyword
from SeleniumLibrary.base import LibraryComponent
import time

class ImdbTopMovie(LibraryComponent):
    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)

    @keyword
    def click_on_sort_and_verify(self, labelPage, sortButton, option, imdbRating):
        self.ctx.wait_until_element_is_visible(labelPage)
        self.ctx.click_element(option)
        time.sleep(2)
        listNumbImdb = []
        ratingList = self.ctx.find_elements(imdbRating)
        for item in ratingList:
            listNumbImdb.append(self.ctx.get_element_attribute(item, "aria-label").split(':')[1].strip())

        expectedList = sorted(listNumbImdb, reverse=True)
        self.log(listNumbImdb)
        self.log(expectedList)
        assert listNumbImdb == expectedList