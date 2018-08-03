from generic import base_page
from generic.base_page import BasePage
from generic.locators import Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time


class AccountMStump(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    hostlogin = 'login-host'
    email = 'email' #id
    password = 'password' #id
    submit = 'btn-success'
    back = 'login-back-button'
    Menu_bar = 'dropdown'
    Account_Management_sub = 'dashboard-link'
    Active = '[aria-controls="Active"]' #css
    Deactivated = '[aria-controls="Deactivated"]' #CSS
    Wait = '[aria-controls="Wait"]'



    def login(self,email,password):
        self.elementClick(self.hostlogin, locatorType="class")
        self.sendKeys(data=email, locator=self.email, locatorType="id")
        self.sendKeys(data= password, locator= self.password, locatorType="id")
        self.elementClick(self.submit,locatorType="class")
        time.sleep(2)

    def menu(self):
        self.elementClick(self.Menu_bar, locatorType='class')
        time.sleep(2)
    def Acc(self):
        self.elementClick(self.Account_Management_sub,locatorType='class')
        time.sleep(2)
    def active(self):
        self.elementClick(self.Active, locatorType='CSS')
        time.sleep(2)
    def deact(self):
        self.elementClick(self.Deactivated,locatorType='CSS')

    def wait(self):
        self.elementClick(self.Wait, locatorType='CSS')
        time.sleep(2)


