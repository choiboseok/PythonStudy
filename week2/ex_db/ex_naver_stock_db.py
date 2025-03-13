import requests
import json
import cx_Oracle
from DBManager import DBManager

mydb = DBManager()
# conn = mydb.get_connection()
conn = cx_Oracle.connect("member", "member", "localhost:1521/xe")
sql = """
    INSERT
    INTO tb_stocks(item_code, close_price)
    VALUES(:1, :2)
"""
for page in range(1, 25):
    url = f"https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page={page}&pageSize=50"
    res = requests.get(url)
    if res.status_code == 200:
        stocks = json.loads(res.text)['stocks']
        for stock in stocks:
            cur = conn.cursor()
            mydb.insert(sql, [stock['itemCode'], stock['closePrice'].replace(',','')])
conn.commit()
# for row in rows:
#     print(row)
conn.close()
# tb_stocks
# item_code, close_price, update_date(default sysdate)