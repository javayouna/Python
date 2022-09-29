from random import *
#import random as rd  #이방법도 가능 


#복습1 (phython)
#기본 무조건 배열
#파이썬 웹 서버구축 -flask
#이클립스 - Java(x)

#개발도구 - 파이썬 설치
#그 외 패키지 - pip install 패키지
#패키지 삭제 - pip uninstall 패키지
#--------------------------------#
#파이썬 변수에 자료형 없음 

abc=["a","b","c",10]
#for in(배열) while(반복문)
print("{}".format(abc[0])) #a

#import random as rd 이었을 경우에는 
#aaa=rd.randint(4,10)
aaa=randint(5,10)
print(aaa) #6

#문자열
msg="""
[이용약관]
테스트입니다.
"""
print(msg)

#문자열 세팅하는 형태
hp="010-1234-5678"
print(hp[9]) #5
print(hp[0:3]) #010
print(hp[:8]) #010-1234 >문자열처음부터 ~7까지 
print(hp[9:]) #5678 >해당 문자열부터~끝까지
print(len(hp)) #13 >문자열 개수
print(hp.replace("-","")) #01012345678
print(hp.find("<span>")) #-1 문자열있음 없음 


import re as r #findall 쓰려면 1.re import 해야함 2.변수로 받아서 배열처리
array=r.findall("1",hp)
print(array) #['1','1']



#변수값 출력
abox=3000
cbox=5000
total=f"{abox}와 {cbox} 부분 금액입니다."
print(total)

#경로 출력 \\ 2개써야함
print("c:\windows\python") #일반 문자로 출력


