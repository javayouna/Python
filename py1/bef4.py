from bs4 import BeautifulSoup  
from requests import *

url="https://www.nate.com/"
res=get(url)
res.raise_for_status()
result=BeautifulSoup(res.text,"lxml")
#태그 이름으로 태그안 텍스트 가져올 수 있음
#중복 태그면,가장 먼저 읽어오는 라인
#print(result.title)
#print(result.title.get_text())
#find: 해당 단어를 찾음
#attrs:(attribute 속성명)
rank=(result.find("div",attrs={"class":"isKeyword"}))
#print(rank.h4.get_text())
#print(rank.li)
#rank에만 속하는 태그 중 span태그와 해당클래스명 검토 

#ranknum = rank.find("span",attrs={"class":"num_rank"})
#ranksubject=rank.find("span",attrs={"class":"txt_rank"})
#print(len(rank.li)) #반복되는 태그 개수 확인 
#find는 1개 태그, find_all 부모 마크업안에 있는 모든태그

'''
print(ranknum)
print(ranksubject)
print(ranksubject.get_text())
'''
ranknum = rank.find_all("span",attrs={"class":"num_rank"})
ranksubject=rank.find_all("span",attrs={"class":"txt_rank"})
#find_all은 기본으로 배열구조가 변경됨 

w=0
for bb in ranknum:
    print(bb.get_text())
    print(ranksubject[w].get_text())
    w+=1

for cc in ranksubject:
    print(cc.get_text())

