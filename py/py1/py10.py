#BeautifulSoup에 대한 bs4를 사용하기 위해 라이브러리를 pom.xml처럼 파이썬 등록해야함
#설치는 cmd로 설치 


'''
1. 파이썬이 설치된 디렉토리 경로 확인
2. cd이용해서 해당 디렉토리 이동
3. cd Script 디렉토리 안으로 이동
4. pip install beautifulsoup4
'''



from urllib.request import urlopen
from bs4 import BeautifulSoup
from idlelib.iomenu import encoding

#beautifulsoup4 : 접속한 휍페이지모든 문서파일 파서
#urlopen(웹페이지 주소)
html =urlopen("https://n.news.naver.com/mnews/article/025/0003225002?sid=102")

#해당 url parser작업함
object = BeautifulSoup(html,"html.parser")

#해당 parser 문자를 html로 저장 
files=open("1.html","w",encoding="utf-8")
print(object,file=files)
files.close()
