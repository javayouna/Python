#DB연결
from sqlite3 import *
from MySQLdb import *

con=connect(
    user="moko2",
    passwd="spdlxlqm2@",
    host="umj7-009.cafe24.com",
    db="moko2",
    charset="utf8" #mysql콘솔에서 \status
    )

cur=connect.cursor()
sql="select * from 테이블명"
cur.execute(sql)
#select에서 fetchall함수를 이용해서 loop가 작동되도록
for z in cur.fetchall():
    print(z)
    
delsql="delete from 테이블명 where 고유필드컬럼= '고유값'"
cur.execute(delsql)
con.commit() #commit()꼭 있어야함

#insert,updata
insql="insert into 테이블명 values ()"
cur.execute(delsql)
con.commit() #commit()꼭 있어야함