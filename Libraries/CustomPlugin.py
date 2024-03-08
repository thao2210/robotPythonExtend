from robot.libraries.BuiltIn import BuiltIn
from SeleniumLibrary.base import LibraryComponent, keyword

class CustomPlugin(LibraryComponent):

    def __init__(self, ctx, arg, *varargs, **kwargs):
        super(CustomPlugin, self).__init__(ctx)
        self.arg = arg
        self.varargs = varargs
        self.kwargs = kwargs
        self.ctx.log_to_console(f"arg: {self.arg}, varargs: {self.varargs}, kwargs: {self.kwargs}")

    @keyword
    def custom_keyword_from_plugin(self):
        """A custom keyword provided by the plugin."""
        self.ctx.log_to_console('Custom keyword from CustomPlugin executed.')
