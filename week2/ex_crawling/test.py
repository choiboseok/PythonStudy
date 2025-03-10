from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time


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
    print(img_src, img_title)


# ul = soup.select_one('ul.wOWfwtMC_3 _3cLKMqI7mI')
# lis = ul.select_one('li')
# for li in lis :
