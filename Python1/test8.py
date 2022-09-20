#배열기호 [],{}
#튜플:  셀 수 있는 수량의 순서가 나열된 형태
subject=("자바","파이썬","서블릿")
print(subject[1])
a1="홍길동"
a2="hong@nate.com"
a3="M"
a4=(a1,a2,a3)
print(a4)
listdata={100,200,300,200,100,600,700}
print(listdata)

listdata2={"홍길동","이순신","홍길동","강감찬"}
print(listdata2)

#[]:중복된것도 나옴 
listdata3=[100,200,300,200,600,200,500] #append, insert
listdata6=set([100,200,300,200,600,200,500]) #set을 적용시 []=> {}인식시

#주의사항이 필요함 
listdata6.add(800)
listdata6.remove(200)
print(listdata6)
print(listdata3)


listdata3_1 ={100,200,300,200,600,200,500}
listdata4 = set([300,200])
#set:교집합사용시 주의할점 비교 배열{}이며, set[]로 표현
print(listdata3_1 & listdata4) # & 3_1과 4배열 중 4번 배열을 기준으로 3_1의 값을 가져옴
print(listdata3_1.intersection(listdata4))

print(listdata3_1 | listdata4) #합집합
print(listdata3_1.union(listdata4)) #union | 기호로 대체되었음

print(listdata3_1 - listdata4) #차집합
print(listdata3_1.difference(listdata4)) #difference -기호로 대체되었음

box={"블랙커피","아메리카노"}
box2=["블랙커피","아메리카노"]
box3={"product":"블랙커피","money":3500}

print(type(box)) #set
print(type(box2)) #list

#set을 list로
box=list(box)
print(box)

#list를 set으로 
box2=set(box)
print(box2)

#값만 뽑아내기
box3=list(box3.values())
print(box3)


