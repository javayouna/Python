#함수이용하기
import pandas as pd
from idlelib.iomenu import encoding
data = pd.read_csv("area.csv",encoding='euc-kr')

#값변경
def add_liter(z):
    return str(z) + "L"
#data["휘발유"] = type은 Object
#apply 함수: 해당 객체 반환
#data["휘발유"] = data["휘발유"].apply(add_liter)
#print(data)


#함수에 조건문 적용해서 값 변경
def add_literck(k):
    if k > 1700:
        return str(k)+"L" 
    return str(k)
data["휘발유"]=data["휘발유"].apply(add_literck)
print(data)
    