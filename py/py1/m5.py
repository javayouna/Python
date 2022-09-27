import matplotlib.pyplot as mpt #그래프모듈
import mfont

days = [7,8,9] #월별 
azn = [100,156,112] #아스라제네카
pfz = [95,112,198] #화이자
sen = [92,88,76] #얀센
mod = [74,69,87] #모더나

mpt.plot(days,azn,label='아스트라제네카',marker="o")
mpt.plot(days,pfz,label='화이자',marker="o")
mpt.plot(days,sen,label='얀센',marker="o")
mpt.plot(days,mod,label='모더나',marker="o")
mpt.xticks(days,['7월','8월','9월'])

for idx,txt in enumerate(azn):
    mpt.text(days[idx],azn[idx]+5,txt,ha="center")


#ncol:한줄에 몇개 label출력하는지 선정
mpt.legend(ncol=2)
mpt.show()