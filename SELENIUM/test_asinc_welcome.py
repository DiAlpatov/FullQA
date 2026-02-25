import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains  ## Для цепочки вызовов

@pytest.fixture()
def driver():
  chrome_driver = webdriver.Chrome()
  sleep(2)
  chrome_driver.maximize_window()
  yield chrome_driver
  chrome_driver.quit()

def test_new_tab(driver):
  driver.get('https://www.qa-practice.com/elements/new_tab/link')
  driver.find_element(By.ID, 'new-page-link').click()
  tabs = driver.window_handles
  driver.switch_to.window(tabs[1])
  result = driver.find_element(By.ID, 'result-text')
  assert result.text == 'I am a new page in a new tab'
  driver.close()
  driver.switch_to.window(tabs[0])
  
# def test_stale_exception(driver):
#   driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')
#   checkbox = driver.find_element(By.ID,'id-checkbox_0')
#   checkbox.click()
#   submit = driver.find_element(By.ID, 'submit-id-submit')
#   submit.click()
#   assert driver.find_element(By.ID, 'result-text').text == 'select me or not'
#   checkbox.click()
#   submit.click()

def test_drop_menu(driver):
  driver.get('какой-то сайт')
  ActionChains(driver).move_to_element('здесь переменная котороую мы.find').move_to_element('здесь переменная котороую мы.find далее по списку').click().perform()
  assert driver.find_element(By.TAG_NAME, 'wfewfwef').text == 'Jacket'