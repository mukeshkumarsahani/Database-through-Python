import mysql.connector as sql

mydb=sql.connect(host='localhost', user='root', password='*****')

print(mydb.connection_id)