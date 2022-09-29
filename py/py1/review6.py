#예외처리 try~ except
try: #정상처리
    a="123a"
    b=int(a)
    print(b)

except: #예외처리
    print("error")
    
finally: #프로세스 종료
    print("정상처리 완료")