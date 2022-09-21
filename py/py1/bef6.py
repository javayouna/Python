from bs4 import BeautifulSoup  
from requests import *

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
print(tr)
#for aa in span:
#    print(aa.get_text())

#print(atag)
#print(cartoon.a.get_text())