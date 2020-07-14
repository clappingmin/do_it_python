import sqlite3

conn = sqlite3.connect('sqlite/example.db')
c = conn.cursor()

#create table

c.execute('''CREATE TABLE if not exists stocks (date text, trans text, symbol text, qty real, price real)''')

#insert a row of data

c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

#save changes(commit)

conn.commit()
conn.close()