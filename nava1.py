#1.Assinment

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

dr = webdriver.Chrome()
time.sleep(2)

dr.maximize_window()
time.sleep(2)

dr.get('https://testpages.herokuapp.com/styled/basic-html-form-test.html')
time.sleep(3)

uname = dr.find_element(By.XPATH,'//*[@id="HTMLFormElements"]/table/tbody/tr[1]/td/input')
uname.send_keys('Navadeep')
time.sleep(3)

pd = dr.find_element(By.NAME,"password")
pd.send_keys('VVVVVVV')
time.sleep(3)

text = dr.find_element(By.XPATH,'//*[@id="HTMLFormElements"]/table/tbody/tr[3]/td/textarea')
text.clear()
time.sleep(3)

text.send_keys('Hello all')
time.sleep(3)

r = dr.find_element(By.NAME,"filename")
r.send_keys(r'C:\Users\VENKATA NAVADEEP\OneDrive\Desktop\3_SELENIUM.png')
time.sleep(3)

dr.find_element(By.XPATH,'//*[@id="HTMLFormElements"]/table/tbody/tr[5]/td/input[2]').click()
time.sleep(3)

dr.find_element(By.XPATH,'//*[@id="HTMLFormElements"]/table/tbody/tr[6]/td/input[3]').click()
time.sleep(4)

dr.find_element(By.XPATH,'//*[@id="HTMLFormElements"]/table/tbody/tr[7]/td/select/option[2]').click()
time.sleep(3)

dr.find_element(By.XPATH,'//*[@id="HTMLFormElements"]/table/tbody/tr[8]/td/select/option[6]').click()
time.sleep(5)

button = dr.find_element(By.XPATH,'//*[@id="HTMLFormElements"]/table/tbody/tr[9]/td/input[2]')
button.click()
time.sleep(20)

dr.close()



