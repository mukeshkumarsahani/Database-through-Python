import mysql.connector as sql

mydb=sql.connect(host='localhost', user='root', password='*****')

cur = mydb.cursor()
cur.execute("create database db1")