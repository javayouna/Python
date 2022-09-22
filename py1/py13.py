#extends 형태 파이썬

class box: #box 추상 클래스
    def __init__(self,data1,data2):
        self.data1=data1
        self.data2=data2
        
class box2(box): #box2에서 box를 상속받음
    def __init__(self,data1,data2,data3): #상속받을 때 값을 적용
        box.__init__(self, data1, data2) #추상클래스해서 세팅됨 self
        self.data3=data3
    def abc(self): #추상클래스+box2클래스 출력하게됨(self)
        print("data값은 {0},{1},{2}".format(self.data1,self.data2,self.data3))
#box2 호출해야만 box를 상속받아 처리 가능
a=box2("hong","홍길동","hong@nate.com")
a.abc() #box2에 있는 abc클래스 호출함