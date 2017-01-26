from emailpysender import Sender

sender = Sender(pools=8)
sender.send_mail()
