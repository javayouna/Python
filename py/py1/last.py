import pandas as pd
import matplotlib.pyplot as mpt
import mfont
#xls로 구성하면 usecols='탭 영어단위'
#pd.read_excel(")
#예) usercols='A,B,D:X'




#총인구
data=pd.read_excel("person.xlsx",usecols="D:X")
#print(data.iloc[1])
#남자인구
man=pd.read_excel("person.xlsx",usecols="AA:AU")
#여자인구
woman=pd.read_excel("person.xlsx",usecols="AX:BR")

#컬럼값만 출력 (data.columns):배열로 칼럼 이름만 출력
#print(data.columns)

#1000명 단위 출력
#iloc(xls,xlsx):행번호 맞춰서 해당행에 있는 모든 데이터 가져오는 함수
a_data=data.iloc[0]
mpt.figure(figsize=(10,8)) #figure그래프이미지 x,y늘려줌
#mpt.barh(data.columns,a_data//1000)

m_data=man.iloc[0] #man.columns 목차
w_data=woman.iloc[0] #woman.columns 목차
mpt.barh(data.columns,-m_data//1000,label="남성인구")
mpt.barh(data.columns,w_data//1000,label="여성인구")
mpt.legend()
mpt.title("2022년 8월 남녀 인구 분포도")
mpt.savefig("202208person.png",dpi=200)
mpt.show()