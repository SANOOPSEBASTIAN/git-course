import datetime
import psycopg2

def generate_alert(transaction):
    try:
        # Establish a connection to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="Banking_Transaction",
            user="postgres",
            password="root",
            host="localhost",
            port="5432"
        )

        # Create a cursor object
        cursor = conn.cursor()

        # Get the current timestamp
        current_timestamp = datetime.datetime.now()

        # Extract transaction data
        transaction_id = transaction['transaction_id']
        amount = transaction['amount']
        transaction_type = transaction['type']
        account_id = transaction['account_id']

        # Execute SQL query to insert alert data into the database
        cursor.execute("INSERT INTO alerts (transaction_id, amount, type, account_id, timestamp) VALUES (%s, %s, %s, %s, %s)",
                       (transaction_id, amount, transaction_type, account_id, current_timestamp))

        # Commit the transaction
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # If the alert was successfully generated, print a success message
        print("Alert generated successfully.")

    except psycopg2.Error as e:
        # If an error occurs, print the error message
        print("Error generating alert:", e)

# Example transaction data
transaction_data = {
    'transaction_id': 12345,
    'amount': 100.00,
    'type': 'debit',
    'account_id': 101
}

# Generate an alert for the transaction
generate_alert(transaction_data)