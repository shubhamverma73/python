import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="python",
    port=3306
)

print("Connected successfully")
conn.close()