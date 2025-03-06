print("시작")
try:
    print("^^"%3)
except Exception as e:
    print(str(e))
print("종료")

def calc(valuse):
    sum = 0
    try:
        sum = valuse[0] + valuse[1] + valuse[2]
    except IndexError as a :
        print("인덱스 에러")
    except Exception as e :
        print("어떤 오류도")
    else:
        print("정상처리 일때")
    finally:
        print("무조건 처리되는")
calc([1, 2, 3]) # else, finally
calc([1, 2]) # index
calc([True, True, True]) # exception, finally
calc(None)
