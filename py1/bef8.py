from bs4 import BeautifulSoup  
from requests import * 
from re import * #정규식
from random import * #랜덤
from csv import *
from lib2to3.fixer_util import Newline

filenm="kospi.csv"
f=open(filenm,"w",encoding="euc-kr",newline="") 
#csv파일 저장할 때 한글깨지는 거 방지
#newline:csv데이터 등록할 때 한칸 띄어쓰기 될때가 있는데..!이거사용하면댐
writer=writer(f)

url="https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0"
web=get(url)
web.raise_for_status()

html=BeautifulSoup(web.text,"lxml")
table=html.find("table",attrs={"class":"type_2"})
tbody=table.find("tbody")
tr=tbody.find_all("tr")
for data in tr:
    td = data.find_all("td")
    data = [text.get_text() for text in td]
    
    if len(data) <= 1:
        continue
    
    else:
        company = data[1]
        price=data[2].strip().replace(",","")
        face=data[5].strip().replace(",","")
        print(company,price,face)
        #writerow:엑셀기준 , 다음칸으로 적용
        #writer.writerow(company)
        #writer(company)
        rowdata=[company,price,face] #배열로 생성해야한 csv에서 행,열 인식됨
        writer.writerow(rowdata)
        #f.write(company,price,face)