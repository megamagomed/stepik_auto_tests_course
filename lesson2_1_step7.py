import time 
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    treasure_img = browser.find_element(By.ID, "treasure")
    x = treasure_img.get_attribute("valuex")
    
   
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    input1 = browser.find_element(By.ID , "robotCheckbox")
    input1.click()
    input2 = browser.find_element(By.ID, "robotsRule")
    input2.click()
    
    input3 = browser.find_element(By.TAG_NAME, "button")
    input3.click()
finally:
    time.sleep(20)
    browser.quit()