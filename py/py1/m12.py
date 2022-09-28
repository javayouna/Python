#산점도 응용 부분 
import pandas as pd
import matplotlib.pyplot as mpt
import mfont

#scatter:x축, y축
data = pd.read_csv("movie.csv",encoding="euc-kr")
#c:color+cmap(자동색상)
#scatter에서 text사용시 x축, y축 값이 int어야지 반복문적용 가능
mpt.scatter(data["지역"],data["관객수"],sizes=data["관객수"]*5,c=data["관객수"])

    
mpt.colorbar()
mpt.xlabel("지역")
mpt.ylabel("관객수")
mpt.show()


