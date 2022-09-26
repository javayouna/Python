#평균값, 최소, 최대값 특정 행렬값(loc)
import pandas as pd
#read_csv 로드시
data = pd.read_csv("area.csv",encoding='euc-kr')
#print(data)
#describe():평균값 카운터값 최소값 최대값등 산술 출력 (문자열 상태는 X) 
#25~75% : 전체 데이터 파트 부분
#print(data.describe())

#loc
#print(data.loc[0])

#특정 칼럼값 가져오기
#print(data.loc[0]["LPG"])

#두가지 지역을 비교하는 데이터
print(data.loc[[0,1],"경유"])
print("------------------")
print(data.loc[[0,1],["휘발유","경유"]])