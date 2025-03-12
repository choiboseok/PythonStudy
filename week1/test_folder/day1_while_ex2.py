import random
# 업다운 게임
# 3번의 기회
# 사용자 입력이 맞으면 '정답', '작으면 '업', 크면 '다운' 출력
# 틀릴때 마다 몇번의 기회가 있는지 출력
# computer의 랜덤 값은 1 ~ 10 사이의 정수

computer = random.randint(1,10)

for i in range(3, 0, -1):
    sel = int(input("숫자 입력:"))
    if sel > computer :
        print("다운")
        print("남은 기회", i-1)
    elif sel < computer :
        print("업")
        print("남은 기회", i-1)
    elif sel == computer :
        print("정답")
        break
print("정답은 ", computer)