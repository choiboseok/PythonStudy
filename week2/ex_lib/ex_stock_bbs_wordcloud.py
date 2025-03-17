import pandas as pd
from week2.ex_db.DBManager import DBManager
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
sql = '''
    SELECT *
    FROM stock_bbs
'''
db = DBManager()
conn = db.get_connection()
df = pd.read_sql(con=conn, sql=sql)
okt = Okt()
nouns = []
for i, v in df.iterrows():
    content = v["BBS_CONTENTS"].strip()
    # 1. 명사 추출
    list =okt.nouns(content)
    nouns += list
    # 2. 단어 카운트 생성
count = Counter(nouns)
# 3. 워드 클라우드 생성
cloud = WordCloud(font_path='../../dataset/NanumGothicBold.ttf', width=800, height=400, background_color='white')
gen = cloud.generate_from_frequencies(count)
plt.figure(figsize=(10, 5))
plt.imshow(cloud)
plt.axis("off")
plt.show()