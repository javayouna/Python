#조건문
import pandas as pd
data = pd.read_csv("area.csv",encoding='euc-kr')

#False or True로 출력됨
#print(data["휘발유"]<=1700)

#조건을 배열키로 적용하고 필터링
filter=(data["휘발유"]<=1700)
print(data[filter]) #1700이하만 출력됨 
print(data[~filter]) #1700이상만 출력됨 

#&,|를 이용해서 두 조건이 만족하는 데이터 출력 
filter2=data.loc[(data["휘발유"]<=1700) & (data["지역"]=="대구")]
print(filter2)

filter3=data.loc[(data["휘발유"]<=1700)  & (data["경유"]<=1800)]
print(filter3)
