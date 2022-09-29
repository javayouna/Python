import pickle as io #파일 저장, 읽기
#wb:저장 


#w:텍스트저장(write)
#wb:저장(dump)+ 바이너리
#r:텍스트읽기(read)
#rb:읽기(load)+ 바이너리
pf = open("array.txt","w")

#문자전용
data="홍길동님 ㅋㅋ"
pf.write(data)
pf.close()

pf2= open("array2.txt","wb")
data2=[1,2,3,4,5]
io.dump(data2,pf2)
pf2.close()

rf=open("array2.txt","rb")
result=io.load(rf)
print(result)
rf.close()

#io.dump(data,pf)
#data=[1,2,3,4,5]
#print(pf)