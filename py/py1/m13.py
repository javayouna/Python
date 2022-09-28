#다중 그래프 출력 a,axs
import pandas as pd
import matplotlib.pyplot as mpt
import mfont

#axs:다중 표 제작 사용 함수
#subplots:가로,세로 개수만큼 생성
#figsize:그래프 사이즈 설정
'''
a,axs=mpt.subplots(2,2,figsize=(15,10))
a.suptitle("파트별 데이트 분석")
'''
'''
#버전 업
a,axes=mpt.subplots(2,2,figsize=(15,10))
a.suptitle("파트별 데이트 분석")
'''

#subplots_adjust: 가로, 세로 여백
#각 그래프 가로,세로 사이즈
a,axes=mpt.subplot(2,2)

a.set_size_inches(15,10)
mpt.subplots_adjust(wspace=0.5, hspace=0.5)
