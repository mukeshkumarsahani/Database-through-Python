import mysql.connector as sql
mydb=sql.connect(host='localhost', user='root', password='*****',database ='db1')

cur = mydb.cursor()

s="create table book(book_id integer(4), title varchar(20),price float(5,2))"
cur.execute(s)