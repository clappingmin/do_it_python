import sqlite3

def create_conn():
    conn=sqlite3.connect('sqlite/my_books.db')
    return conn

#테이블 생성
def create_table():
    with create_conn() as conn:
        conn = create_conn()
        c=conn.cursor()
        sql='''
                create table if not exists books(
                    title text,
                    published_date text,
                    publisher text,
                    pages integer,
                    recommend integer
                )'''
        c.execute(sql)
        conn.commit()
        c.close()

def insert_book(item):
    conn= create_conn()
    c= conn.cursor()
    sql ='insert into books values(?,?,?,?,?)'
    c.execute(sql,item)
    conn.commit()
    c.close()
    conn.close()

def insert_books(items):
    conn=create_conn()
    c=conn.cursor()
    sql ='insert into books values(?,?,?,?,?)'
    c.executemany(sql,items)
    conn.commit()
    c.close()
    conn.close()

def all_books():
    conn=create_conn()
    c=conn.cursor()
    sql = 'select * from books'
    c.execute(sql)
    books = c.fetchall()
    # print(books) #리스트안에 tuple
    return books

def one_book(title):
    conn = create_conn()
    c=conn.cursor()
    sql = "select * from books where title = ?"
    c.execute(sql,title)
    book = c.fetchone()
    return book

def select_book(title):
    conn = create_conn()
    c=conn.cursor()
    sql="select * from books where title like ?"
    title = "%"+title+"%"
    c.execute(sql,(title,))
    book = c.fetchone()
    return book



if __name__ =='__main__' :
    create_table()
    item = ('데이터분석실무','2020-07-13','위키북스',302,10)
    insert_book(item)
    items=[
        ('빅데이터','2020-07-15','위키북스',302,10),
        ('안드로이드','2020-05-18','오렌지미디어',405,20),
        ('spring','2020-09-13','오렌지미디어',201,8)
    ]
    insert_books(items)
    all_books()

    book = one_book(('빅데이터',)) #title이 tuple형태임
    print(book)
    
    book = select_book('안드로이드')
    print(book)

