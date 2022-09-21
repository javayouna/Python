from bs4 import BeautifulSoup  #파싱 파서사용하기 위해 
from os import * #운영체제가 기본제공하는 모듈
from requests import * #requests: 해당 url 접속 정보 확인

url = get("https://www.naver.com")
#print("응답코드:",url.status_code) #200 : 정상

if url.status_code == codes.ok:
    print(url.text)
    print("정상적인 웹사이트 페이지입니다.")
else:
    print("해당 웹사이트는 보안 or 코드에 문제가 있습니다.")