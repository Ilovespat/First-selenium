from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.google.com/')
assert "Google" in driver.title
element = driver.find_element(By.CLASS_NAME, "lnXdpd")
form = driver.find_element(By.NAME, "q")
form.send_keys('Python')
form.submit()
capture_path = 'C:/111/screenshot.png'
driver.save_screenshot(capture_path)
driver.close()
