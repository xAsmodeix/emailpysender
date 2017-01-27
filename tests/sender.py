from emailpysender import Sender

mail_names = ['mail', 'mail2']

for file in mail_names:
    send = Sender(file)
    send.send_mail()