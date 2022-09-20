#문자열을 자르기 및 해당 문자열 가져오기(배열구조이므로 무조건 0부터시작)
gender="911101-2345678"
print("성별: "+gender[7])
print("월일: "+gender[2:6]) #2부터~5까지..
print("생년월일:"+gender[:6])#무조건 0부터 시작해서 문자열 가져옴
print("주민번호 뒷자리:" +gender[7:]) #해당 문자열 번호부터 끝까지 가져옴
print("생년월일:"+gender[:-8]) #-1부터는 문자열에서 거꾸로넘버링하게됨
word="Python Programming"
print(word.lower()) #lower(전체 소문자)
print(word.upper()) #upper(전체 대문자)
 #is는 문자열에 대한 검토 할 때 사용하는 문법 islower,isupper
print(word[2].isupper()) #Ture
print(len(word)) #len.lenth와 같은 뜻
#print(word.replace("Python","Java")) #replace는 단어를 변경할 때 

print(word.index("g")) #해당 문자열 인덱스출력
print(word.index("P"))
i=word.index("P") #문자열에서 동일한 단어가 있어도 첫번째 단어 번호 
i=word.index("P",i+1) #문자열에 동일한 단어 다음을 찾아서 출력 
print(i)

#find -1:문자열 또는 단어가 없을 경우
print(word.find("gra1")) #find문자열을 찾을 때 사용, (indexOf와 동일한 기능)
print(word.count("P")) #동일한 문자 개수가 몇개인지 카운팅 
