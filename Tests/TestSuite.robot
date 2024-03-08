*** Settings ***
Library    SeleniumLibrary
Library    ./Libraries/CustomPlugin.py
*** Test Cases ***
Test Plugin Keywords
    Library    SeleniumLibrary    plugins=plugins.CustomPlugin;arg_value;varg1;varg2;kw1=kwarg1;kw2=kwarg2    Custom Keyword From Plugin
