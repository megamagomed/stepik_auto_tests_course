from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
x = browser.find_element(By.ID, "input_value").text
def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)

input = browser.find_element(By.ID, "answer")
# browser.execute_script("return arguments[0].scrollIntoView(true);", input)
browser.execute_script("window.scrollBy(0, 150);")

input.send_keys(y)
input1 = browser.find_element(By.ID, "robotCheckbox")
input1.click()
input2 = browser.find_element(By.CSS_SELECTOR,"label[for='robotsRule']")
input2.click()

button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(30)


browser.quit()
