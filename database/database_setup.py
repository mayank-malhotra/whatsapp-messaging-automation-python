import sqlite3
from datetime import datetime, timedelta
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
mob_no = config['DEFAULT']['phone_number']

def setup_database():
    """
    Sets up the ScheduledMessages table in the scheduled_messages.db database
    and inserts some sample rows for testing purposes.
    """
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('scheduled_messages.db')

    # Create a cursor object to execute SQL commands
    c = conn.cursor()

    # Create the ScheduledMessages table
    c.execute("""
        CREATE TABLE IF NOT EXISTS ScheduledMessages (
            MessageID INTEGER PRIMARY KEY AUTOINCREMENT,
            RecipientNumber TEXT NOT NULL,
            MessageText TEXT NOT NULL,
            ScheduledTime DATETIME NOT NULL,
            Status TEXT NOT NULL
        )
    """)

    # Insert some sample rows
    sample_messages = [
        (mob_no, "Hello, this is a test message", datetime.now() + timedelta(minutes=10), "Scheduled"),
        (mob_no, "Don't forget about our meeting tomorrow", datetime.now() + timedelta(hours=1), "Scheduled"),
        (mob_no, "Happy Birthday!", datetime.now() + timedelta(days=1), "Scheduled"),
    ]

    c.executemany("""
        INSERT INTO ScheduledMessages (RecipientNumber, MessageText, ScheduledTime, Status)
        VALUES (?, ?, ?, ?)
    """, sample_messages)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Call the setup_database function to set up the database and insert sample rows
setup_database()
