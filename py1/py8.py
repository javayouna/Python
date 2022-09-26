#편의성 및 함수이동 방법

#0001 0002 0003
for number in range(1,30): #range 는 이상 미만
    print("대기번호 "+str(number).zfill(4))
#zfill:자동으로 숫자 자리수 맞추는 함수

#3자리마다 ,로 출력
money = 10000000000
print("{0:,}".format(money))

#함수이동
def abc():
    bbb()
def bbb():
    print("함수이동으로 값을 출력")   
abc()