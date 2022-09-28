#csv => 그래프화
import pandas as pd
import matplotlib.pyplot as mpt
import mfont
from matplotlib.lines import lineStyles

#pandas:입력
#matplotlib:출력

data = pd.read_csv("area.csv",encoding="euc-kr")
mpt.plot(data['지역'],data['휘발유'],label='휘발유',marker='o')
mpt.plot(data['지역'],data['경유'],label='경유',marker='o')
mpt.plot(data['지역'],data['LPG'],label='LPG',marker='o')
mpt.legend()
#그래프를 가시화 형태로 변경
#axis:라인 표시 x,y
mpt.grid(axis='x',linestyle='--')
mpt.show()