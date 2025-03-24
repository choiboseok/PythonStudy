from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request as req
import requests
import time
import os

img_path = './testimg'
if not os.path.exists(img_path):
    os.mkdir(img_path)

query = '세진아쿠아리움'

url = 'https://seijin.co.kr/goods/goods_list.php?cateCd=002031'
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)
time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
div = soup.select_one("div.item_gallery_type")
lis = div.find_all('li')
img_set = set()
for li in lis:
    photo = li.select_one('.item_photo_box')
    p_a = photo.select_one('a')
    imgs = p_a.find_elements(By.TAG_NAME, 'img')
    for v in imgs:
        if v.get_attribute('src') != None:
            img_set.add(v.get_attribute('src'))
    img = p_a.select_one('img')
    info = li.select_one('.item_info_cont')
    i_a = info.select_one('a')
    name = i_a.select_one('strong.item_name')
    print(img['src'])
    print(name.text)
    print("-"*100)


img_dir = os.path.join('./', '세진아쿠아사진') # 검색명으로 폴더
if not os.path.exists(img_dir) :
    os.mkdir(img_dir)
for i, v in enumerate(img_set):
    file = os.path.join(img_dir, str(i) + '.png')
    try :
        req.urlretrieve(v, file)
    except Exception as e:
        print(str(e))
print("저장완료")