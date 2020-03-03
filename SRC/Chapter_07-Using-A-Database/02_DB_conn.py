import mysql.connector

dbconfig = {
    "host": "127.0.0.1",
    "user": "vsearch",
    "password": "hello",
    "database": "vsearchlogDB",
}

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()

_SQL = """describe log"""
cursor.execute(_SQL)
res = cursor.fetchall()
for row in res:
    print(row)

cursor.close()
conn.close()
