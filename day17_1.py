# Day 17
# Task 1
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='prem18',
)
cur = mydb.cursor()
cur.execute("SELECT VERSION()")
data = cur.fetchone()
print("DBMS Version:", str(data))