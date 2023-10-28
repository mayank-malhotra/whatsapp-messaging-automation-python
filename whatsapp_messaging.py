import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

ph = config['DEFAULT']['phone_number']
token = config['DEFAULT']['token']
api_url = config['DEFAULT']['url']

def send_message(phone_number, message_text):
    """
    Sends a WhatsApp message to the specified phone number using the Whatsapp API.

    Args:
        phone_number (str): The phone number to send the message to, in international format (e.g. "+14155238886").
        message_text (str): The text of the message to send.

    Returns:
        None
    """
    

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    data = {
        "to": f"whatsapp:{phone_number}",
        "type": "text",
        "text": {
            "body": message_text
        },
        "messaging_product": "whatsapp"  # Add this line
    }
    
    response = requests.post(api_url, headers=headers, json=data)
    
    if response.status_code == 200:
        print(f"Message sent successfully to {phone_number}")
    else:
        print(f"Failed to send message. Status code: {response.status_code}, Error: {response.text}")


def test_send_message():
    """
    Tests the send_message function by sending a test message to the phone number specified in the config.ini file.
    """
    phone_number = config['DEFAULT']['phone_number']
    send_message(phone_number, "Hi Hello, this is a test message")


# Usage test this function
# send_message(ph, "Hi Hello, this is a second test messageees")
