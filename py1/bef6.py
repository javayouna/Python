from bs4 import BeautifulSoup  
from requests import *
#해당 사이트에 접속하여 Devtool로 볼 경우 데이터가 확인이 되지만 
#실제 크롤링 후 스크래핑시 데이터가 확인이 안 될 경우는 AJAX 및 자바 스크립트로 직접 태그가 생성되도록 제작 되었음.
#이럴경우 스크래핑 하기가 어려워짐
url="https://www.koreabaseball.com/TeamRank/TeamRank.aspx"
result=get(url) 
result.raise_for_status()
#print(result.raise_for_status()) 
#status코드에 문제사항 출력 None(문제없음)
html = BeautifulSoup(result.text,"lxml")
#lxml자동 파서 
baseball = html.find("div",attrs={"id":"cphContents_cphContents_cphContents_udpRecord"})
team=baseball.find("tbody")
tr=team.find_all("tr")
w=0
for aa in tr:
    td=tr[w].find_all("td")
    print(td[1].get_text())
    w+=1
#for aa in span:
#    print(aa.get_text())

#print(atag)
#print(cartoon.a.get_text())