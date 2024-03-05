from robot.api import logger
from robot.api.deco import library, keyword, not_keyword
from robot.libraries.BuiltIn import BuiltIn


# @library
class Duck:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, arg1, arg2): #self is stand for current class, object
        self.selLib = BuiltIn().get_library_instance("SeleniumLibrary"); #ko the import truc tiep Selenium lib vi python ko support
        self.arg1 = arg1
        self.arg2 = arg2

   # @keyword
    def getArgInConstructor(self, required):
        result = f"The arg passing from constructor is: {self.arg1}, {self.arg2}"
        return result

    #@keyword
    def hello_world(self):
        print("heello");

    def sort_words(*words, case_sensitive=False):
        key = str.lower if case_sensitive else None
        return sorted(words, key=key)

    def strip_spaces(word, *, left=True, right=True):
        if left:
            word = word.lstrip()
        if right:
            word = word.rstrip()
        return word

    def open_and_maximize_browser(self, url, browser, searchItem):
        lib = self.selLib;
        lib.open_browser(browser=browser, url=url);
        lib.maximize_browser_window();
        lib.set_browser_implicit_wait("10");
        lib.input_text("name=q", searchItem);

