from sqlite3 import * #pip install pysqlite3
from dbconnect import *
from random import *
#[test3. 20 21 22 지우기]

'''
#update
for a in range(20,23): #sql index 고유값 범위선정
    cur= connect.cursor()
    #해당 index값 모두 변경 되게 반복 시킴
    sql = "update test3 set mpw='pass1234' where midx='"+str(a)+"'"
    #%s 사용시 sql 문법 전체를 %s로 적용해야만 정상적으로 반영 
    cur.execute(sql)
    connect.commit()
'''
'''
#delete
cur=connect.cursor()
for b in range(20,23):
    sql="delete from test3 where midx='"+str(b)+"'"
    cur.execute(sql)
    connect.commit()
'''

#create
cur = connect.cursor()
sql="create table shopping(sidx int(4) not null AUTO_INCREMENT,sname varchar(200),primary key(sidx))"
cur.execute(sql)
    
    