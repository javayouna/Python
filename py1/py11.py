#pickle:json같은 데이터 객체파일
import pickle


data={"고객명":"홍길동","나이":25,"취미":["볼링","축구","야구"]}


files = open("file.pickle","wb") # w = wb파일 생성 및 저장(인코딩이 별도로 필요하지 않음)
print(data)
pickle.dump(data,files) #dump 객체를 생성 및 저장
files.close()


#2번째 방법=>with 이건됨
with open("file.pickle","wb") as files:
    pickle.dump(data,files)
    
with open("file.pickle","rb") as files2:
   loadfile= pickle.load(files2)    
print(loadfile)    

#txt 파일저장하는형태..
with open("abc.txt","w") as textfile:
    textfile.write(data)
