import smtplib
import sys
import os
# CARRIERS = {
#     "att": "@mms.att.net",
#     "tmobile": "@tmomail.net",
#     "verizon": "@vtext.com",
#     "sprint": "@messaging.sprintpcs.com"
# }
 


# def send_message(phone_number, carrier, message):
#     # recipient = phone_number + CARRIERS[carrier]
#     recipient = "kosar.liam@gmail.com"
#     auth = (EMAIL, PASSWORD)
    
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login(auth[0], auth[1])
 
#     server.sendmail(auth[0], recipient, message)
 
 
# if __name__ == "__main__":
#     if len(sys.argv) < 4:
#         print(f"Usage: python3 {sys.argv[0]} <PHONE_NUMBER> <CARRIER> <MESSAGE>")
#         sys.exit(0)
 
#     phone_number = sys.argv[1]
#     carrier = sys.argv[2]
#     message = sys.argv[3]
#     send_message(phone_number, carrier, message)


def send_email(recipient, subject, message_body):

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

# send_email('kosar.liam@gmail.com', 'URGENT - Maintenance Procedure Limit', 'This task is overdue!')
