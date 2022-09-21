from bs4 import BeautifulSoup  #파싱 파서사용하기 위해 
from nt import mkdir, getcwd
from os import * #운영체제가 기본제공하는 모듈

import antigravity

#htmlcode= BeautifulSoup("<div><span>테스트</span></div>")
#soup=BeautifulSoup("<span><i>테스트</i></span>")
#print(soup.prettify())


directory="html"
print(getcwd()) #현재경로
mkdir(directory) #mkdir(리눅스):디렉토리 생성