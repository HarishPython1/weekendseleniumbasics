from pages.webgeneric import WebGeneric
from testdata.ExcelUtil import *


class SelectDemoPage(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        self.day = "day"
        self.month = "month"
        self.year = "year"
        global wb
        wb = WebGeneric(driver)

    def select_day(self):
        wb.select_drp_down_by_visible_text("id",self.day,"10")

    def select_month(self):
        wb.select_drp_down_by_visible_text("id", self.month, "May")

    def select_year(self):
        wb.select_drp_down_by_visible_text("id", self.year, "2010")


