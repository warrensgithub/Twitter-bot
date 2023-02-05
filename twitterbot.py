from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
driver = webdriver.Chrome()
driver.get("https://twitter.com/i/flow/login")

time.sleep(9)

username = driver.find_element(By.TAG_NAME,"input")
username.send_keys("Anapplefell1")

time.sleep(4)

next = driver.find_elements(By.XPATH,"//div[@role='button']")
next[-2].click()

time.sleep(6)

password = driver.find_element(By.XPATH,"//input[@type='password']")
password.send_keys("pineappleincident83")

time.sleep(2)

next = driver.find_elements(By.XPATH,"//div[@role='button']")
next[-1].click()

time.sleep(5)

keyword = "dr strange"
driver.get("https://twitter.com/search?q="+ keyword +"&src=typed_query&f=image")

time.sleep(7)

nscrolls = 3
for i in range (nscrolls):
    like = driver.find_elements(By.XPATH,"//div[@data-testid='like']")
    like[0].click()
    
    time.sleep(3)
    
    driver.execute_script("window.scrollTo(0,document.body.scrollheight);")
    
    time.sleep(3)