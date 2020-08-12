import smtplib,ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#end of imports

myemail = 'email'
port = 465  # For SSL

#starting of the the server 

server = smtplib.SMTP("smtp.gmail.com", port ) # entring the server smtp domain and port

server.ehlo() # starting the server 

#reading the password fromt a txt file " better to be encrypted one "

with open('password.txt', 'r') as f:
    password = f.read

server.login(myemail , password) # logging in 

# This link is usefull https://docs.python.org/3.4/library/email-examples.html
## Email Header 
msg = MIMEMultipart()

msg['From'] = 'Omar nazih'
msg['To'] = 'email'
msg['subject'] = 'Test'


# Reading Email Text attachment
with open('message.txt', 'r') as f:
    message = f.read

# Sending Email Text attachment
msg.attach(MIMEText(message,'plain'))

# Sending email image attachment
filename = 'ibrahim.jpg' 
attachment = open(filename,'rb') # "rb" stands for reading bytes mode 

p = MIMEBase('application' , 'octet-stream') # this is fro processing the image data
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail(myemail , 'email',text)

