def ccc():
    return "test"

def ddd(a,b):
    c=a+b
    print(c)
    
gdata="핸드백" #전역변수
    
class product:
    data1 = "가방"
    data2 = "휴대폰"
    def add1(self,m):
        global gdata #global 선언시 전역변수 호출
        result=self.add2(m)
        gdata="바지" #지역변수 gdata (global x)
        #global 호출하면 gdata 전역변수가됨
        print(result)
        print(gdata)
        
    def add2(self,mm):
        data3=self.data1+"금액은: "+str(mm) 
        return data3
    def add3(self):
        print(gdata)