#사용자 입력값에 따른 결과 출력
try:
    print("값 2개를 입력하세요")
    data=[]
    data.append(int(input("첫번째 숫자를 입력하세요.")))
    data.append(int(input("두번째 숫자를 입력하세요.")))     
    print(data)    
except ValueError: #error가 발생했을 때 
    print("숫자만 입력하세요.")
except: #java사용한 기본 exception
    print("전체 오류")