import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from seleniumbase import BaseCase

import time

'''
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

driver = webdriver.Firefox(firefox_profile=firefox_profile)

Chr = webdriver.ChromeOptions()
Chr.add_argument("--incognito")

driver = webdriver.Chrome(options=Chr)
driver = webdriver.Firefox()
driver.get("http://demo.automationtesting.in/Windows.html")
driver.implicitly_wait(10)
driver.maximize_window()
'''
class image(BaseCase):
    logoicon = 'original1.png'
    logoicon1 = 'original.png'
    def test_verifyimg(self):
        self.open("http://demo.automationtesting.in/Windows.html")
        try:
            self.assert_element(self.logoicon)
            print ("element not found")
        except NoSuchElementException:
            self.refresh()
        else:
            self.assert_element(self.logoicon1)
        finally:
            print("element found")




'''
class test_image(image):
    def test_check(self):
        self.verifyimg()
        self.assert_element(self.logoicon)
'''

'''
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
'''