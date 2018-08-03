from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pytest

class test:

    def __init__(self):

     driver = webdriver.Chrome("C:\\Users\\Hasher\\PycharmProjects\\Ascent_MDM")

     driver.get('http://mdmweb-dev.ahwspl.net/login')

     driver.find_element_by_id('username').send_keys('UL1')
     driver.find_element_by_id('password').send_keys('admin@123')
     driver.find_element_by_class_name('mat-button-wrapper').click()
     time.sleep(5)

     driver.find_element_by_xpath('//a[@href="/user-level-1"]').click()



     select = Select(driver.find_element_by_id('mat-input-1'))

# select by visible text
     select.select_by_visible_text('3A PHARMACEUTICALS')

# select by value
#select.select_by_value('1')


# def __init__(self, driver):
#     self.driver = driver
#
#
# def getByType(self, locatorType):
#     locatorType = locatorType.lower()
#     if locatorType == "id":
#         return By.ID
#     elif locatorType == "name":
#         return By.NAME
#     elif locatorType == "xpath":
#         return By.XPATH
#     elif locatorType == "css":
#         return By.CSS_SELECTOR
#     elif locatorType == "class":
#         return By.CLASS_NAME
#     elif locatorType == "link":
#         return By.LINK_TEXT
#     else:
#         self.log.info("Locator type " + locatorType + " not correct/supported")
#     return False
#
#
# def getElement(self, locator, locatorType="id"):
#     element = None
#     try:
#         locatorType = locatorType.lower()
#         byType = self.getByType(locatorType)
#         element = self.driver.find_element(byType, locator)
#         self.log.info("Element Found with locator: " + locator + " and  locatorType: " + locatorType)
#     except:
#         self.log.info("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
#     return element
#
#
def getDropdown(self, locator="", locatorType="id", droptext=""):
    element = None
    try:
        locatorType = locatorType.lower()
        byType = self.getByType(self, locatorType)
        element = Select(self.driver.find_element(byType, locator))
        self.webScroll(self, direction='')
        for droptext in element.find_elements_by_tag_name(''):
            if droptext.text == '':
                droptext.select_by_visible_text('')
            break

        self.log.info("Element Found with locator: " + locator + " and  locatorType: " + locatorType)
    except:
        self.log.info("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
    return element

    return droptext
