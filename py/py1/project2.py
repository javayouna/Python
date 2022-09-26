from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from asyncio.tasks import sleep

#자동로그인, 자동페이지이동, 자동검색...
dw = webdriver.Chrome(ChromeDriverManager().install())
dw.get("https://www.naver.com") #자동 크롬 브라우저 이동
#https://search.naver.com/search.naver?query=
#https://search.daum.net/search?q=
#https://google.com/search?q=