from bs4 import BeautifulSoup  
from requests import * 
from random import *

data="http://9s.co.kr/shop/shopbrand.html?xcode=127&type=Y"

url=data
html=get(url)
html.raise_for_status()
code=BeautifulSoup(html.text,"lxml")
#code=BeautifulSoup(html.content.decode('euc-kr','replace'))
products = code.find("ul",attrs={"class":"prd_wrap new2022"})
lis=products.find_all("li")
#print(lis)

products_img=code.find('li','prd_list').find_all('img')
print(products_img)
prd_list=[]
for f in products_img:
    img_src1=f['src']
    prd_list.append(img_src1)
print(prd_list)


'''
for no in lis:
    products_subname =no.find("p",attrs={"class":"subname"}) #상품명
    products_name=no.find("p",attrs={"class":"name"}) #상품상세
    products_subname2=no.find("span",attrs={"class":"subname2"}) #상품타입
    products_strike =no.find("span",attrs={"class":"strike "})#정가
    products_price=no.find("span",attrs={"class":"price"})#할인가
    products_MS_rod_img_s=no.find("img",attrs={"class":"MS_rod_img_s"})
    #products_MS_rod_img_s=no.find("img")#이미지
    #pd_img="https:"+products_MS_rod_img_s["lazy-load"]

    code=randrange(1000,9000) 

    products_subname_tt=products_subname.get_text()
    products_subname_text=products_subname_tt.strip()
    #print(products_subname_text)

    print(products_MS_rod_img_s)
'''
