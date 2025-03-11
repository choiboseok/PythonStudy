from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request as req
import requests
import time
import os
img_path = './testimg'
if not os.path.exists(img_path):
    os.mkdir(img_path)

url = 'https://www.aquamarket.co.kr/goods/goods_list.php?cateCd=001011'
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)
time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
div = soup.select_one('div.list')
lis = div.find_all('li')
for li in lis:
    thumbnail = li.select_one('div.thumbnail')
    a_tags = thumbnail.select_one('a')
    img_src= a_tags.select_one('img')['src']
    img_title= a_tags.select_one('img')['title']
    img_file_path = os.path.join(img_path, img_src)
    req.urlretrieve(img_src, img_file_path)
    print(img_src, img_title)


# ul = soup.select_one('ul.wOWfwtMC_3 _3cLKMqI7mI')
# lis = ul.select_one('li')
# for li in lis :
