import sqlite3

def query_database():
    # Connect to the database
    conn = sqlite3.connect('scheduled_messages.db')

    # Create a cursor object to execute SQL commands
    c = conn.cursor()

    # Execute a SQL query
    c.execute("SELECT * FROM ScheduledMessages")

    # Fetch all rows from the result of the query
    rows = c.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the connection
    conn.close()

# Call the function to execute the query
query_database()
