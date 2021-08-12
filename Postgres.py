import psycopg2


conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="0000",
)

# print(conn)
cur = conn.cursor()

# print(cur)

res = cur.execute("SELECT id, username FROM users;")
print(res)

users = cur.fetchall()
print(users)

res = cur.execute("CREATE TABLE CUSTOMERS(ID INT NOT NULL, NAME VARCHAR(20) NOT NULL, AGE  INT NOT NULL, ADDRESS  CHAR (25) ,SALARY   DECIMAL (18, 2), PRIMARY KEY (ID));")
print(conn.commit())


conn.close()