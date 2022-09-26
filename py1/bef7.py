from bs4 import BeautifulSoup  
from requests import * 
from re import * #정규식
from random import * #랜덤

#크롤링 사용되는 page view
pno_data = ["69382","70931","69388","69389"]

#해당 pageview 배열을 순차적으로 접근할 수 있게 반복문 실행
for pno in pno_data:
    url="https://pages.coupang.com/p/"+pno+"?from=home_C2&traid=home_C2&trcid=11186418"
    html=get(url) 
    html.raise_for_status()
    #print(result.raise_for_status()) 
    #status코드에 문제사항 출력 None(문제없음)
    code = BeautifulSoup(html.text,"lxml")
    #lxml자동 파서 
    products = code.find("ul",attrs={"id":"products"})
    lis=products.find_all("li")

    for no in lis:
        products_name =no.find("div",attrs={"class":"name"}) #상품명
        products_money=no.find("strong",attrs={"class":"price-value"}) #상품가격
        products_count=no.find("span",attrs={"class":"rating-total-count"}) #추천수
        products_img=no.find("img")#이미지
        pd_img="https:"+products_img["lazy-load"]
        #products_img["lazy-load"]:attrs 임의 속성값(class나img가아님)이라서 속성을 가져오지못함 
        #임의 속성값은 []배열형태로 로드하면 쉽게가져올 수 있음..!?
        
        #code=randrange(1000,9000) #새로운 이미지 파일명 1001~8999까지 붙이기
        #imgload=get(pd_img) #해당 url로 이미지 가져옴
        
        #with open("product{}.jpg".format(code),"wb") as i:#이미지 저장
        #    i.write(imgload.content)
        
        #상품명
        products_name_txt=products_name.get_text()
        name=products_name_txt.strip() #strip 줄바꿈 및 공백
        name=name.replace(", ","")#상품명 ,없앰
        print(name)
      
        #상품가격
        money =products_money.get_text()
        #replace(",","",1):1개만 수정
        #replace(",",""):해당 단어에 모든 단어 수정
        money_txt=money.replace(",","")
        print(money_txt)
        
        #추천수
        if products_count:
            rate=products_count.get_text()
            rate_text=sub(r"[(,)]","",rate) #정규식방법 from re import 해야함
        
        else:
            rate_text="평점없음" 
        print(rate_text)
    