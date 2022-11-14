import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

DRIVER_WAIT_IN_SEC = 10
ATTRACTIONS_HEARTS_XPATH = '//span[@class="attractions__favourite-heart"]'
CALC_BUTTON_XPATH = '//div[contains(@class,"calculator__action")]'

@pytest.mark.parametrize(
    'number_of_attractions, calculator_amount',
        [pytest.param(3, '0 EUR'),
        pytest.param(5, '18 EUR')]
    )
def test_calculator_amount(driver, number_of_attractions, calculator_amount):
    #Closing cookies ad
    WebDriverWait(driver, DRIVER_WAIT_IN_SEC).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'coi-banner__accept'))
        ).click()
    driver.find_element(By.LINK_TEXT, 'Attractions').click()

    #Select how much attractions add to favourite using slicing
    attractions = driver.find_elements(By.XPATH, ATTRACTIONS_HEARTS_XPATH)[:number_of_attractions]
    for attraction in attractions:
        attraction.click()

    #Clicking on calculator buttons
    for i in range(3):
        WebDriverWait(driver, DRIVER_WAIT_IN_SEC).until(
            EC.element_to_be_clickable((By.XPATH, CALC_BUTTON_XPATH))
            ).click()

    calculator_result = WebDriverWait(driver, DRIVER_WAIT_IN_SEC).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'calculator__savings-amount'))
        ).text
    assert calculator_result == calculator_amount
