from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0"
)
driver = webdriver.PhantomJS(desired_capabilities=dcap)
driver.get('https://www.ixl.com')
print (driver.title)

username = driver.find_element_by_id("qlusername")
password = driver.find_element_by_id("qlpassword")

username.send_keys("trevorforget")
password.send_keys("mathmathmath88")

driver.find_element_by_css_selector("button#qlsubmit.crisp-button.quick-login-button.site-nav-header-button").click()
wait = WebDriverWait(driver, 10)
accept = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "subLoginImg")))

driver.find_element_by_class_name('subLoginImg').click()
driver.get_screenshot_as_file('buttoncheck.png')

print(driver.current_url)
print (driver.title)
driver.get('https://www.ixl.com/analytics/student-details')
print(driver.current_url)
print (driver.title)
driver.get_screenshot_as_file('ixl.png')

