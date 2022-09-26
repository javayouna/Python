#함수
def aaa(): #def javascript function
    print("함수 호출 완료")
aaa() #함수 즉시 실행

def bbb(a):
    print("함수 호출값은 %s" %(a))
bbb("홍길동")

def ccc(b,c):
    d = b+c
    return d
z=ccc(5,10)
print("결과값은 %s입니다." %(z))

money = 100000
def bank(umoney):
    if umoney > money:
        msg="출금 금액이 모자랍니다."
    else:
        m=money - umoney
        msg = str(umoney)+'출금 되었습니다. 잔액은'+str(m)+'입니다'
    return msg

result = bank(5000)
print(result)

#함수 인수밗에 값을 전달해서 출력하는 형태
def myinfo(username,age=33,email="honh@gmail.com"):
    print("고객명:{0},연령:{1},이메일:{2}".format(username,age,email))
myinfo("홍길동") #username 인수값 하나만     
    
    