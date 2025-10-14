import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
USERNAME = 'your_email@example.com'
PASSWORD = 'your_password'

def send_email(to_address, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = USERNAME
    msg['To'] = to_address

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(USERNAME, PASSWORD)
    server.send_message(msg)
    server.quit()

if __name__ == "__main__":
    send_email('receiver@example.com', 'Test Email', 'Hello, this is a test email.')
    print("Email sent successfully.")
