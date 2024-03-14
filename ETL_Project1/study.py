import pandas
import psycopg2

conn=psycopg2.connect(
        user="postgres",
        password="root",
        host="localhost",
        port="5432",
        dbname="study"
        )
cursor = conn.cursor()
conn.autocommit = True
cursor.execute("CREATE TABLE Employees(sl_no SERIAL PRIMARY KEY, emp_name VARCHAR(255), salary INT, years_of_exp INT)")
conn.autocommit = False
conn.commit()