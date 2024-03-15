import pandas as pd, psycopg2
conn = psycopg2.connect(
    dbname = "study",
    user = "postgres",
    password ="root",
    host="localhost",
    port ="5432"
)
db=pd.read_csv(r"D:\SanoopDE\people-1000.CSV")

create_table_details = """
CREATE TABLE people (
    "Index" SERIAL,
"User Id" VARCHAR(255),
"First Name" VARCHAR(255),
"Last Name" VARCHAR(255),
"Sex" VARCHAR(255),
"Email" VARCHAR(255),
"Phone" VARCHAR(255),
"Date of birth" VARCHAR(255),
"Job Title" VARCHAR(255)
)
"""
cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS people")

insert_values = """
INSERT INTO people ("Index", "User Id", "First Name", "Last Name", "Sex", "Email", "Phone", "Date of birth", "Job Title")
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
#data = (row["Index"],row["User Id"],row[ "First Name"],row["Last Name"],row[Sex],row[Email],row[Phone],row["Date of birth"],row["Job Title"])


cursor.execute(create_table_details)

for index,row in db.iterrows():
    cursor.execute(insert_values,(row["Index"],row["User Id"],row[ "First Name"],row["Last Name"],row["Sex"],row["Email"],row["Phone"],row["Date of birth"],row["Job Title"]))
conn.commit()
cursor.close()
conn.close()

