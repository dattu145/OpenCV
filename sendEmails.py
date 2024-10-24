import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "daddyphone145233@gmail.com"
    msg['from'] = user
    passwd = "dkmymwirgissmqqy"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user,passwd)
    server.send_message(msg)

    server.quit()

    with open("result.png", 'rb') as f:
        time.sleep(10)
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename="thiefs.jpg")
if __name__ == '__main__':
    email_alert("Hey python", "Hello Guys this is dattu", "sridharreddy145233@gmail.com")
