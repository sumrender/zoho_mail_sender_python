import smtplib
from email.mime.text import MIMEText

def send_mail(subject, message, sender, password, recipient):
  try:
    # Body of E-mail
    email_body = MIMEText(message)
    # Subject of E-mail
    email_body['Subject'] = subject
    # Sender E-mail Id
    email_body['From'] = sender
    # Receiver E-mail Id
    email_body['To'] = recipient
    # SMTP Server
    server = smtplib.SMTP_SSL('smtppro.zoho.in', 465)
    # SMTP Server Login Credentials
    server.login(sender, password)
    # Gives Send Mail Request to SMTP Server
    server.sendmail(sender, recipient, email_body.as_string())
    # Quit or Logout from SMTP Server 
    server.quit()
    print("email sent successfully")
  except:
    print("failed to send email")