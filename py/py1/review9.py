#크롤링 & 스크래핑
#http://www.ode.co.kr/shop/faq.html
from bs4 import BeautifulSoup
from requests import *

url="http://www.ode.co.kr/shop/faq.html"
call=get(url)
call.raise_for_status()
#htmlcode=BeautifulSoup(call.text,"lxml")
htmlcode=BeautifulSoup(call.content.decode('euc-kr','replace'),"lxml")
code=htmlcode.find("div",attrs={"id":"faqTable"})
code2 = code.find("tbody")
code3 = code2.find_all("div",attrs={"class":"tb-center"})
code4 = code2.find_all("div",attrs={"class":"tb-left"})
tr=code.find_all("tr")

ea=len(code4)

for idx,z in enumerate(code3):
    if idx!=0 |idx%2!=0:
       print(z.get_text())  
    if idx < ea:
        print(code4[idx].get_text())