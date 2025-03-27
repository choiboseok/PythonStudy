from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request as req
import requests
import time
import os

img_path = '../week2/ex_crawling/testimg'
if not os.path.exists(img_path):
    os.mkdir(img_path)

query = '세진아쿠아리움'
i=1
option = webdriver.ChromeOptions()
option.add_argument('--headless')
img_set = set()
while True:
    url = url = f'https://seijin.co.kr/goods/goods_list.php?page={i}&cateCd=002'
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(3)
    driver.get(url)
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    div = soup.select_one("div.item_gallery_type")
    lis = div.find_all('li')
    if lis ==[]:
        print('수집종료')
        break
    for li in lis:
        photo = li.select_one('.item_photo_box')
        p_a = photo.select_one('a')
        img = p_a.select_one('img')
        img_set.add(img['src'])
        info = li.select_one('.item_info_cont')
        i_a = info.select_one('a')
        name = i_a.select_one('strong.item_name')
        print(img['src'])
        print(name.text)
        print("-"*100)
    print(i, "페이지 끝")
    # page 값 증가
    i += 1

# 이미지 저장
img_dir = os.path.join('../week2/ex_crawling/', '세진아쿠아어항사진') # 검색명으로 폴더
if not os.path.exists(img_dir) :
    os.mkdir(img_dir)
for i, v in enumerate(img_set):
    file = os.path.join(img_dir, str(i) + '.png')
    try :
        req.urlretrieve(v, file)
    except Exception as e:
        print(str(e))
print("저장완료")
