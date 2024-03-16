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
cursor.execute ("CREATE TABLE dbjoin (Index VARCHAR(255), country VARCHAR(255), phone VARCHAR(255))" )

cursor.execute("""
    SELECT customers."Index", customers.country, people."Phone" 
    FROM customers 
    INNER JOIN people ON customers."Index" = people."Index" 
    WHERE people."Index" < '6'
""")

result=cursor.fetchall()

for row in result:
    cursor.execute("INSERT INTO dbjoin (Index, country, phone) VALUES (%s, %s, %s)", row)

conn.commit()
