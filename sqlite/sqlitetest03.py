#input.csv 파일을 가져다가 데이터베이스에 넣고 싶다
import sqlite3,csv
from sqlite3.dbapi2 import Cursor

input_file = 'sqlite/input.csv'

conn = sqlite3.connect('sqlite/suppliers.db')

c=conn.cursor()

#테이블이 없으니 생성
sql ='''
        create table if not exists suppliers(
            supplier_name varchar(20),
            invoice_number varchar(20),
            cost float,
            part_number varchar(20),
            purchase_date date

        )'''

c.execute(sql)
sql = "delete from suppliers"
c.execute(sql)
conn.commit()

#csv파일에서 데이터를 읽어서 테이블에 clone
file_reader = csv.reader(open(input_file,'r'),delimiter=',')
print(file_reader)

#첫라인을 읽음(제목행)
header = next(file_reader,None)
print(header)

data=[]
for row in file_reader:
    # print(type(row)) #list
    data.append(row)
print(data)
print(type(data))    

sql='insert into suppliers values(?,?,?,?,?)'
c.executemany(sql,data)
conn.commit()

c.close()
conn.close()