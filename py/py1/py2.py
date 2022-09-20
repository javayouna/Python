a = 15
if a == 5: #if문 :={}
    print("숫자 5입니다.")
elif a == 10: #elif문 = else if
    print("숫자10입니다.")
else:
    print("숫자15입니다.")
#input = Scanner 같은 기능
#input은 모두 str로 인식되니까 , int 변환해야 산술식 적용
'''
b= input("좋아하는 숫자를 입력하세요")
c= int(b) % 2 
if c == 0:
    print("해당 숫자는 짝수입니다.")
else:
    print("해당 숫자는 홀수입니다.")
'''
'''    
person = input("아이디를 입력하세요")
if person == "hong" or person =="kim":
    print("일바 회원입니다.")
elif person == "park":
    print("실버 회원입니다.")
else:
    print("가입되지 않은 회원입니다.")
'''
    
number = int(input("총 입금하실 금액은?"))
if 10000 > number:
    print("입금은 최소 10,000원 이상 입력하셔야합니다.")
elif number >= 10000 and 5000000  >= number: #입력범위 설정해서 조건 
    print("입금이 되었습니다.")
else:
    print("입금은 한번에 5,000,000까지 입니다.") 
