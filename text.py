from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
time.sleep(2)

rb = driver.find_element(By.XPATH,'//*[@id="radio-btn-example"]/fieldset/label[2]/input').click()
time.sleep(3)
