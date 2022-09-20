#절대값 구하기
print(abs(-100)) #음수를 양수로 무조건 변경
print(pow(2,3)) #^제곱근 표
print(max(5,1)) #가장  값
print(min(5,1)) #가장 작은 값

#abs는 배열형태로 수정 후 양수로 변경 가능 그외 방식은 사용하지않음
print(max(1,5,8,7,11,3,6))

#round:반올림0.5단위
print(round(3.74)) #4
print(round(3.11)) #3

#round외에 모듈 사용하는 경우 (floor, ceil)
from math import *
print(floor(3.74))
print(ceil(3.74))

#문법에 math없이 사용하는 방식 (floor, ceil)
import math
print(math.floor(3.74))
print(math.ceil(3.74))

from random import *
print(random()*10) #소수점 나옴
print(int(random()*10)) #(정수) 0~10 미만의 임의값 생성
print(int(random()*10)+1) #(정수) 1~10 이하의 임의값 생성

print(randrange(1,10)) #1~10미만의 임의값 생성
print(randint(1,2)) #1~2까지 임의값 생성

#문자열을 출력하는 방식
msg="""홍길동님 환영합니다.
적립금은 2500원 사용할 수 있습니다"""
print(msg)
