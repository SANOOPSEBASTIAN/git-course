import pandas as pd, psycopg2
conn=psycopg2.connect(
    dbname="study",
    user="postgres",
    password="root",
    host="localhost",
    port="5432",
)
#read csv file
df=pd.read_csv(r'D:\SanoopDE\customers-1000.csv')
# Define the table schema
create_table_query = """
CREATE TABLE Customers (
    "customer id" VARCHAR(255),
    "first name" VARCHAR(255),
    "last name" VARCHAR(255),
    company VARCHAR(255),
    city VARCHAR(255),
    country VARCHAR(255),
    "phone 1" VARCHAR(255),
    "phone 2" VARCHAR(255),
    email VARCHAR(255),
    "subscription date" VARCHAR(255),
    website VARCHAR(255)
)
"""

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Drop the table if it already exists
cursor.execute("DROP TABLE IF EXISTS Customers")

# Create the Customers table with the specified columns
cursor.execute(create_table_query)

# Insert DataFrame records into the PostgreSQL database
for index, row in df.iterrows():
    cursor.execute(
        'INSERT INTO Customers ("customer id", "first name", "last name", company, city, country, "phone 1", "phone 2", email, "subscription date", website) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
        (row['Customer Id'], row['First Name'], row['Last Name'], row['Company'], row['City'], row['Country'], row['Phone 1'], row['Phone 2'], row['Email'], row['Subscription Date'], row['Website'])
    )

# Commit the transaction
conn.commit()

# Close cursor and connection
cursor.close()
conn.close()