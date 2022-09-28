#빅데이터 분석 차트 
import pandas as pd
import matplotlib.pyplot as mpt
import mfont

data=[100,50,80,77,65]
data2=[50,75,95,42,16]
#해당 값 크기를 표시하기위한 배열
total=[data[0]+data2[0],data[1]+data2[1],data[2]+data2[2],data[3]+data2[3],data[4]+data2[4]]
#scatter:산점도 그래프 (빅데이터 분석표)
#산점도 그래프는 무조건 sizes를 정해서 출력해야함

#별개 데이터
cdata=['red','blue','green','orange','gray']
data3=["서울","경기도","세종시","광주","대구"]
#mpt.scatter(data,data2,sizes=total)

mpt.scatter(data,data2,sizes=total,color=cdata)
#scatter에 반복문 text 
for a, textin in enumerate(data3):
    mpt.text(data[a]-5,data2[a]+3,data3[a])

#color로 색상바 표현
mpt.colorbar(orientation="horizontal")
mpt.title("각 지역별 차량 보유대수")
mpt.title('각 지역별 차량 보유')
mpt.xlabel("휘발유 차")
mpt.ylabel("경유차")
#mpt.legend()
mpt.show()