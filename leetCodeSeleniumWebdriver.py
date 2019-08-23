from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0")
driver = webdriver.PhantomJS(desired_capabilities=dcap)
driver.get('https://leetcode.com/accounts/login/')
print (driver.title)

username = driver.find_element_by_id("id_login")
password = driver.find_element_by_id("id_password")


username.send_keys('valkiron08')
password.send_keys('zZ82hdrQws4Q')


driver.find_element_by_css_selector('button.btn.btn-primary').click()
print(driver.current_url)
print (driver.title)
driver.get('https://leetcode.com/')
print(driver.current_url)
print (driver.title)
driver.get('https://leetcode.com/accounts/login/?next=/mockinterview/session/list/')
print (driver.title)
driver.get_screenshot_as_file('leetcode.png')
