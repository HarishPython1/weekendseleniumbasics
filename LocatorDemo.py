from selenium import webdriver

driver=webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("http://facebook.com")
driver.find_element_by_xpath("//input[contains(@id,'_j')]").send_keys("First Name")
driver.find_element_by_name("lastname").send_keys("Last Name")
driver.find_element_by_xpath("//input[@aria-label='Mobile number or email address']").send_keys("999999999")