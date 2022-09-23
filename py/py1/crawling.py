from tkinter import *
from _functools import partial
#gui
root = Tk()
root.title("펜션 쿠팡 크롤링")
root.geometry("640x150")  #가로 X 세로

msg = Label(root, text="쿠팡 크롤링 주소 형식 ")
msg2 = Label(root, text="예시) https://www.coupang.com/np/search?component=&q=경기펜션&page=1")
msg.pack()
msg2.pack()

###입력파트###
src = Text(root,width=50, height=3, padx=5 ) # 크롤링 주소입력
src.insert(END, "") # 사용자가 입력한 주소값을 전달받기 위한 코드
src.place(x=50, y=50) #place는 원하는 위치에 오브젝트를 설정할 수 있음
#src.pack(side="left")

#from형태의 import 방식
from crawling_def import *
#btn = Button(root, width=10, height=2, text="크롤링 시작", command=partial(crawlings,"홍길동"))
#btn = Button(root, width=10, height=2, text="크롤링 시작", command=lambda:crawlings("url"))

def textload():
    #사용자가 입력한 값을 변수로 변환
    url=src.get("1.0",END)
    #crawling_def.py 함수로 값 전달
    crawlings(url)
        
btn = Button(root, width=10, height=2, text="크롤링 시작", command=textload)
#일반적인 import 방식
# import crawling_def as craw
# btn = Button(root, width=10, height=2, text="크롤링 시작", command=craw.crawlings)
# lambda
btn.place(x=50, y=50)

#btn.pack(side="right")
btn.place(x=450, y=50)
root.resizable(False, False)
root.mainloop() #실행 무조건 맨 아래 생성