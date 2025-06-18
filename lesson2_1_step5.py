from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    print(y)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    input1 = browser.find_element(By.ID , "robotCheckbox")
    input1.click()
    input2 = browser.find_element(By.ID, "robotsRule")
    input2.click()
    
    input3 = browser.find_element(By.TAG_NAME, "button")
    input3.click()
finally:
    time.sleep(10)
    browser.quit()
    
