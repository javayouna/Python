#막대그래프+pandas3
import pandas as pd
import matplotlib.pyplot as mpt
import mfont
from matplotlib.lines import lineStyles

data=pd.read_csv("area.csv",encoding="euc-kr")
#높은 순위 데이터부터 위로 
'''
mpt.bar(data['지역'],data['경유'])
mpt.bar(data['지역'],data['휘발유'])
mpt.bar(data['지역'],data['LPG'])
'''

#데이터를 누적해서 출력하는 형태
mpt.bar(data['지역'],data['경유'],label='경유')
mpt.bar(data['지역'],data['휘발유'],label='휘발유')
mpt.bar(data['지역'],data['LPG'],label='LPG')

#bottom:그래프를 출력할 때 해당 값 누적해서 표현
mpt.bar(data['지역'],data['경유'],bottom=data['LPG']+data['휘발유'],label='총금액')

mpt.legend()
mpt.show()
