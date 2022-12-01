from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.instagram.com")
sleep(4)
driver.find_element_by_name('username').send_keys('User_2321') #replace with your username
driver.find_element_by_name('password').send_keys('pass123')   #replace with your password
sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()
sleep(10)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button").click()
sleep(6)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/section/div/div[2]/div/div/div/div/ul/li[3]/div/button/div[1]/span/img").click()
#driver.find_element_by_class_name("_abx2").send_keys("amazing") #replace with your needed word which replies to story if you needed reply means it only reply for first viewed story 
#sleep(2)
#driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/div[3]/div/div/div[1]/div[2]").click()
sleep(4)
driver.find_element_by_class_name("_abx4").click() #its only like first story post
sleep(50)


