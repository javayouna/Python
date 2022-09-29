import pandas as pd
import matplotlib.pyplot as mpt
import mfont
#xls로 구성하면 usecols='탭 영어단위'
#예) usercols='A,B,D:X'

#총인구
data=pd.read_excel("person.xlsx",usecols="D:G")
#남자인구
man=pd.read_excel("person.xlsx",usecols="AA:AD") #데이터 너무 많아서 줄임
#여자인구
woman=pd.read_excel("person.xlsx",usecols="AX:BA")
#data.T of data : 인덱스 위치 변경

#(남자데이터)
#여러 데이터 출력하면 bar 그래프가 올바르게 반영 안됨 
#bar데이터
#subplots, subplot:그래프 하나에 여러 데이터 보여줄떄
#(알고만있어도됨): 이렇게 써야하고 s붙이면 (subplots 하면 알아서 잡힘)
#mpt.subplot(0,0,1)
#mpt.subplot(0,1,2)
fig, ax1 = mpt.subplots(figsize=(10,8))
titles=data.columns;
mandata=man.loc[0]//100
ax1.bar(data.columns,mandata,color="orange",label="남자")
ax1.set_ylim(0,30000) #세로데이터최대
ax1.set_ylabel("남자 0~19세 데이터")
ax1.legend()
for idx, txt in enumerate(mandata):
    ax1.text(idx,txt+500,txt,ha='center')

#(여자데이터)
#plot 그래프 남자데이터와 안 겹치게
womandata=woman.loc[0]//50
#twinx,twiny: ?
ax2=ax1.twinx() #그래프 데이터에 추가로 별도 수치값 표현 (ax1 수치 포함)
ax2.set_ylim(0,30000)
ax2.set_ylabel("여자 0~19세 데이터")
ax2=mpt.plot(data.columns,womandata,color="red",label="여자")
mpt.legend(loc='center left')

#선 그래프에 수치값 표현 주의점> 값을 나눠서 표현한다면.. +1, +10 보다 큰 숫자를 입력 
for idx2, txt2 in enumerate(womandata):
    mpt.text(idx2,txt2+500,txt2,ha='center')
mpt.show()