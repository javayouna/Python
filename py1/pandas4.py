#txt로 저장 
import pandas as pd
data = {
    "area" : ['강남구','강동구','강북구','강서구'],
    "gasoline" : [1947,1812,1677,1721],
    "diesel" : [1647,1918,1809,1855],
    "ev" : [173.8,170,158.4,166]
    }
#txt 생성할 떄 DataFrame을 무조건 선언 후 저장
pr=pd.DataFrame(data)
#txt로 저장
pr.to_csv("data.txt",encoding='euc-kr')
index=False #인덱스 번호 삭제 저장
pr.to_csv("data.txt",encoding='euc-kr',index=False)

#xls로 저장
pr.to_csv("data.xls",encoding='euc-kr',index=False)

#xlsx
pr.to_excel("data2.xlsx",index=False)
#pip install xlwt
#pip install openpyxl

