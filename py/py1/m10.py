#pie: 원그래프 응용편(도넛) + movie.csv
import pandas as pd
import matplotlib.pyplot as mpt
import mfont
data = [30,25,20,17,10,6]
text = ["1일차","2일차","3일차","4일차","5일차","6일차"]
w={'width':0.1} #0~1까지 width원 두께 기본은 1
#wedgeprops:원 안에 빈공간 크기 (도넛 모양)
'''
mpt.pie(data,labels=text,autopct="%.1f%%",wedgeprops=w)
mpt.legend()
'''
csv=pd.read_csv("movie.csv",encoding="euc-kr")
print(csv)
#groupby:컬럼 그룹화

#gp.size():해당 파트별 그룹개수
gp=csv.groupby("영화관")
#data2 배열로 파트 개수 생성
data2=[gp.size()['cgv'],gp.size()['megabox']]
text2=["CGV","MEAGABOX"]
mpt.pie(data2,labels=text2)
mpt.title("영화 상영 영화관")
mpt.show()