import selenium
from selenium import webdriver

driver = webdriver.Ie("C:\\Users\\srikar\\PycharmProjects\\Drivers\\IEDriverServer.exe")
driver.get("https://admin-demo.nopcommerce.com/")
driver.implicitly_wait(10)
driver.maximize_window()
driver.quit()
