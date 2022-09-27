from bs4 import BeautifulSoup  
from requests import * 
from random import *
from re import * #정규식
data="http://9s.co.kr/shop/shopbrand.html?xcode=127&type=Y"
url=data
html=get(url)
html.raise_for_status()
html_text=html.text
code=BeautifulSoup(html.content.decode('euc-kr','replace'),"lxml")
products = code.find("ul",attrs={"class":"prd_wrap new2022"})
lis=products.find_all("li")
#print(lis)


for no in lis:
    products_subname =no.find("p",attrs={"class":"subname"}) #상품명
    products_name=no.find("p",attrs={"class":"name"}) #상품상세
    products_subname2=no.find("p",attrs={"class":"subname2"}) #상품타입
    products_strike =no.find("p",attrs={"class":"strike"})#정가
    products_strike =no.find("span",attrs={"class":"strike"})#정가
    products_price=no.find("span",attrs={"class":"price"})#할인가
    products_MS_prod_img_s=no.find("img",attrs={"class":"MS_prod_img_s"})#이미지
    products_src="http://9s.co.kr"+ products_MS_prod_img_s["src"]
    #products_rollover="http://9s.co.kr"+ products_MS_prod_img_s["rollover_onimg"]

    #상품명
    products_subname_tt=products_subname.get_text()
    products_subname_text=products_subname_tt.strip()
    #print(products_subname_text)

    #상품상세
    products_name_tt=products_name.get_text()
    products_name_text=products_name_tt.strip()
    #print(products_name_text)

    #상품타입
    products_subname2_tt=products_subname2.get_text()
    products_subname2_text=products_subname2_tt.strip()
    print(products_subname2_text)
   
    #정가
    products_strike_tt=products_strike.get_text()
    products_strike_text=products_strike_tt.replace(",","")
    #print(products_strike)
    
    #할인가
    products_price_tt=products_price.get_text()


    #이미지
    #print(products_src)
