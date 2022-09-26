#데이터베이스 연결
import pandas as pd
from sqlite3 import *
from dbconnect import *
from pandas.io.sas.sas_constants import column_data_length_length

sqlin =connect.cursor()
'''
sqlin.execute("select * from test3")
#1:아이디 2:패스워드 3:이름 
for data in sqlin.fetchall():
    print(data[3])
'''

#read_sql_query, read sql (pandas전용 DB연결)
#read_sql_query("sql문법","db접속정보")
sql="select * from test3"
data = pd.read_sql_query(sql,connect)
#data=data.drop(columns=['mpw','midx','mtel']) #삭제
data=data[["mid","mnm","mage"]] #pick
data=data.rename(columns={"mid":"아이디","mnm":"고객명","mage":"나이"})
data.to_csv(r"test3.csv",encoding="euc-kr") #r새로고침
print(data)