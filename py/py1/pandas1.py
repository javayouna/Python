import pandas as pd
#Series => Time, Num, Data (간격에 맞춰서 배치된 데이터)
data = pd.Series([10,20,30,40]) #Series로 배열값 로드 (인덱스 자동 설정)
print(data)

#index 기본 숫자 (0 부터 시작) 데이터 인덱스 이용해서 이름 지정가능함
data2 = pd.Series([17,19,20,17,16,15,16],index=['월','화','수','목','금','토','일'])
print(data2)
print(data2['토']) #지정된 index 별명 출력할 수 있음

array={
    "username": ['홍길동','이순신','강감찬'],
    "userage": ['30','46','27'],
    "usercp":['SKT','KT','KT']
    }


#일반 python 배열 출력
print(array['username'])
print(type(array))

#DataFrame이용해서 키가있는 배열 시각화
pr=pd.DataFrame(array)
print(pr)
print(pr['username'][2])

#원하는 키 데이터 시각화
print(pr[['username','usercp']]) 

#키배열 index명 변경
pr2=pd.DataFrame(array, index=['no1','no2','no3'])
print(pr2)

#컬럼 위치 변경 
pr3=pd.DataFrame(array, columns=['usercp','username','userage'])
print(pr3)

