import pandas as pd
data = {
    'area' : ['서울','경기도','제주도'],
    'gas' : [1150,1200,980],
    'diesel' :[1860,1845,1998],
    'gasoline' : [1750,1700,1810]
    }

pr=pd.DataFrame(data)
#index.name : 표이름 
pr.index.name='지역별 유가'
print(pr)

pr2=pd.DataFrame(data)
#index 번호를 데이터 키값에 맞춰 변동한 상태
print(pr2.set_index("area"))