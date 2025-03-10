import csv
date_list = []
with open('paxnet.csv', mode='r', encoding='utf8') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader :
        date_list.append(row)
print(date_list)
for v in date_list : 
    url = f'https://www.paxnet.co.kr/tbbs/view?id=N10841&seq={v[0]}' # 키
    print(v[1]) # 데이터
    print(url)