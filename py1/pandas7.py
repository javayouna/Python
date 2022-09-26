#정렬
import pandas as pd
from idlelib.iomenu import encoding
data = pd.read_csv("area.csv",encoding='euc-kr')

#오름차순 sort_values
print(data.sort_values("휘발유"))
print("-------------------------------")

#내림차순 sort_values,ascending=False 기본:True
print(data.sort_values("휘발유",ascending=False))
print(data["휘발유"].sort_values(ascending=False))
print("-------------------------------")

#index숫자 값으로 내림차순
print(data.sort_index(ascending=False))
print("-------------------------------")

#내림차순 키 2개
print(data.sort_values(["휘발유","경유"],ascending=True))
print("-------------------------------")

#replace
print(data["지역"].replace({"서울":"서울특별시","인천":"인천광역시"}))
#print(data.replace({"서울":"서울특별시","인천":"인천광역시"}))
print("-------------------------------")

#기타
print(data["지역"].str.upper()) #소문자=>대문자
print(data["지역"].str.lower()) #대문자=>소문자
print("-------------------------------")

#필드추가 +,=,*,/ 등 출력
data['평균값']=(data['휘발유'] + data['경유'] + data['LPG'])/3
print(data)
print("-------------------------------")

#필드숨김
print(data.drop(columns=["LPG"]))
print(data.drop(index=7))



