# pip install bs4
from bs4 import BeautifulSoup
import requests

url = "https://smartstore.naver.com/tmakxmdjgkd/category/b4ebc078ffd84464a25c7bf7a4c836f4?cp=1"
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser') # html 형식으로 변경
print(soup.prettify()) # 구조화되게 출력

ul_all = soup.find_all('ul', string=True) # text가 있는 a 태그만
for ul in ul_all :
    print(ul)