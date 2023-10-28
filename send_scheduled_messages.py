import sqlite3
import whatsapp_messaging  # Assuming this is the name of your file from Task 1
import time
from datetime import datetime, timedelta

import sqlite3
import time
from datetime import datetime
import whatsapp_messaging

def send_scheduled_messages():
    """
    Continuously checks the ScheduledMessages table in the SQLite database for messages that are scheduled to be sent.
    If a message is due to be sent, it sends the message via the WhatsApp Business API and updates the Status column in the database.
    This function runs indefinitely until it is manually stopped.
    """
    while True:  # Infinite loop to keep checking the database
        # Step 1: Connect to the SQLite database
        conn = sqlite3.connect('scheduled_messages.db')
        c = conn.cursor()
        
        # Get the current time in the same format as in the database
        current_time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Step 2: Query the ScheduledMessages table to retrieve the messages
        c.execute("""
            SELECT * FROM ScheduledMessages
            WHERE Status = 'Scheduled' AND ScheduledTime <= ?
        """, (current_time_str,))
        messages = c.fetchall()
        
        if not messages:
            print(f"No messages to send at {current_time_str}.")
        else:
            for message in messages:
                message_id, recipient_number, message_text, scheduled_time, status = message
                
                # Step 3: Send each message via the WhatsApp Business API
                whatsapp_messaging.send_message(recipient_number, message_text)  # Reusing the send_message function
                
                # Step 4: Update the Status column in the database
                c.execute("UPDATE ScheduledMessages SET Status = 'Sent' WHERE MessageID = ?", (message_id,))
                conn.commit()  # Commit the change to the database
        
        # Find the time of the next message in the queue
        c.execute("""
            SELECT MIN(ScheduledTime) FROM ScheduledMessages
            WHERE Status = 'Scheduled'
        """)
        next_message_time_str = c.fetchone()[0]
        if next_message_time_str:
            next_message_time = datetime.strptime(next_message_time_str, '%Y-%m-%d %H:%M:%S')
            time_until_next_message = next_message_time - datetime.now()
            minutes_until_next_message = time_until_next_message.total_seconds() / 60
            print(f"Next message in queue after {minutes_until_next_message:.2f} minutes.")
        
        # Close the connection to the database
        conn.close()
        
        # Sleep for 60 seconds before checking again
        time.sleep(60)

# Call the function to send the scheduled messages
send_scheduled_messages()