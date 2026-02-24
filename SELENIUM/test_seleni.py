# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from time import sleep


# options = Options()
# options.add_argument('start-maximized') ## новый вариант расширить браузер
# ## options.add_argument('--window-size=500, 1080')  ## новый вариант открыть в окне с определенным размером
# ##driver.maximize_window() ## Старый вариант

# driver = webdriver.Chrome(options=options)
# sleep(1)
# #options.add_experimental_option('detach', True)   #не закрывать браузер
# driver.get('https://www.qa-practice.com/')
# search_input = driver.find_element(By.CLASS_NAME, 'gLFyf')
# sleep(1)
# search_input.send_keys('house')

# sleep(10)


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture()
def driver():
  chrome_driver = webdriver.Chrome()
  sleep(2)
  chrome_driver.maximize_window()
  yield chrome_driver
  chrome_driver.quit()


## Поиск по имени
# def test_id_name(driver):
#   input_data = 'wwegwefwefwef'
#   driver.get('https://www.qa-practice.com/elements/input/simple')
#   text_string = driver.find_element(By.NAME, 'text_string')   ##ищим по name
#   text_string.send_keys(input_data)
#   text_string.send_keys(Keys.ENTER)
#   sleep(3)
#   result_text = driver.find_element(By.ID, 'result-text')
#   assert result_text.text == input_data

## Поиск по ксс селектору
# def test_css_selector(driver):
#   driver.get('https://www.qa-practice.com/elements/input/simple')
#   #text_string = driver.find_element(By.CSS_SELECTOR, '[placeholder="Submit me"]')
#   text_string = driver.find_element(By.CSS_SELECTOR, '.form-control')
#   text_string.send_keys('ewfwefwef')
#   #text_string.send_keys(Keys.ENTER)
#   sleep(3)
#   assert text_string.get_attribute('placeholder') == 'Submit me'

## Поиск по XPATH
# def test_byXpath(driver):
#   a='wewqewqe'
#   driver.get('https://www.qa-practice.com/elements/input/simple')
#   text_string = driver.find_element(By.XPATH, '//*[@placeholder="Submit me"]')
#   text_string.send_keys(a)
#   text_string.send_keys(Keys.ENTER)
#   sleep(3)
#   assert a.text == 'ewfwefwef'