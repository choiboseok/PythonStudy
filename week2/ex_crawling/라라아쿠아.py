from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request as req
import requests
import time
import os
img_path = './testimg'
if not os.path.exists(img_path):
    os.mkdir(img_path)

url = 'https://raraaqua.com/category/%ED%81%AC%EA%B8%B0%EB%B3%84-%EC%88%98%EC%A1%B0/615/'
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)
time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
div = soup.select_one("div.ec-base-product")
uls = div.select_one('ul.prdList grid5')
print(uls)


# ul = soup.select_one('ul.wOWfwtMC_3 _3cLKMqI7mI')
# lis = ul.select_one('li')
# for li in lis :
