import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://demo.automationtesting.in/Windows.html")
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a").click()
time.sleep(3)
driver.find_element_by_xpath("""//*[@id="Tabbed"]/a/button""").click()
Win = driver.window_handles
print(Win)
print(len(Win))
time.sleep(3)
driver.switch_to.window(Win[0])
driver.find_element_by_xpath("""//*[@id="Tabbed"]/a/button""").click()
Win1 = driver.window_handles
print(Win1)
print(len(Win1))
driver.switch_to.window(Win1[2])
print(driver.title)
driver.quit()
