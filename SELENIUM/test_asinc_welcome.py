import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture()
def driver():
  chrome_driver = webdriver.Chrome()
  chrome_driver.implicitly_wait(6)
  sleep(2)
  chrome_driver.maximize_window()
  yield chrome_driver
  chrome_driver.quit()

def test_something(driver):
  driver.get('https://demoqa.com/dynamic-properties')
  btn = driver.find_element(By.ID, 'visibleAfter') 
  btn.click()