import pandas as pd
import requests
import json
from week2.ex_db.DBManager import DBManager
db = DBManager()
sql_merge = '''
MERGE INTO stock_bbs a
USING DUAL 
ON(a.rsno = :rsno   
    AND a.discussion_id = :discussion_id
    AND a.item_code = :item_code) 
WHEN MATCHED THEN
    UPDATE SET a.read_count = :read_count
                , a.good_count = :good_count
                , a.bad_count = :bad_count
                , a.comment_count = :comment_count
                , a.update_date = SYSDATE
WHEN NOT MATCHED THEN
    INSERT (a.rsno, a.discussion_id, a.item_code, a.title, a.bbs_contents, a.writer_id, read_count
            , a.good_count, a.bad_count, a.comment_count, a.end_path, a.update_date)
    VALUES (:rsno, :discussion_id, :item_code, :title, :bbs_contents, :writer_id, :read_count
            , :good_count, :bad_count, :comment_count, :end_path, TO_DATE(:update_date, 'YYYY-MM-DD HH24:MI:SS'))

'''

# # db 에서 krx_yn 이 Y인 종목만 요청
# sql = '''SELECT * FROM tb_krx WHERE krx_yn=:1'''
# rows = db.select(sql, ['Y'])
# for row in rows:
#     print(row)

def get_bbs(code):
    # code = "005930"
    url = f"https://m.stock.naver.com/front-api/discuss?discussionType=localStock&itemCode={code}&size=100"
    res = requests.get(url)
    json_data = json.loads(res.text)
    for v in json_data['result']:
        row = {
            "rsno": v["rsno"]
            , "discussion_id": v["discussionId"]
            , "item_code": v["itemCode"]
            , "title": v["title"]
            , "bbs_contents": v["contents"][:1300]
            , "writer_id": v["writerId"]
            , "read_count": v["readCount"]
            , "good_count": v["goodCount"]
            , "bad_count": v["badCount"]
            , "comment_count": v["commentCount"]
            , "end_path": v["endPath"]
            , "update_date": v["date"][:19]
        }
        try:
            print(row)
            db.insert(sql_merge, row)
        except Exception as e:
            print(str(e))
        # {'rsno': -298111477, 'discussionId': 298111477, 'type': 'localStock', 'itemCode': '069080', 'replyDepth': 0
        # , 'title': 'kys6가 병관씨에게'
        # , 'contents': '칼부림 \r<br>명장면\r<br>볼수 없는건가?\r<br>현재는\r<br>kys6\r<br>'
        # , 'writerId': 'yell****', 'date': '2025-03-02 14:16:25.0',
        # 'readCount': 40, 'goodCount': 1, 'badCount': 7, 'commentCount': 0, 'itemName': '웹젠'
        # , 'endPath': '/domestic/stock/069080', 'isHolding': False, 'isHideCleanbot': False}

if __name__ =='__main__':
    db = DBManager()
    conn = db.get_connection()
    select_sql= '''
                SELECT krx_code
                    , krx_name
                    , krx_market
                FROM tb_krx
                WHERE krx_yn = 'Y'
    '''
    df = pd.read_sql(con=conn, sql=select_sql)
    print(df.head())
    for i, v in df.iterrows():
        code = v['KRX_CODE']
        get_bbs(code)
    print("완료")
    # get_bbs('069080')