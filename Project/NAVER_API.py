import requests

from week2.ex_crawling.bs4_cgv import title


def get_naver(query):
    s = 1
    url = "https://openapi.naver.com/v1/search/encyc.json?query={0}&start={1}&display=100".format(query,s)
    CLIENT_ID = "r80vcnBCMritWH12NS2_"
    SECRET = "AT8ZXK7FNW"
    header = {"X-Naver-Client-Id": CLIENT_ID
             ,"X-Naver-Client-Secret":SECRET}
    res = requests.get(url, headers=header)
    json_data = res.json()
    return json_data
print(get_naver("강아지"))
lis = get_naver("강아지")
items = lis['items']
for item in items:
    print(item)