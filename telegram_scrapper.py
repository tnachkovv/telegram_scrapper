from telethon import TelegramClient, events
import asyncio
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
from datetime import datetime

# Replace these with your values
api_id = '######################'
api_hash = '############'
channels = ['##############','#######']  # List of channels to monitor

# Email credentials and settings
email_from = '####################'
email_password = '#################'
email_to = '###################'
email_subject = 'New Telegram Messages Alert'

# Create the client and connect
client = TelegramClient('session_name', api_id, api_hash)

# List to hold matching messages
matching_messages = []


# Function to send an email
def send_email(messages, channel_name):
    try:
        # Set up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_from, email_password)

        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = email_to
        msg['Subject'] = f'New Telegram Messages Alert from {channel_name}'  # Include channel name in the subject
        body = "\n\n".join(messages)
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server.sendmail(email_from, email_to, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to write messages to a file and send email
def process_messages():
    if matching_messages:
        with open('messages.txt', 'a', encoding='utf-8') as f:  # Use UTF-8 encoding
            for message in matching_messages:
                f.write(message + '\n')
        matching_messages.clear()

# Function to check messages
@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    message = event.raw_text.lower()  # Convert the entire message to lowercase
    keywords = ['buy', 'tp', 'sl']  # Define keywords in lowercase
    if any(keyword in message for keyword in keywords):
        channel_name = event.chat.title if event.chat else 'Unknown Channel'
        matching_messages.append(message)  # Append the original message (preserving case)
        send_email([message], channel_name)  # Send email with the channel name


# Function to clear messages daily
def clear_messages_daily():
    global matching_messages
    matching_messages.clear()
    print(f"Messages cleared at {datetime.now()}")


# Function to schedule clearing messages daily
def schedule_daily_clearing():
    schedule.every().day.at("00:00").do(clear_messages_daily)
    while True:
        schedule.run_pending()
        time.sleep(1)


async def main():
    # Start the client
    await client.start()

    # Debugging: Check if channels can be resolved
    for channel in channels:
        try:
            await client.get_input_entity(channel)
            print(f"Successfully resolved {channel}")
        except ValueError:
            print(f"Cannot find any entity corresponding to \"{channel}\"")

    # Start the scheduling in a separate thread to avoid blocking
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, schedule_daily_clearing)

    # Periodically process messages
    while True:
        process_messages()
        await asyncio.sleep(60)  # Wait for 1 minute


with client:
    client.loop.run_until_complete(main())

