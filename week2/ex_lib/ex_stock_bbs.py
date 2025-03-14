import requests
import json
from week2.ex_db.DBManager import DBManager
db = DBManager()

# db 에서 krx_yn 이 Y인 종목만 요청
sql = '''SELECT * FROM tb_krx WHERE krx_yn=:1'''
rows = db.select(sql, ['Y'])
for row in rows:
    print(row)

def get_bbs(code):
    code = "005930"
    url = f"https://m.stock.naver.com/front-api/discuss?discussionType=localStock&itemCode={code}&size=100"
    res = requests.get(url)
    json_data = json.loads(res.text)
    for v in json_data['result']:
        print(v)