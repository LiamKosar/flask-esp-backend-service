import smtplib
import os

# Sends a notification email to the specified recipient
def send_email(recipient:str, subject:str, message_body:str):

    EMAIL = os.getenv('EMAIL')
    PASSWORD = os.getenv('EMAIL_APP_PASSWORD')
    auth = (EMAIL, PASSWORD)
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
 
    
    from_addr = auth[0]
    to_addrs = [recipient]

    subject = subject
    body = message_body

    # Construct the email message
    msg = f"Subject: {subject}\nFrom: {from_addr}\nTo: {', '.join(to_addrs)}\n\n{body}"

    server.sendmail(auth[0], to_addrs, msg)