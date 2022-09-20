#배열로 만들기
age=[10,20,30,40,50,60,70,80,90,100]
print(age)

person=["홍길동","이순신","강감찬"]
print(person[2])
print(person.index("이순신")) #idnex
print(len(person)) #배열 총개수
person.append("유관순")
print(person)

person.insert(1,"세종대왕")
#insert(인덱스번호, 추가할 값)
print(person)
print(person.pop()) #pop()값을 뒤에서부터 차례대로 가져옴
print(person.pop())

numbers = [5,8,7,1,9,3,2,6]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

numbers.clear()
print(numbers)

datas=["hong","홍길동",33,3000,False]

datas2 =["면도기","신발","바지","이어폰"]

#datas에 있는 배열값과 datas2에 있는 배열값을 datas에 종속시킴
datas.extend(datas2) #배열값을 종속시킬때는 변수 처리하진않음
print(datas)
print(datas+datas2) #해당 배열 변수명 출력

#키값이 있는 배열
infodata = { "mid" : "hong", "mname":"홍길동", "age":33}
print(infodata["mname"]) #배열에있는 키명으로 로드
print(infodata.get("mid")) #get함수사용해서 키 배열가져옴

print(infodata.keys())


#in은 키 배열에 해당 키명이 있는지 확인할 떄 사용
print("age" in infodata) #True
print("mtel" in infodata) #False

infodata["tel"]="01023456677"
print(infodata)
infodata["age"]=30
print(infodata)

#삭제 키+값 
del infodata["mid"]

#삭제 값만
infodata["mid"]=""
print(infodata)
print(infodata.keys()) #key이름만 출력=Object.keys (Javascript)
print(infodata.values()) # 키 배열에 값만 출력할 경우 
 
