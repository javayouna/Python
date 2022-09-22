from random import *
#random 라이브러리(random,randrange,randint < range (여러개))

#set,list
user = range(1,21) #1~20까지 데이터 그냥 순서대로만 나옴
#range 배열 범위 데이터 생성하는 클래스
user=list(user) 
#list나 set에담아야함
print(user)
shuffle(user) #배열값을 섞음
print(user)
#random => sample 1개이상 값 가져올 때 
lotto=sample(user,6) #sample(배열명,출력나올개수)
print(lotto)

print("1등 당첨번호:  "+str(lotto[0]))
print("1등 당첨번호:  {0}".format(lotto[0])) #배열의0번째
print("보조 당첨번호: {0}".format(lotto[1:]))
