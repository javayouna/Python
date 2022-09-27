import matplotlib.pyplot as mpt #그래프모듈
import mfont

x=[10,20,30,40]
y=[15,25,35,45]

mpt.plot(x,y,label="테스트 그래프",color="red",marker="o")
mpt.legend()
#enumerate: 그래프값 포인트에 값 가져와서 text

#idx(배열 index 0~부터),txt(배열값)
for idx,txt in enumerate(x):
    mpt.text(x[idx],y[idx]+0.7,txt,ha="right",color='blue')
    #ha:left,right,center 반대방향
    #x[idx]+0.5: x배열값 (위치)에 글자를 0.5만큼 이동
    #y[idv]+0.5: y배열값 (위치)에 글자를 0.5만큼 이동
mpt.show()