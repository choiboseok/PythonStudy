import requests
from bs4 import BeautifulSoup
import csv

def get_paxnet(page):
    url = f'https://www.paxnet.co.kr/tbbs/list?tbbsType=L&id=N10841&page={page}'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    ul = soup.select_one('#comm-list')
    lis = ul.find_all('li')
    data_rows = []
    for i, li in enumerate(lis): # 인덱스 활용
        if i != 0 :
            seq = li.select_one('.type')
            if seq : # 해당 객체가 있는가를 뜻함
                seq_num = seq.get('data-seq')
                title = li.select_one('.title').select_one('.best-title').text
                data_rows.append([seq_num, title])
    with open('paxnet.csv', 'a', encoding='utf8', newline='') as f:
        write = csv.writer(f, delimiter='|')
        write.writerows(data_rows) # rows 로 배열에 있는 내용 전부 저장

if __name__ == '__main__':
    for p in range(1, 11) :
        get_paxnet(p)