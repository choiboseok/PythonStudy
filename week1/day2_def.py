# 함수 선언 def
def adder(a, b):
    sum = a + b
    return sum

print(adder(2, 10))

# return 0 ~ n개 가능
def return_test() :
    print("리턴 없음")
return_test()

def return_test2():
    return 10, True, "aa"
val = return_test2()
print(val, type(val)) # 튜플 타입
re1, re2, re3 = return_test2()
print(re1, type(re1))
print(re2, type(re2)) ## 각각의 객체 타입

# 디폴트 매개변수
def fn_default(nm, level=1) :
    print(nm, level)

fn_default("팽수")
fn_default("동수", 100)

# 가변 매개변수(0~n개)
def fn_calc(operator, *args) : # args - 가변길이 매개 변수 사용시 * 표시
    result = 0
    if operator == '+' :
        for n in args :
            result += n
    elif operator == '*' :
        result = 1
        for n in args :
            result *= n
    return result
print(fn_calc('+', 1, 2, 3, 4, 5))
print(fn_calc('+'))
print(fn_calc('*', 2, 10))