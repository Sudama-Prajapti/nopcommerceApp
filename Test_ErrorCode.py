import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("C:\drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
wait = WebDriverWait(driver,10)

driver.find_element(By.XPATH,"//input[@id='Email']").send_keys()
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys()
driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[@href='#']//p[contains(text(),'Customers')]").click()
driver.find_element(By.XPATH,"//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Add new']").click()
#customer roles
driver.find_element(By.XPATH,"//body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[9]/div[2]").click()

driver.find_element(By.XPATH,"//span[@role='presentation']").click()
time.sleep(5)

driver.close()