#class 선언 방식 및 메소드 형태
from tarfile import pwd
class box: #class를 선언
    def __init__(self,a,b,c):
        self.a=a #self=JAVA(this)
        self.b=b 
        self.c=c
        print("값은 {0},{1},{2}".format(self.a,self.b,self.c))
        #print("값은 %s, %s, %s" %(a)%(b)%(c))
        
    def abc(self): #일반메소드
         print(self.c) 
           
box("홍길동",20,30) #_init_에 인자값 전달
box(60,100,200)
cl=box(5,10,15) #_init_에 인자값 전달 setter
cl.abc() #abc 메소드를 로드 getter형태

class box2:
    def __init__(self,name,id,pw):
        self.name=name
        self.id=id
        self.pw=pw
    def abc(self,email): #일반 메소드에 추가 인자값 적용
        print("고객명:{0}, 아이디:{1}, 이메일:{2}"\
              .format(self.name, self.id,email))
        
data=box2("강감찬","kang","a123456") #_init_에 값 등록 
data.abc("kang@naver.com") #abc메소드에 추가로 값 등록