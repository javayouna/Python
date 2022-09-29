#크롤링 & 스크래핑
from bs4 import BeautifulSoup
from requests import *
from attr._make import attrs

url="http://moko2.cafe24.com/site.html"
call=get(url)
call.raise_for_status()
#htmlcode=BeautifulSoup(call.text,"lxml")
htmlcode=BeautifulSoup(call.content.decode('utf-8','replace'),"lxml")
code=htmlcode.find("div",attrs={"class":"divcss"})
code2=code.find("ul",attrs={"class":"ulcss"})
code3=code2.find_all("li")

f=0
for txt in code3:
    print(txt.get_text())

