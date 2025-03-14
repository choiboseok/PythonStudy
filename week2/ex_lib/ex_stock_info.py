import pandas as pd
from week2.ex_db.DBManager import DBManager
db = DBManager()
# 엑셀 읽어오기
# query
krx_df = pd.read_excel("krx.xlsx", engine="openpyxl")
print(krx_df.head())
for i, row in krx_df.iterrows():
    print(f"{i}:{row['Name']}-{row['Code']}")
    # DB에 저장
    # conn = db.get_connection()
    # if conn:
    db.insert("INSERT INTO tb_krx(krx_code, krx_name, krx_market, krx_volume) VALUES(:1, :2, :3, :4)"
              , [row['Code'], row['Name'], row['Market'], row['Volume']])