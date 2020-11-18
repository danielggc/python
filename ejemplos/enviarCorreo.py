from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()

dir_Imagen='/home/dgc7/Descargas/imagen.jpg'
message = "hola sebas \n Este mensaje fue enviado con cpp digo con py"
password = "danielgrecia12345"
msg['From'] = "danielgrecia7@gmail.com"
msg['To'] = " sebcaspp@gmail.com"
msg['Subject'] = "prieba"

msg.attach(MIMEText(message, 'plain'))
fp=open(dir_Imagen,'rb')
imagen=MIMEImage(fp.read())
msg.attach(imagen)

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print("successfully sent email to %s:" )

