import pytest
from chromedriver_py import binary_path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from .constant import URL

@pytest.fixture
def service():
    service = Service(binary_path)
    return service

@pytest.fixture    
def driver(service):    
    driver = webdriver.Chrome(service=service)
    driver.get(URL)
    driver.maximize_window()
    return driver
