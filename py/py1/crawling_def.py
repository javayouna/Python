#messagebox는 alert이랑 동일한 메세지 출력 입니다.
from tkinter.messagebox import * 
import requests #통신 api json변화 사용해서 웹사이트 접속
from bs4 import BeautifulSoup

def crawlings(data):
    #사용자가 입력한 값을 변수로 변환
    #showinfo=alert
    #print(len(data))
    if len(data)==1 or 5 > len(data):
        showinfo("경고","올바른 url를 입력하세요.") 
    else:
      #try,except,finally 문제 발생시 예외처리  
        try:
            url="{}".format(data) # data #문자열로 변환해야 requests사용할 수 있음
            check =requests.get(url.strip()) # \n형태문제가 발생할 수 있음 
            ck=check.raise_for_status() #NoneType(통신 type)    
            if str(ck) == "None": #ck==None
                html=BeautifulSoup(check,"lxml")
                print(html)
                showinfo("성공","정상적인 url입니다.")
        except:
            showinfo("실패", "오류:url를 다시 확인하세요.")