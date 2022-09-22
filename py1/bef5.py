from bs4 import BeautifulSoup  
from requests import *

url="https://comic.naver.com/index"
result=get(url) 
print(result.raise_for_status()) 
#status코드에 문제사항 출력 None(문제없음)
html = BeautifulSoup(result.text,"lxml")
#lxml자동 파서 
cartoon = html.find("ol",attrs={"id":"realTimeRankFavorite"})
atag=cartoon.find_all("a")
for aa in atag:
    print(aa.get_text())


#print(atag)
#print(cartoon.a.get_text())