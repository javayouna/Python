#특정 예외처리 구성
try:
    print("값 2개를 입력하세요")
    data=[]
    number1 =int(input("첫번째 숫자를 입력하세요."))
    number2 =int(input("두번째 숫자를 입력하세요."))    
    if number1 >= 1 and number2 >= number1:
        data.append(number1)
        data.append(number2)
    else:
        raise OverflowError
        #raise : 해당 이름을 가진 except을 선정하여 실행하게함
    print(data)    
except OverflowError: #error가 발생했을 때 
    print("두번째 숫자에 첫번째 숫자보다 큰 수를 입력하세요.")
except ValueError: #java사용한 기본 exception
    print("숫자만 입력하세요.")
finally:
    print("모든 프로세서가 종료됩니다.")