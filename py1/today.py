from datetime import *
#오늘 날짜 및 시간 출력
today = datetime.now()
print(today.replace(microsecond=0)) #replace(microsecond=0) : 초 부분에 소수점을 없앰

#오늘 날짜
day= today.date()
print(day)

#시간
time = today.time()
print(time.replace(microsecond=0))

#시간을 문자열로 변환 -> DB에 저장시 필요
time=datetime.today()
print(time.strftime('%Y-%m-%d %H:%M:%S'))