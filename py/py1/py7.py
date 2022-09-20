#전역변수, 지역변수
box="변수값"
box3="" #최초 전역변수 비어있는 값

#전역변수는 절대 값 변화 없음 
#global = static이랑 비슷

def afunction():
    global box3
    print(box)
    box2="변수값2"
    print(box2)
    print(box3) #전역변수값이 출력
    box3="변수값3" #afunction실행시 box3에 문자값 입력
    #만약에 global이 없으면 새로운 지역 변수 생성,
    #global적용시 전역변수에 새로운 값을 적용 

def bfunction():
    print(box)
    #print(box2) error afunction에서 사용하는 변수를 bfunction에 사용
    print(box3) #""이 출력됨 
    
    
    #단, afunction보다 bfunction이 먼저 실행되면 빈값 출력

afunction()
bfunction()