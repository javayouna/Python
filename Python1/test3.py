# + / - *
# 산술연산 기호 및 결과값 출력
# print(10%3) #나머지 구하는 연산기호
# print(10/3) #소수점도 출력되는 나누기
# print(10//3) #소수점출력없이 정수로 출력
# print(2*3) #곱하기
# print(2**3) # ** = ^ , 2^3 
#부등호 <,>,<=,>=,==
# print(10+30==50) 
# print(10 != 20)#True
# print(not 10 != 20) #not이 들어갔으므로 부정. 원래 결과와 반대로 뜸 . False
'''
# and : 그리고. 두 조건이 모두 맞아야 true 출력됨. and == & (java에선 &&로 기호2개사용하지만 파이썬은 1개만 사용함.)
print((10 > 5) and (4<5)) #True
print((10>5) and (4>5)) #False
print((10>5) & (4<5)) #True
#or : or == | 
print((10>5) or (4>5)) #True
print((10>5) | (4>5)) #True
'''
#여러개를 한꺼번에 비교하여 전체가 모두 맞을경우 True, 그 외에는 False가 출력됩니다.
print(10>20>30) #False
print(3>2>1) #True

#괄호 부분에 포함된 산술연산 부터 실행
print(10+20*10)
print((10+20)*10)
num=(10+20)*10
print(num)

#증가, 감소, 곱하기, 나누기(+=,-=,*=,/=)
# jum = 5
jum += 4 
print(jum)