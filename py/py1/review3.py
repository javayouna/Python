#파이썬 배열 중요사항 
adata={10,5,6,7,6}
print(adata) #{10, 5, 6, 7} >>중복삭제

bdata=[10,5,6,7,6]
print(bdata)#[10, 5, 6, 7, 6] >>중복데이터 출력
print("--------------------")
#for문 배열형태1
for no in bdata:
    print(no)
print("--------------------")

#for문 배열형태2
adata3={"data1":[1,2,3,4],"data2":[5,6,7,8]}
for k in adata3:
    for kk in adata3[k]:
        print(kk) #1,2,3,4,5,6,7,8
print("--------------------")

#for문 배열형태3 
#enumerate:idx 번호,배열값
adata4=[1,2,3,4,5]
for idx,no in enumerate(adata4):
    print(no)
    print(adata4[idx])
print("--------------------")
#while문
w=0
while w <5:
    print(w)
    if w==2:
        break #continue:반복순서를 넘기는형태
    w+=1 # ++,--(없음), +=,-+(+1증가)









    