import smtplib
from email.mime.text import MIMEText
import os

def send_email(customer,game,rating,comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '07ed82eec171bd'
    password = os.environ.get('EMAIL_PASSWORD')

    message = f'<h3> New Feedback Submission</h3>' \
              f'<ul>' \
              f'<li>Customer: {customer}</li>'\
              f'<li>Game: {game}</li>'\
              f'<li>Rating: {rating}</li>'\
              f'<li>Comments: {comments}</li>' \
              f'</ul>'
    sender_email = 'anatoliinakrukovich@gmail.com'
    receiver_email = 'evlarthas96@gmail.com'
    msg = MIMEText(message,'html')
    msg['Subject'] = 'Bethesda feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP(smtp_server,port) as server:
        server.login(login,password)
        server.sendmail(sender_email,receiver_email,msg.as_string())