#그래프 thicks 표현 방식
import matplotlib.pyplot as mpt #그래프모듈
import mfont

#x축, y축 배열 개수 같아야함
#x,y축 중 데이터 숫자 값은 반드시 있어야함
#y축 한글, x축 숫자로 표현 또는 반대

x=[10,15,'데이터']
y=['서울','인천','대구']

'''
mpt.plot(x,y) #(x축값, y축값)
mpt.xlabel("x축",color='blue',loc='left') #left,right,center
mpt.ylabel("y축",color='red',loc='top') #top,center,bottom
mpt.show()
'''

#본데이터
xx=[3,7,9]
yy=[5,9,12]


#mpt.plot(xx,yy) #데이터 개수는 같아야함

#ticks로 출력
x1=[1,2,3]
y1=[3,6,9,12]
#mpt.xticks(x1) #x축 라벨
#mpt.yticks(y1) #y축 라벨 
#mpt.show()

#응용
data1 = [25,30,35,40]
data2 = [10,20,30,40]
#ticks 라벨꾸며주는 형태
mpt.xticks(data1, ['1월','2월','3월','4월']) #y축 10단위씩
mpt.yticks(data2, [10,20,30,40]) #y축 10단위씩
mpt.plot(data1,data2) #출력 
mpt.show()
