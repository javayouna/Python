#함수 Class, method
from itertools import product
def aaa(a,b):
    print("상품명 : {}, 가격 : {}".format(a,b))
    #상품명 : 가방, 가격 : 6000
    print("함수출력")
    #함수출력
aaa("가방",6000)

import defs as df
#출력은 이 파일 
result=df.ccc()
print(result)

#출력은 defs
df.ddd(10,20)

#----------------class---------------#
class cdatas:
    #전역변수
    money = 5000
    def aaa(self):
        #지역변수
        money=1000 #지역변수
        #money는 전역변수라서 그냥 return하면 에러남
        return self.money
cl=cdatas()
#클래스안에 여러개 전역변수 있으면 이렇게 사용
result=cl.aaa()
#print(cl.money) 
print(result)

#------------외부 class load-------------#
out=df.product()
out.add1(50000)
out.add3()
