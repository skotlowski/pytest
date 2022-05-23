from selenium import webdriver
from pytest import fixture
import json

json_file_path = 'test_data.json'

def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data

@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser #you can use return instead but nothing will run after it
    #everyting after will run after each test for scope = 'function'
    #and after all tests for scope = 'session'
    print("\nTest execution is over.")


@fixture(params=[webdriver.Chrome, webdriver.Firefox, webdriver.Edge])
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()


@fixture(params=load_test_data(json_file_path))
def tv_model(request):
    data = request.param
    return data
