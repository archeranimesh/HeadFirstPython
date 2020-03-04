import mysql.connector

dbconfig = {
    "host": "127.0.0.1",
    "user": "vsearch",
    "password": "hello",
    "database": "vsearchlogDB",
}

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()
_SQL = """select * from log"""
cursor.execute(_SQL)
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
