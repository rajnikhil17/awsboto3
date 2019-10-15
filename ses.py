import boto3
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

client = boto3.client('ses')


message = MIMEMultipart()
message['Subject'] = 'From API ---- Sublime Text'
message['From'] = 'XXXXXXXXXXXXXXXXXXXXXx'
message['To'] = ', '.join(['XXXXXXXXXXXXXXXXXXXXX','XXXXXXXXXXXXXXXXXXXXXXX'])
# message body
part = MIMEText('email body string', 'html')
message.attach(part)
# attachment
attachment_string = 'ses.txt'
if attachment_string:   # if bytestring available
    part = MIMEApplication(str.encode('Hai, This is BOTO3 from AWS SES, I am sending you a mail '))
else:    # if file provided
    part = MIMEApplication(open(raj.txt, 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename='raj.txt')
message.attach(part)
response = client.send_raw_email(Source=message['From'],Destinations=['XXXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXXXXXXXX'],RawMessage={'Data': message.as_string()})