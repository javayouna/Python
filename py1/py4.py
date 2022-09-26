from random import *
#반복문 + 조건문
array = [9,12,17,22]

'''
#for문 if문 사용할 때 들여쓰기 주의해야함 
for a in range(0,30):
  if a in array: #array[a]할 경우 인덱스값이 없는 부분도있어서 문법 오류발생
      print(a) 
      continue #조건에 맞을경우 ++적용되어 다음 반복문이 실행됨
        #break 해당조건이 맞으면 반복문 빠져나옴 
'''

'''
for b in range(0,30):
    if b in array: #배열갑소가 반복되는 값이 같을 때 
        if b > 20: #그외 100이상의 값이 될 경우
            break  #반복문 정지
        else: 
            print(b) #조건에 맞는 부분 출력
'''

w=0
while True: #무한루프
    if w in array:
       if w<30:
           print(w)
           w+=1 #무한 loop에선 w++를 별도로 사용않음 +1씩 강제증가
    else:
        w+=1
        if w > 30: #무한 loop지만, 30이상이면 종료
            print(w)
            break
            
            