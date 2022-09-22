from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from asyncio.tasks import sleep

dw = webdriver.Chrome(ChromeDriverManager().install())
dw.get("https://www.naver.com")
sleep(6000)
