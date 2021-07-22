from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://admin-demo.nopcommerce.com")
# driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
#driver.get_screenshot_as_file("test_homePageTitle.png")
driver.find_element_by_xpath("//button[contains(text(),'Log in')]").click()
time.sleep(5)
driver.find_element_by_link_text('Logout').click()
time.sleep(5)
driver.close()
