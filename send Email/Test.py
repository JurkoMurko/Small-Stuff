import smtplib
from email.message import EmailMessage
import ssl
import smtplib

KW_Password = 'nppi hqke nfev tphv'
sender = 'jjanos@kw.com'
recievers = ['jjanos@kw.com', 'jurkokj@gmail.com']
subject = 'TEST w/ Sig3'

html_body = """
<p>Hi , <br><br>
I'm a new realtor in Wisconsin, but I grew up in the area (Berrien). My name is Juro, and this is me doing my lead gen. (I kinda hate it). I don’t like being salesy, so I’m going to make this short.
<br><br>
If you need a moving company we want to help you find one for FREE. Together, we’ve worked as movers in the area with multiple companies for a while now. We wanted to start our own business and thought we could help people with moving. We figured a good way to start a moving business was to first help others and build our network. So all we ask is that if you need a mover and want some advice, you send us a quick email with the job information.
<br><br>
Thank you for your time,<br>
I know it is precious,<br>
Juraj (Juro) Janos<br>
<br>
Also would it be cool if I emailed you again? Just let me know if you're not interested at all. I'd love to get your feedback on how I scripted the email and any ideas you have for us on the business or what we could do better. 
<br></p>
<img src="https://i.imgur.com/wajm5FU.png" width="420" height="122">
"""

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: 
    smtp.login(sender, KW_Password)
    for recipient in recievers:
        custom_body = html_body[0:7] + recipient.split("@")[0] + html_body[7:]  

        msg = EmailMessage()
        msg['From'] = sender
        msg['Subject'] = subject
        msg['To'] = recipient
        msg.set_content(custom_body, subtype="html")
        smtp.send_message(msg)
