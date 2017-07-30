from selenium import webdriver

driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("http://www.linkedin.com")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get_screenshot_as_file("C:\\Users\\prafulk\\PycharmProjects\\Analytics\\Screenshots\\linkedin1.png")
driver.find_element_by_id("login-email").send_keys("testemail")
driver.find_element_by_id("login-password").send_keys("testpassword")
driver.find_element_by_id("login-submit").click()
driver.get_screenshot_as_file("C:\\Users\\prafulk\\PycharmProjects\\Analytics\\Screenshots\\linkedin2.png")
driver.quit()