#pysqlite3, pysqlite2, pysqlite, sqlite3
from sqlite3 import * #pip install pysqlite3
from dbconnect import *

cur =connect.cursor() #명렁어를 입력시키기위한 대기상태

cur.execute("select * from test3") #execute: 콘솔상태 문자값 입력
for a in cur.fetchall(): #fetchall:select에 data를 문자열로 입력함
    print(a)

#cur.execute("insert into test3 values ('0','song','aaa111','송아지','01022224444','33')")    
#java같이 사용하는 방법
sql="insert into test3 values ('0',%s,%s,%s,%s,%s)"
#with를 이용해서 여러개 데이터를 한꺼번에 저장, 수정, 삭제할 수 있음 
with connect:
    cur.execute(sql,('red','red1234','레드사용자','01022223333','55'))
    cur.execute(sql,('blue','blue1234','블루사용자','01022223333','45'))
    cur.execute(sql,('orange','orange1234','오렌지사용자','01022223333','45'))
    connect.commit() 
#이거없으면 실제 데이터베이스에 안들어감
#delete를 바로 해버리는 파이썬 특유의 행동 부분

'''
#책에는 이렇게 많이 나와있음
con=connect("./test.db")
create=con.cursor()
create.execute("create table test(idx int(4) not null,name varchar(200) not null,primary key(idx))")

insert = con.cursor()
insert.execute("insert into test values ('0','hong');")
'''