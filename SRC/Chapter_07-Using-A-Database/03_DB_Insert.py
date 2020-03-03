import mysql.connector

dbconfig = {
    "host": "127.0.0.1",
    "user": "vsearch",
    "password": "hello",
    "database": "vsearchlogDB",
}

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()

_SQL = """insert into log
        (phrase, letters, ip, browser_string, results)
        values
        ('hitch-hiker', 'aeiou', '127.0.0.1', 'FireFox', "{'e', 'i'}")"""
cursor.execute(_SQL)
conn.commit()

_SQL = """select * from log"""
cursor.execute(_SQL)
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
