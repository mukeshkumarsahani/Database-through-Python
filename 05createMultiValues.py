import mysql.connector as sql
mydb=sql.connect(host='localhost', user='root', password='*****',database ='db1')

cur = mydb.cursor()

s="insert into book(book_id ,title,price) values(%s,%s,%s)"

books = [(2,"php",500),(3,"java",330),(4,"C++",300),(5,"DBMS",400)]

cur.executemany(s,books)
mydb.commit()