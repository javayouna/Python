from tkinter import *
from pkg_resources._vendor.jaraco.context import null


   
root=Tk()
root.title("연습프로그램") #프로그램 타이틀이름
root.geometry("500x500") #가로크기 x 세로크기
root.resizable(True, True) #늘렸다 줄였다 할 수 있음 

txt=Entry(root,width=50) #Entry 한줄짜리 input (heignt x)
#Text로 사용할 경우 insert써야됨(width,height)
txt.pack()
#Text(1="첫번째행".0="열 첫번째 위치" END="마지막단어까지")

txt2=Text(root,width=30,height=2)
txt2.pack()
txt2.insert(END, "")
#txt.insert(END, "테스트")
def aaa():
   url= txt.get()
   url2= txt2.get(0.1,END)
   print(url)
   print(url2)
   
btn=Button(root,width=8,height=2,text="크롤링",command=aaa)
btn.pack()
root.mainloop()