from selenium import webdriver
import time
import img_util

url = "https://getbootstrap.kr/"
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)
time.sleep(1)
driver.get_screenshot_as_file("boot.png")
img_util.fullpage_screenshot(driver, "boots.png")
driver.close()