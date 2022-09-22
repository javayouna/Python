from os import *

def logout(): #컴퓨터 로그아웃
    return system("shutdown -l")

def restart(): #컴퓨터재부팅
    return system("shutdown /r /t 0") 

def stop(): #컴퓨터종료
    return system("shutdown /s /t 0")

#def formatting(): 컴퓨터포맷
#    return system("c:\format /s")