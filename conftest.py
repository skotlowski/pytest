from selenium import webdriver
from pytest import fixture


@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser #you can use return instead but nothing will run after it
    #everyting after will run after each test for scope = 'function'
    #and after all tests for scope = 'session'
    print("\nTest execution is over.")