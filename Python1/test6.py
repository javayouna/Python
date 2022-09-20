#%d(숫자), %s(문자,숫자)
print("포인트 %d가 있습니다." %6000)
print("%s님 환영합니다." %"홍길동")
print("%s님 포인트 %s가있습니다." %("이순신","5000"))

#{}형태의 배열형태의 구성                           
print("{}님 회원등급은 {}입니다".format("유관순","실버회원"))
print("입금하신 총 금액은 {}입니다".format(55000+200))
print("고객님 아이디{1}이며, 가입하신 이름은{0}입니다.".format("세종대왕","kings"))

#변수명 형태로 출력가능하고 변수의 값을 외부로 받아서 출력시킬 수 있음 
print("상품은{product}이며, 금액은 {money}입니다.".format(product="청소기",money=1000))

#3.6ver 이상만 사용 가능 
color="red"
car="제네시스"
print(f"자동차 이름은 {car}이며, {color}색상입니다.")

#줄바꿈
#\n

#\하나만 입력할 경우는 \n처럼 특수 언어를 사용하는 형태로 인식
#윈도우 서버에서 로컬로 파일을 로드할 경우 \\2개 사용해야함

print("c:\\user\\window\\")

#패스워드 자동생성 프로그램
from random import *
word1 ="acbdefghijklmnl"
lens=len(word1)
pw1 = int(random() * lens)
pw2 = int(random() * lens)
pw3 = int(random() * lens)
pw4 = int(random() * lens)
passwd=word1[pw1]+word1[pw2]+word1[pw3]+word1[pw4]
print(passwd)




