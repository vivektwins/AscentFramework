import unittest
from page_folder.UL import ULone
from generic.path import *
from ascent_logging import custom_logger as cl
import logging
import pytest
 


@pytest.mark.usefixtures("oneTimeSetUp", "setUp","folder")
class ValidLogin(unittest.TestCase):

    #log = cl.customLogger(logging.DEBUG)
    log = cl.customLogger('false', logging.DEBUG)
    log.info("-------------------------------START--------------------------------------")
    log1 = cl.customLogger('true', logging.DEBUG)

    @pytest.fixture(autouse=True)
    def setup(self):
        self.u1 = ULone(self.driver)

    @pytest.mark.run(order=1)
    def test_methods(self):
        self.ul = ULone(self.driver)
        self.ul.enter_ucode("name")
        #self.ul.enter_name()
        #self.ul.enter_description("test")
        #self.ul.enter_manufacturername()
        #self.ul.enter_plus()
        #self.ul.enter_manufacturercompany()
        #self.ul.enter_manufacturerdivision()
        #self.ul.enter_brand()
        #self.ul.enter_dosageform()
        #self.ul.enter_packform()
        #self.ul.enter_nfc()
        #self.ul.enter_composition()
        #self.ul.enter_pack()
        #self.ul.enter_Hsn()
        #self.ul.enter_mrp("0.5")
        #self.ul.enter_schedule()
        #self.ul.enter_storage()
        #self.ul.enter_productcategory()
        #self.ul.enter_launch()
        #self.ul.enter_flavourvraiantflag()
        #self.ul.enter_flavourtype()
        #self.ul.enter_submit()
        #self.ul.press_cancel()
        #self.ul.continue_popup()
        #self.ul.enter_popup_text()
        #self.ul.user_profile()
        #self.ul.enter_logout()






