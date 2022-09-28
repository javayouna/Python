import pandas as pd
import matplotlib.pyplot as mpt
import mfont
#xls로 구성하면 usecols='탭 영어단위'
#예) usercols='A,B,D:X'

#총인구
data=pd.read_excel("person.xlsx",usecols="D:X")
#남자인구
man=pd.read_excel("person.xlsx",usecols="AA:AD") #데이터 너무 많아서 줄임
#여자인구
woman=pd.read_excel("person.xlsx",usecols="AX:BA")
#data.T of data : 인덱스 위치 변경
mpt.figure(figsize=(10,8))
mpt.plot(man//1000,data.index,marker='o')
mpt.plot(woman//1000,data.index,marker='o')
mpt.show()
