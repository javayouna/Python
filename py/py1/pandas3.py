#csv 저장&읽기
import pandas as pd
data = {
    "area" : ['강남구','강동구','강북구','강서구'],
    "gasoline" : [1947,1812,1677,1721],
    "diesel" : [1647,1918,1809,1855],
    "ev" : [173.8,170,158.4,166]
    }
#csv 생성할 떄 DataFrame을 무조건 선언 후 저장
pr=pd.DataFrame(data)
pr.index.name='유가리스트'
#to_csv 파일(csv)로 저장(pandas전용문법)
pr.to_csv('opinet.csv',encoding='euc-kr')