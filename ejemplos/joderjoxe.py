from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from math import sqrt
from  time import sleep
import smtplib

dirDocumento="/home/dgc7/ejersiciosLibros/pyaton/ejemplos/platon.txt"
fp=open(dirDocumento,'r')
documento=fp.read()
fp.close()
print(documento)
msg=MIMEMultipart()
password = "danielgrecia12345"
msg['From'] = "danielgrecia7@gmail.com"
msg['To'] = "josemase55@gmail.com"
msg['Subject'] = "hola hoxe"
server = smtplib.SMTP('smtp.gmail.com: 587')
msg.attach(MIMEText(documento,'plain'))
server.starttls()
server.login(msg['From'],password)
for i in range(0,50):
    server = smtplib.SMTP('smtp.gmail.com: 587')
    msg.attach(MIMEText(documento,'plain'))
    server.starttls()
    server.login(msg['From'],password)
    server.sendmail(msg['from'],msg['to'],msg.as_string())
    sleep(3)
    server.quit()
    print("successfully sent email to %s:" )

