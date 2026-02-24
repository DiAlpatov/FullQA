import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep


@pytest.fixture()
def driver():
  chrome_driver = webdriver.Chrome()
  sleep(2)
  chrome_driver.maximize_window()
  yield chrome_driver
  chrome_driver.quit()

# def test_clear(driver):
#   input_data = 'seleniumFalse'
#   driver.get('https://www.qa-practice.com/elements/input/simple')
#   text_string = driver.find_element(By.NAME, 'text_string') 
#   text_string.send_keys(input_data)
#   sleep(1)
#   #text_string.clear()
#   ## ИЛИ
#   # for x in range(20):
#   #   text_string.send_keys(Keys.BACKSPACE)
#   ### ИЛИ 
#   entered_value = text_string.get_attribute('value')
#   for x in range(len(entered_value)):
#     text_string.send_keys(Keys.BACKSPACE)
#   sleep(2)

## ПРОВЕРКИ В СЕЛЕНИУМ
# element.is_selected()   / is_displayed()  / is_enabled()


# def test_enabled(driver):
#   driver.get('https://www.qa-practice.com/elements/button/disabled')
#   button = driver.find_element(By.NAME, 'submit')
#   print(button.is_enabled())
#   select = driver.find_element(By.ID, 'id_select_state')
#   dropdown = Select(select)
#   dropdown.select_by_value('enabled')
#   print(button.is_enabled())
#   sleep(3)

