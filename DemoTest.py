from selenium import webdriver
from selenium.webdriver.support.select import Select

#executable_path="D:/driver/73/chromedriver.exe"
qspider=webdriver.Chrome()
qspider.get("http://www.facebook.com")

qspider.implicitly_wait(30)
qspider.find_element_by_name("firstname").send_keys("Harish")
qspider.find_element_by_xpath("//input[contains(@name,'lastname')]").send_keys("qspiders")
#qspider.find_element_by_xpath("//div[text()='Mobile number or email address']").send_keys("12345678")
qspider.find_element_by_name("reg_email__").send_keys("11111111")

#WORKING WITH DROPDOWN VALUES
day = qspider.find_element_by_id("day")#RETURN TYPE IS webelement
s1=Select(day)#where to select
s1.select_by_index("3")#what to select

month = qspider.find_element_by_id("month")
s2=Select(month)
s2.select_by_visible_text("Jan")


year = qspider.find_element_by_id("year")
s3=Select(year)
s3.select_by_value("2015")


