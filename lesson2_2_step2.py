import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)
num1 = browser.find_element(By.ID, 'num1').text
num2 = browser.find_element(By.ID, 'num2').text
sum = str(int(num1) + int(num2))

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(sum)
input = browser.find_element(By.TAG_NAME, "button")
input.click()

time.sleep(30)
browser.quit()