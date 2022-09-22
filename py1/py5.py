from random import *
#2*1~ 3*9까지 출력

for x in range(2,4):
    for y in range(1,10):
        print(x, '*', y, '=', x*y)
        if(y==9):
            print('-------')
            
            
data = [2,6,7,3,1]
print(data)
data=[i+5 for i in data] #배열값에 +산술식 새로운 배열
print(data)

#다양한 형태로 배열값 전환
person = ['kim','part','lee']
person=['#'+aa for aa in person]
#person = [aa.upper() for aa in person]
print(person)