# Telegram Message Scraper & Email Notifier

This Python script monitors specific Telegram channels for messages containing predefined keywords and sends an email notification whenever a matching message is detected. The script also saves these messages to a text file and clears the message list daily at midnight.

## Features

- **Keyword Monitoring**: Monitors specified Telegram channels for messages containing the keywords "BUY", "TP", and "SL".
- **Case-Insensitive Search**: The keyword search is case-insensitive, so it detects both uppercase and lowercase variations.
- **Email Notifications**: Sends an email containing the matching messages. The email subject includes the name of the Telegram channel from which the message originated.
- **Daily Message Clearing**: Automatically clears the list of matching messages every day at midnight.
- **Message Logging**: Appends all matching messages to a text file (`messages.txt`) with proper UTF-8 encoding.

## Requirements

- Python 3.7+
- Telethon
- smtplib
- schedule

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/telegram_scrapper.git
   cd telegram_scrapper

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install the required Python packages**:
   ```bash
   pip install -r requirements.txt

4. **Usage**:
   ```bash
   python telegram_scrapper.py

## Set up your Telegram API credentials:

Obtain your api_id and api_hash from the Telegram API and replace the placeholder values in the script.

Set up your email credentials:
Replace the placeholders with your email credentials (email_from, email_password, and email_to) in the script.

## Script Behavior:

The script will start monitoring the specified Telegram channels.
It checks for new messages every 1 minute.

Message Detection: when a message containing any of the keywords (case-insensitive) is detected, it will:
 Send an email notification with the channel name in the subject.
 Save the message to messages.txt.

## Daily Maintenance:

The list of matching messages is cleared daily at midnight to ensure a fresh start each day.

UTF-8 Encoding:
The script ensures that all messages are saved with UTF-8 encoding to handle special characters correctly.

Additional Notes:
Handling Lowercase and Uppercase Keywords: The script automatically converts messages to lowercase before checking for keywords, ensuring that both "BUY" and "buy" (or any other variations) are detected.

Email Subject Customization: The email subject is dynamically generated to include the name of the Telegram channel where the matching message was found.
