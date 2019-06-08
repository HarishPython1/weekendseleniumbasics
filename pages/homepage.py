from pages.webgeneric import WebGeneric


class HomePage(WebGeneric):
    def __init__(self, driver):
        # self.driver = driver
        WebGeneric.__init__(self, driver)
        self.logout = "//*[text()='log out']"
        global wb
        wb = WebGeneric(driver)

    def logout_acti(self):
        # self.driver.find_element_by_xpath(self.logout).click()
        wb.click("xpath", self.logout)
