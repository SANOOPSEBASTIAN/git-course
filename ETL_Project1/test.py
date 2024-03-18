import pandas as pd
from sqlalchemy import create_engine

# Configuration for PostgreSQL connection
username = 'postgres'
password = 'root'
host = 'localhost'
port = '5432'
database = 'study'

# Create the connection string
connection_str = f'postgresql://{username}:{password}@{host}:{port}/{database}'

# File path to your CSV
csv_file_path = 'C:\\Users\\USER\\git-course\\ETL_Project1\\data.csv'

# Read CSV into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Connect to PostgreSQL
engine = create_engine(connection_str)

# Insert data into PostgreSQL table
df.to_sql('data', engine, if_exists='replace', index=False)

# Close the connection
engine.dispose()

print("CSV data inserted into PostgreSQL successfully!")