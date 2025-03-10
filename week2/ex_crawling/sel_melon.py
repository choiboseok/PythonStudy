from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
url = 'https://www.melon.com/chart/index.htm'
# 406 코드
# res = requests.get(url) # 단순 get 방식 불가
# soup = BeautifulSoup(res.content, 'html.parser')  # 406 코드
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)
time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
tbody = soup.find('tbody')
trs = tbody.find_all('tr')
for tr in trs :
    tds = tr.find_all('td')
    rank = tds[1].select_one('span.rank').text
    a_tags = tds[5].find_all('a')
    title = a_tags[0].text
    singer = a_tags[1].text
    print(title, singer)