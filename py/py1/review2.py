#배열형태의 데이터 {} []
a=10
b=20
c=30
array=[a,b,c]
print(array)
print("---------------------------------")
adata1=[1,2,3]
adata2=[100,200,300]
adata3=[adata1, adata2] #[[1, 2, 3], [100, 200, 300]]
#extend 사용할 때 신규 변수 생성 x 기존에있는 변수에 상속하고 출력하면 됨 
adata1.extend(adata2) #[1, 2, 3, 100, 200, 300]
print(adata1)
print("---------------------------------")
zdata1={1,2,3,4}
zdata2={"key1":"홍길동","key2":"이순신"}
print(zdata1) # {1, 2, 3, 4}
print("---------------------------------")
print(zdata2["key1"]) #홍길동
print("---------------------------------")
kdata1={"kdata":[1,2,3]}
print(kdata1["kdata"]) #[1,2,3]
print(kdata1.get("kdata"))#[1,2,3]
print(kdata1.keys())#dict_keys(['kdata']) >키값
print(kdata1.values())#dict_values([[1, 2, 3]]) >데이터값
print("---------------------------------")
person=("홍길동","이순신") #파이썬에만 있는 배열구조
print(person[1]) #이순신

(aa,bb,cc)=("a1","b1","c1")
print(aa)#a1



