from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .constant import (CALC_POSITIVE_AMOUNT, CALC_ZERO_AMOUNT,
                       DRIVER_WAIT_IN_SEC)


def test_zero_amount(service, driver):
    WebDriverWait(driver, DRIVER_WAIT_IN_SEC).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'coi-banner__accept'))
        ).click()

    driver.find_element(By.LINK_TEXT, 'Attractions').click()

    attractions = driver.find_elements(By.XPATH, '//span[@class="attractions__favourite-heart"]')
    for attraction in attractions[:3]:
        attraction.click()

    WebDriverWait(driver, DRIVER_WAIT_IN_SEC).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'calculator__action '))
        ).click()
    WebDriverWait(driver, DRIVER_WAIT_IN_SEC).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'calculator__action'))
        ).click()
    WebDriverWait(driver, DRIVER_WAIT_IN_SEC).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'calculator__action'))
        ).click()

    calculator_amount = WebDriverWait(driver, DRIVER_WAIT_IN_SEC).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'calculator__savings-amount'))
        ).text
    driver.close()
    assert calculator_amount == CALC_ZERO_AMOUNT

def test_positive_amount(service, driver):
    WebDriverWait(driver, DRIVER_WAIT_IN_SEC).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'coi-banner__accept'))
        ).click()
    driver.find_element(By.LINK_TEXT, 'Attractions').click()

    attractions = driver.find_elements(By.XPATH, '//span[@class="attractions__favourite-heart"]')
    for attraction in attractions[:5]:
        attraction.click()

    WebDriverWait(driver, DRIVER_WAIT_IN_SEC).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'calculator__action '))
        ).click()
    WebDriverWait(driver, DRIVER_WAIT_IN_SEC).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'calculator__action'))
        ).click()
    WebDriverWait(driver, DRIVER_WAIT_IN_SEC).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'calculator__action'))
        ).click()

    calculator_amount = WebDriverWait(driver, DRIVER_WAIT_IN_SEC).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'calculator__savings-amount'))
        ).text
    driver.close()
    assert calculator_amount == CALC_POSITIVE_AMOUNT
