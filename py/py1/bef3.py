from bs4 import BeautifulSoup  
from requests import * 
from tkinter import *
from idlelib.iomenu import encoding   
from test.test_urllib import urlopen

root=Tk()
root.title("웹페이지 크롤링") #프로그램 타이틀이름
root.geometry("500x100") #가로크기 x 세로크기
root.resizable(False, False) #True:늘렸다 줄였다 할 수 있음 False:안됨

url=Text(root,width=60,height=2)
url.pack()
url.insert(END, "")

def pageload():
    urladdr=url.get(0.1, END)
    check=get(urladdr)
    
    if check.status_code == codes.ok:
        html=urlopen(urladdr)
        object =BeautifulSoup(html,"html.parser")
        files=open("test.html","w",encoding="utf-8")
        print(object,file=files)
        print("크롤링 완료")
        files.close()
    else:
        print("올바른 웹페이지가 아닙니다.")
    
btn = Button(root,text="웹크롤링",command=pageload)
btn.pack()
root.mainloop()