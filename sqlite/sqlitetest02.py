import sqlite3

conn = sqlite3.connect('sqlite/example.db')

c = conn.cursor()
#symbol = 'RHAT' # 이렇게 쓰지 말 것 ! 
#c.execute('''
#           select * from stocks
#           where symbol = '%s' ''' %symbol)

#t = ('RHAT',) #stocks 에서 symbol = RHAT 인 것 출력 
#sql = 'SELECT * FROM stocks WHERE symbol=?'
#c.execute(sql,t)
#print(c.fetchone())

# Larger example that inserts many records at a time
"""
#반영된 data 
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]

c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases) # 한 번에 여러개 실행 executemany
conn.commit()
conn.close()
"""

sql = "select * from stocks order by price"

# c.execute(sql)
# rows=c.fetchall()
# print(type(rows))

# for row in rows:
#     print(row)
#     print(row[0])
    

for row in c.execute(sql):
    print(type(row))
    print(row[0])

c.close()
conn.close