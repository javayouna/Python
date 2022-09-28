#pie: 원그래프
import pandas as pd
import matplotlib.pyplot as mpt
import mfont

data = [30,25,20,17,10,6]
text = ["1일차","2일차","3일차","4일차","5일차","6일차"]
color =['skyblue','pink','green','blue','red','yellow']


#autoopct : 데이터에 % 출력 
#1f:데이터 1개에 소수점 1자리,f:flot, i:int
#%% : 그래프에 %를 출력하기 위해 
#sartangle:원 각도 조절
#mpt.pie(data,labels=text,autopct='%.2f%%',startangle=90)


#조각피자
#transform=[0.2,0.1,0.1,0.2,0,0]
transform=[0.05]*6 #원 그래프 배열개수에 맞춰서 띄어짐 
#explode:원 그래프 조각 낼떄
mpt.pie(data,labels=text,colors=color,autopct='%.1f%%',explode=transform)
mpt.title("원 그래프 테스트")
mpt.legend(loc=(1,0.5)) #loc (위치변경) -> loc(x축,y축)
mpt.show()

