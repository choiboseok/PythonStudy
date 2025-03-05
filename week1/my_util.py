import random
from sys import flags
from traceback import print_tb

import requests

def lotto():
    '''
    로또 번호 6개 생성
    1 ~ 45 사이의 숫자
    :return: set
    '''
    lotto_num = set()
    while len(lotto_num) < 6:
        lotto_num.add(random.randint(1, 45))
    return lotto_num

# 원화 to 달러
def krw_to_usd(krw) :
    res = requests.get("https://open.er-api.com/v6/latest/USD")
    data = res.json()
    exchange_rate = data['rates']['KRW']
    return krw / exchange_rate

# 달러 to 원화 함수를 만들어주세요
def usd_to_krw(usd) :
    res = requests.get("https://open.er-api.com/v6/latest/USD")
    data = res.json()
    exchange_rate = data['rates']['KRW']
    return usd * exchange_rate

# user_lotto 함수 생성
# input : 0 ~ n 개(사용자 희망 번호)
# output : true or false, 메세지, 로또 번호(사용자 희망 번호가 포함된)
# 사용 입력 번호를 포함 시켜서 로또 번호 생성
# 단 사용자 입력은 최대 5개 까지만 포함 
# 각 사용자 입력은 1 ~ 45 사이 수
# 조건을 만족 하지 않으면 false, 만족 하면 true
# 메세지는 false일때 왜 false인지
test = (1, 14, 15)
# to List
test2 = list(test)

def user_lotto(*user_list) :
    lotto_list = list(user_list)
    if len(lotto_list) > 5 :
        lotto_list = lotto_list[:5]
        flag = True
        text = "사용자 희망 번호는 5개 까지만"
        while len(lotto_list) < 6:
            lotto_list.append(random.randint(1, 45))
        return flag, text, lotto_list
    elif len(lotto_list) == 0 :
        while len(lotto_list) < 6:
            lotto_list.append(random.randint(1, 45))
        flag = True
        text = "정상처리"
        return flag, text, lotto_list
    else:
        for i in lotto_list :
            if i > 45 :
                flag = False
                text = "1~45 사이 값만 가능"
                lotto_list = None
        return flag, text, lotto_list


# 모듈 내에서만 실행 (import에서는 사용 x)
if __name__ == '__main__':
    # print("lololottttttto")
    # print(f"달러 100은: {usd_to_krw(100)}원")
    # print(f"원화 20000은 : {krw_to_usd(20000)}달러")

    print(user_lotto(1, 2, 3, 4, 5, 6,))
    print(user_lotto(99, 2, 3))
    print(user_lotto())

