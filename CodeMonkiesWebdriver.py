
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0")
driver = webdriver.PhantomJS(desired_capabilities=dcap)
driver.get('https://www.playcodemonkey.com/users/sign_in')
print (driver.title)

username = driver.find_element_by_id("loginForm_login")
password = driver.find_element_by_id("loginForm_password")


username.send_keys('FIX')
username.send_keys(Keys.TAB)
password.send_keys('FIX')


driver.find_element_by_id('login-btn').click()
print(driver.current_url)
print (driver.title)
driver.get('https://www.playcodemonkey.com/home')
print(driver.current_url)
print (driver.title)
