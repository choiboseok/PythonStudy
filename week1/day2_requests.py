import requests
# 없다면 pip install requests
# http 요청을 쉽게 할 수 있는 라이브러리
# get, post, put, delete 요청 처리
# 응답 : json or text
# 요청시 자동으로 URL 인코딩 처리
# http 요청중 발생할 수 있는 오류에 대한 예외처리 제공.

url = "https://api.upbit.com/v1/market/all"
res = requests.get(url) # get 방식 url 요청
if res.status_code == 200 :
    data = res.json() # json 형태로 파싱
    for v in data :
        print(f"마켓명:{v['market']} 코인명:{v['korean_name']} ")

def fn_get_coin_price(code) :
    '''
    예)https://api.upbit.com/v1/ticker?markets=KRW-BTC
    요청하여 코인 trade_price를 리턴하는 함수
    :param code: 코인 마켓코드
    :return: price : 실시간 거래가격
    '''
    price = 0
    res = requests.get(f"https://api.upbit.com/v1/ticker?markets={code}")
    if res.status_code == 200:
        data = res.json()
        price = data[0]['trade_price'] # 하나를 받았지만 0번째 배열에 들어 있기 때문에 [위치]를 지정해 줘야 함
        # for v in data :
        #     price = v['trade_price']
    return price

print(fn_get_coin_price("KRW-BTC"))
print(fn_get_coin_price("KRW-ETH"))