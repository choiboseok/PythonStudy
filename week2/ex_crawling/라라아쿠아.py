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
    if tnail:
        t_a = tnail.select_one('a')
        img = t_a.select_one('img')
        img_set.add(img['src'])
        print(img['src'])
        description = li.select_one('div.description')
        name = description.select_one('div.name')
        name_a = name.select_one('a')
        span = name_a.find_all('span')
        print(span[2].text)

img_dir = os.path.join('./', '라라아쿠아사진') # 검색명으로 폴더
if not os.path.exists(img_dir) :
    os.mkdir(img_dir)
for i, v in enumerate(img_set):
    file = os.path.join(img_dir, str(i) + '.png')
    try :
        req.urlretrieve(v, file)
    except Exception as e:
        print(str(e))
print("저장완료")