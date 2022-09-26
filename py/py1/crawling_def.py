#messagebox는 alert이랑 동일한 메세지 출력 입니다.
from tkinter.messagebox import * 
import requests #통신 api json형태로 변환, 사용해서 웹사이트 접속하는 형태
from bs4 import BeautifulSoup
from re import *
from sqlite3 import *
from dbconnect import * #db접속정보 
from datetime import * #dbconnect 보다 아래에있어야함

def crawlings(data):
    #showinfo = alert
    if len(data) == 1 or 10 > len(data) : #아무것도 입력안되어도 1이찍힘. 1이면 빈값
        showinfo("경고","크롤링할 url주소를 입력하셔야 합니다.")
    #elif, else
    else:
        #try,except,finally 문제 발생 시 예외처리 하는 형태
        try:
            # url = "https://www.naver.com"
            url="{}".format(data) #문자열로 변환해야만 request 사용가능
            check=requests.get(url.strip(), headers={'User-Agent':'Mozilla/5.1'}) # \n  \ 빈공간 제거
            ck=check.raise_for_status()  #None 로 뜨면 정상.
            
            if str(ck) == "None" :
                html=BeautifulSoup(check.text,"lxml")
                div = html.find("div",attrs={"module-design-id":"17"})
                div2 = div.find_all("div", attrs={"class":"component--item_card"})
               # titles = div2[0].find("span", attrs={"class":"text--title"})
                    # money = div2[0].find("strong",attrs={"class":"text--price_seller"})
                
                #db접속정보 로드
                con = connect.cursor()

                for z in div2:
                    titles = z.find("span", attrs={"class":"text--title"})
                    money = z.find("strong",attrs={"class":"text--price_seller"})
                    money = sub(",","",money.text)
                    print(titles.text, money)
                    
                    #DB에서 날짜 입력을 저장시키기 위해서 strftime으로 문자열 형태의 시간으로 변경
                    now_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    
                    print(now_date)
                    #DB저장
                    #등록시간
                    sql = "insert into pension values('0','"+titles.text+"','"+money+"','"+now_date+"')"
                    con.execute(sql)
                    connect.commit()
                showinfo("성공", "정상적으로 모든 데이터를 스크래핑 완료 하였습니다.")
         
        except:
            showinfo("실패", "크롤링할 url 주소를 다시 확인 하세요.")
                    