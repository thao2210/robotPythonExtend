from SeleniumLibrary import SeleniumLibrary
from ImdbHomePage import  ImdbHomePage
from ImdbTopMovie import ImdbTopMovie
from PluginDemo import PluginDemo

class DepositionDemo(SeleniumLibrary):
    def __init__(self):
        SeleniumLibrary.__init__(self)

        self.add_library_components([
            PluginDemo(self),
            ImdbHomePage(self),
            ImdbTopMovie(self)
        ])

