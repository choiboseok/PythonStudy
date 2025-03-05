import my_util
# import 가져온 함수를 자체적으로 있는 것 처럼 사용할수 있게 해줌''
from my_util import lotto
# 별칭 사용
from my_util import lotto as l
# help(my_util) 모듈은 알지만 사용할 함수, 방법을 모를때 사용함.
print(my_util.lotto())
print(lotto())
print(l())
