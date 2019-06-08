import time

from selenium import webdriver

from pages.selectdemopge import SelectDemoPage
from testdata.data import *
from pages.loginpage import LoginPage
from pages.homepage import HomePage
import pytest
from pages.jqueryloginpage import Jquery_LoginPage

@pytest.mark.usefixtures("test_setup")
class TestSelectDemo:
    def test_drag(self):
        driver = self.driver
        sdp = SelectDemoPage(driver)
        sdp.select_day()
        sdp.select_month()
        sdp.select_year()
        time.sleep(5)