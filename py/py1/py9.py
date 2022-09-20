#파일저장
from idlelib.iomenu import encoding


'''
#open("파일명","읽기(r),쓰기(w),수정(a)","언어셋"):파일 생성및 저장 
files=open("./data.txt","w",encoding="utf-8")
print("홍길동",file=files) #file=해당파일명에 데이터저장
print("이순신",file=files)
files.close() #open파일을 close로 종료
'''

'''
#파일수정
files=open("./data.txt","a",encoding="utf-8")
print("유관순",file=files)
'''

#파일읽기
files=open("./data.txt","r",encoding="utf-8")
#print(files.read())
#print(files.readline()) #한줄씩 출력

#반복문으로 파일 데이터값 가져옴
'''
while True:
    line=files.readline() #파일에있는 라인별로 읽어옴
    if not line: #만약에 더 이상 읽을라인이 없을 경우
        break 
    print(line,end="") #end="" readline은 엔터기능 없앰(공백 삭제)
files.close()
'''
for line in files.readlines(): #readlines 이용해서 반복문 출력 
    print(line,end="")
    files.close()