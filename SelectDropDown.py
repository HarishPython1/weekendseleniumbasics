from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\Administrator\\PycharmProjects\\Framework_POM_17\\drivers\\chromedriver.exe")
driver.get("http://facebook.com")
driver.implicitly_wait(20)
driver.maximize_window()

day_element = driver.find_element_by_id("day")
select = Select(day_element)
select.select_by_visible_text("10")


month_element = driver.find_element_by_id("month")
year_element = driver.find_element_by_id("year")

select = Select(month_element)
select.select_by_visible_text("Feb")

select = Select(year_element)
select.select_by_visible_text("1998")