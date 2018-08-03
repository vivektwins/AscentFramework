from generic.base_page import BasePage
from generic.locators import Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time


class ULone(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.main_window = self.driver.window_handles[0]

    username = 'username'
    password = 'password'
    loginbutton = 'mat-button-wrapper'
    createrequest = '[ng-reflect-router-link="/user-level-1/"]'
    errormsg= 'modal-content-text'
    title= 'Master Data Management'
    ucode= '[ng-reflect-name="ucode"]'
    name ='[ng-reflect-name="name"]'
    description ='[ng-reflect-name="description"]'
    manufacturername= '[ng-reflect-name="manufacturer"]'
    manufacturercompany= '[ng-reflect-name="company"]'
    manufacturerdivision= '[ng-reflect-name="manufacture_division"]'
    brand= '[ng-reflect-name="brand"]'
    dosage= '[ng-reflect-name="dosage_form"]'
    packform = '[ng-reflect-name="pack_form"]'
    nfc= '[ng-reflect-name="nfc_l1"]'
    composition= '[ng-reflect-name="composition"]'
    pack= '[ng-reflect-name="pack"]'
    hsn='[ng-reflect-name="hsn_sac"]'
    mrp = '[ng-reflect-name="mrp"]'
    schedule = '[ng-reflect-name="schedule"]'
    storagecon = '[ng-reflect-name="storage_condition"]'
    productcate= '[ng-reflect-name="product_category"]'
    launch = '[ng-reflect-name="launch_date"]'
    flavourVariant = '[ng-reflect-name="flavour_variant_flag"]'
    flavourtype = '[ng-reflect-name="flavour_type"]'
    submit = 'success-btn'
    contin_popup = '//*[contains(@class,"action-btns")]//button[2]'
    okay_created = '//*[contains(@class,"ok-btn")]//button[1]'
    popup_text= 'modal-heading'
    cancelButton = '//*[contains(@class,"action-btns")]//button[1]'
    userclick = 'p-0'
    logout = '//*[contains(@class,"mat-menu-content")]//button[4]'
    plus = 'add'


    def enter_username(self, email):
        self.sendKeys(data=email, locator=self.username, locatorType="id")

    def enter_password(self, _password):
        self.sendKeys(data=_password, locator=self.password, locatorType="id")

    def click_login(self):
        self.elementClick(self.loginbutton, locatorType="class")

    def login(self, email="", _password = ""):
        self.enter_username(email)
        self.enter_password(_password)
        self.click_login()

    def create_request(self):
         self.elementClick(self.createrequest, locatorType="CSS")


    def verifylogin(self):
        if self.title in self.getTitle():
            return True
        else:
            return False

    def enter_ucode(self, data=""):
        self.text = self.sendKeys(data, self.ucode,locatorType = "CSS")

    def enter_name(self):
        self.dropdown_click_option(self.name, "1 2 3 100 MG TABLET 4", type='CSS')


    def enter_description(self, data=""):
        self.sendKeys(data, self.description, locatorType ="CSS")

    def enter_manufacturername(self):
        self.dropdown_click_option(self.manufacturername, "3 CUBE", type='CSS')

    def enter_plus(self):
        self.plusClick(self.plus,locatorType="link")

    def enter_manufacturercompany(self):
        self.dropdown_click_option(self.manufacturercompany, "3 CUBE" ,type='CSS')

    def enter_manufacturerdivision(self):
        self.dropdown_click_option(self.manufacturerdivision, "3D" ,type='CSS')

    def enter_brand(self):
        self.dropdown_click_option(self.brand, "Test Brand" ,type='CSS')

    def enter_dosageform(self):
        self.dropdown_click_option(self.dosage, "BLADE" ,type='CSS')

    def enter_packform(self):
        self.dropdown_click_option(self.packform, "BOTTLE" ,type='CSS')

    def enter_nfc(self):
        self.dropdown_click_option(self.nfc, "K-ORAL TOPICAL",type='CSS')

    def enter_composition(self):
        self.dropdown_click_option(self.composition, "1,3-BUTANEDIOL+2-PHENOXYETHANOL+CHLORPHENESIN+CITRIC ACID" ,type='CSS')

    def enter_pack(self):
        self.dropdown_click_option(self.pack, "0.2 ML" ,type='CSS')

    def enter_Hsn(self):
        self.dropdown_click_option(self.hsn, "HSN Code Test" ,type='CSS')
       # self.webScroll(self, "down")

    def enter_mrp(self, data=""):
        self.sendKeys(data, self.mrp, locatorType='CSS')

    def enter_schedule(self):
        self.dropdown(self.schedule, "SCHEDULE C",type='CSS')

    def enter_storage(self):
        self.dropdown_click_option(self.storagecon, "0⁰ TO 4⁰C",type='CSS')

    def enter_productcategory(self):
        self.dropdown(self.productcate, "Product Category" ,type='CSS')

    def enter_launch(self):
        self.dropdown(self.launch, "1",type='CSS')

    def enter_flavourvraiantflag(self):
        self.dropdown_click_option(self.flavourVariant, "NO",type='CSS')

    def enter_flavourtype(self):
        self.dropdown_click_option(self.flavourtype, "APPLE" ,type='CSS')

    def enter_submit(self):
        self.elementClick(self.submit, locatorType="class")
        time.sleep(10)

    def continue_popup(self):
        self.log.info(self.waitForElement(self.contin_popup, locatorType="class", timeout=10, pollFrequency=0.5))
        self.elementClick(self.contin_popup, locatorType="xpath")
        time.sleep(2)
        self.elementClick(self.okay_created,locatorType="xpath")
        time.sleep(5)

    def press_cancel(self):
        #window_after = self.driver.window_handles[1]
        #self.driver.switch_to_window(window_after)
        #time.sleep(10)
        self.elementClick(self.cancelButton, locatorType="xpath")
        #self.driver.switch_to_window(self.main_window)

    def enter_popup_text(self):
        self.getText(self.popup_text,locatorType= "class")

    def user_profile(self):
        self.elementClick(self.userclick, locatorType="class")
        time.sleep(2)

    def enter_logout(self):
        self.elementClick(self.logout,locatorType="xpath")
        time.sleep(5)






