import csv
import smtplib
import random
import datetime as dt
from email.message import EmailMessage
import pandas as pd

# """
# Python uses:

# MIMEMultipart
# MIMEText
# MIMEImage
# MIMEApplication    
# """
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

my_email = ".......@gmail.com"
password = "........"
now = dt.datetime.now()

#READ CSV FILE

with open("DAY-32/DOB.csv", newline='') as file:
    data = csv.DictReader(file)
    for row in data:

# Why int() Needed?
# CSV values are read as strings.
        if int(row['day']) == now.day and int(row['month']) == now.month:
            
            # Create email object
            msg = MIMEMultipart()
            
            msg["Subject"] = "Hello!!!!"
            msg["From"] = my_email
            msg["To"] = row['email']
            
            # EMAIL BODY
            with open("DAY-32/hbd.txt") as f:
                mssg = MIMEText(f.read(), 'plain')
                msg.attach(mssg)
 
            # ATTACHING IMAGE AND GIF
            with open("DAY-32/chat.png", "rb") as img1:
                image1 = MIMEImage(img1.read())
                msg.attach(image1)
                
            with open("DAY-32/batman.gif", "rb") as gif1:
                gif = MIMEImage(gif1.read())
                msg.attach(gif)
                
            with open("DAY-32/panda.gif", "rb") as gif2:
                new_gif = MIMEImage(gif2.read())
                msg.attach(new_gif)
                
            with open("DAY-32/HBD.gif", "rb") as gif3:
                new_gif_2 = MIMEImage(gif3.read())
                msg.attach(new_gif_2)    
                

                    
                
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(my_email, password)
                connection.send_message(msg)
                
                print(f"Email sent to {row['name']}")    




