import pytest
from selenium import webdriver

URL = 'https://copenhagencard.com/'

@pytest.fixture    
def driver():    
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.maximize_window()
    yield driver
    driver.close()
