#using selenium with python we automate a web page 

from selenium import  webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
time.sleep(3)
driver.maximize_window()
time.sleep(3)

driver.get('https://testpages.herokuapp.com/styled/basic-html-form-test.html')
time.sleep(3)

uname=driver.find_element(By.XPATH, '//*[@id="HTMLFormElements"]/table/tbody/tr[1]/td/input')
uname.send_keys('NAVADEEP')
time.sleep(3)

pwd=driver.find_element(By.NAME,'password')
pwd.send_keys('123456')
time.sleep(3)

text=driver.find_element(By.XPATH,'//*[@id="HTMLFormElements"]/table/tbody/tr[3]/td/textarea')
text.clear()
time.sleep(3)

text.send_keys('Hello All')
time.sleep(3)

c=driver.find_element(By.NAME,'filename')
c.send_keys('C:/Users/VENKATA NAVADEEP/OneDrive/Desktop/3_SELENIUM.png')
time.sleep(3)

driver.find_element(By.NAME,'checkboxes[]').click()
time.sleep(3)

driver.find_element(By.NAME,'radioval').click()
time.sleep(3)

driver.find_element(By.XPATH,'//*[@id="HTMLFormElements"]/table/tbody/tr[7]/td/select/option[2]').click()
time.sleep(3)

driver.find_element(By.XPATH,'//*[@id="HTMLFormElements"]/table/tbody/tr[8]/td/select/option[1]').click()
time.sleep(3)

driver.find_element(By.XPATH,'//*[@id="HTMLFormElements"]/table/tbody/tr[9]/td/input[2]').click()
time.sleep(6)

driver.close()