import mysql.connector as sql
mydb=sql.connect(host='localhost', user='root', password='*****',database ='db1')

cur = mydb.cursor()

s="insert into book(book_id ,title,price) values(%s,%s,%s)"
b1 = (1,"python3",500)

cur.execute(s,b1)
mydb.commit()