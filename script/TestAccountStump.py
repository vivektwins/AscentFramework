import unittest
from page_folder.Stump_accountManagement import AccountMStump
from generic.path import *
from ascent_logging import custom_logger as cl
import logging
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp", "folder")
class testacc (unittest.TestCase):
    # log = cl.customLogger(logging.DEBUG)
    log = cl.customLogger('false', logging.DEBUG)
    log.info("-------------------------------START--------------------------------------")
    log1 = cl.customLogger('true', logging.DEBUG)

    @pytest.fixture(autouse=True)
    def setup(self):
        self.st = AccountMStump(self.driver)

    @pytest.mark.run(order=1)
    def test_methods(self):
        self.st = AccountMStump(self.driver)
        self.st.login('vivekkumam26@gmail.com','!321Shoot')
        self.st.menu()
        self.st.Acc()
        self.st.active()
        self.st.deact()
        self.st.wait()
