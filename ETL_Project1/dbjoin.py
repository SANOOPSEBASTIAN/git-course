import pandas as pd, psycopg2
conn=psycopg2.connect(
    dbname="study",
    user="postgres",
    password="root",
    host="localhost",
    port="5432",
)
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS dbjoin")
cursor.execute ("CREATE TABLE dbjoin (Index VARCHAR(255), country VARCHAR(255), phone VARCHAR(255), city VARCHAR(255))" )

cursor.execute("""
    SELECT customers.Index, customers.country, people.Phone, customers.city
    FROM Customers 
    INNER JOIN people ON customers.Index = people.Index
    WHERE people.Index < '6'
""")

result=cursor.fetchall()
print (result)

for row in result:
    cursor.execute("INSERT INTO dbjoin (Index, country, phone, city) VALUES (%s, %s, %s, %s)", row)

conn.commit()
cursor.close()
conn.close()