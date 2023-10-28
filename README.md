
# WhatsApp Scheduled Messages

This project sends scheduled messages via the WhatsApp Business API.

## Installation

1. Clone the repository.
2. Set up your WhatsApp Business API account and obtain your credentials. - https://developers.facebook.com/apps
3. Update the `config.py` file with your credentials.

## Usage

1. Add the messages you want to send to the `ScheduledMessages` table in the `scheduled_messages.db` SQLite database.
2. You can create `scheduled_messages` database and `ScheduledMessages` table in the `database_setup.py` file. 
3. Run the `send_scheduled_messages.py` script to continuously check the database for messages to send.

## Files

- `config.py`: Contains the configuration variables for the WhatsApp Business API.
- `send_scheduled_messages.py`: Sends the scheduled messages via the WhatsApp Business API.
- `whatsapp_messaging.py`: Contains the `send_message` function to send messages via the WhatsApp Business API.
- `scheduled_messages.db`: SQLite database to store the scheduled messages.

## Credits

This project was created by [Mayank Malhotra].

