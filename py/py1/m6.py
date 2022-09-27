import matplotlib.pyplot as mpt #그래프모듈
import mfont

person = ["이순신","강감찬","유관순"]
product = [46,10,86]
barcolor=["red","green","orange"]#배경색상
#bar:막대그래프
'''
#세로그래프
bar=mpt.bar(person,product,color=barcolor)
mpt.ylim(0,100) #lim:범위와 단위를 정할 때 사용
#ylim:y축 limit(단위,최대범위)
#mpt.xticks(rotation=45)
#rotation:글자 비스듬이 
for idx,txt in enumerate(bar): 
    #txt.get_height():막대 세로 계산 출력
    mpt.text(idx,txt.get_height()+5,product[idx],ha="center")
'''


#가로 그래프
bar=mpt.barh(person,product,color=barcolor)
mpt.xlim(0,100)
#bar[0].set_hatch('\\') #막대배경
#bar[1].set_hatch('*')
#bar[2].set_hatch('x')
for idx,txt in enumerate(bar):
    #주의점 barh 사용시 x축 기준으로 get_width로사용
    mpt.text(txt.get_width()+5,idx,product[idx])
mpt.show()