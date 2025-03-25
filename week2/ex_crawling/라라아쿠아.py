from bs4 import BeautifulSoup
from matplotlib.image import thumbnail
from selenium import webdriver
from selenium.webdriver.common.by import By
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
lis = div.find_all('li')
img_set = set()
for li in lis:
    tnail = li.select_one('div.thumbnail')
    t_a = tnail.select_one('a')
    img = t_a.select_one('img')
    print(img['src'])
    # # img_set.add(img['src'])
    # description = li.select_one('div.description')
    # name = description.select_one('div.name')
    # span = name.select_one('span.title displaynone')
    # text = span['text']
    # print(text)


