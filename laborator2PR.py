import smtplib
import imaplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import email
import os
import email.encoders
import stdiomask

port = 587
host = input("Write ur Email:\n\t\t\t")
smtp_server = "smtp.gmail.com"
print("Write ur password:\n\t\t\t")
password = stdiomask.getpass()
receivers = []
imap_server = "imap.gmail.com"
home_folder = os.path.dirname(os.path.abspath(__file__))



def email_read():
    number = int(input("How many messages do you want to read?\n\t\t\t"))
    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(host, password)
    imap.select('Inbox')
    data = imap.search(None, 'ALL')
    mail_number = data[1]
    id_list = mail_number[0].split()
    first_email = int(id_list[0])
    latest_email = int(id_list[-1])
    iterator = 0
    print('----------------===================================================----------------')
    for i in range(latest_email, first_email, -1):
        data = imap.fetch(str(i), '(RFC822)')
        for response_part in data:
            arr = response_part[0]
            if isinstance(arr, tuple):
                msg = email.message_from_string(str(arr[1], 'utf-8'))
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True)
                        print("From: %s\nTo: %s\nSubject: %s\n\nBody: \n\n%s" %
                              (msg['from'], msg['to'], msg['subject'], body.decode('utf-8')))
                        print('----------------===================================================----------------')
                    else:
                        continue
        iterator += 1
        if iterator == number:
            break

    imap.close()


def email_send():
    print("Print emails u want to send a message \n\t\t\t( Just press enter after u printed all the emails )\n\t\t\t")
    while True:
        date = input("Email:\n\t\t\t")
        if date == "" or date == " ":
            break
        else:
            receivers.append(date)
    if not receivers:
        print("ERROR: No receivers!")
        exit()
    subject = input("Write ur subject\n\t\t\t")
    message = input("Write ur message\n\t\t\t")
    msg = MIMEMultipart('alternative')
    img = input("Do you want to attach image to your message?\n\t\t\t1 - Yes\n\t\t\t2 - No\n\t\t\t")
    for x in range(0, len(receivers)):
        msg['Subject'] = subject
        msg['From'] = host
        msg['To'] = receivers[x]
        msg.preamble = subject
        msg.attach(MIMEText(message))
        if img == "1":
            filename = input("Print your filename ( Ex: 'image.png' ):\n\t\t\t")
            my_file = os.path.join(home_folder, filename)
            stats = os.stat(filename)
            if stats.st_size <= 2097152:
                with open(my_file, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())

                email.encoders.encode_base64(part)

                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {filename}",
                )
                msg.attach(part)
            else:
                print("Error: Image size > 2 MB\nImage wasn't sent")
                pass
        else:
            pass

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            try:
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                server.login(host, password)
                server.sendmail(host, receivers[x], msg.as_string())
                server.quit()
                print("Email was successfully sent!")
            except smtplib.SMTPException:
                print("Failed to send a email")


Choice = input("What do you wanna do?\n\t\t\t1 - Read message from email\n\t\t\t2 - Write message\n\t\t\t")


if Choice == "1":
    email_read()
elif Choice == "2":
    email_send()
else:
    print("Wrong input")
    exit()
