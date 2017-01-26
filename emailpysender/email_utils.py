import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import premailer
from emailpysender.settings import *


class Sender:
    servers = {
        'gmail': ['smtp.gmail.com', '587'],
        'mail': ['smtp.mail.ru', '465'],
        'yandex': ['smtp.yandex.ua', '465'],
    }

    def __init__(self):
        if '' in list(SENDER['default'].values()) + [EMAIL_LIST, SMTP_SERVER]:
            raise Exception('Please, configure settings.')
        self.server_name = self.servers[SMTP_SERVER]
        self.email_list = EMAIL_LIST
        self._username = SENDER['default'].get('USERNAME')
        self._password = SENDER['default'].get('PASSWORD')
        self.subject = MESSAGE_CONF['subject']
        self.user = MESSAGE_CONF['from']

    def _get_email_list(self):
        return [line.strip() for line in open(self.email_list)]

    def _send_mail(self, to_addrs, msg):
        server = smtplib.SMTP(*self.server_name)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self._username, self._password)
        server.sendmail(self._username, to_addrs, msg.as_string())
        server.quit()

    def form_message(self, to_addrs, attachmens=None):
        msg = MIMEMultipart()
        msg['Subject'] = self.subject
        msg['From'] = self.user
        msg['To'] = to_addrs
        body = MIMEText(self.compress_html('index.html'), 'html')
        msg.attach(body)
        if attachmens:
            for attachment in os.listdir(ATTACHMENTS_DIR):
                cover_letter = MIMEApplication(open(os.path.join(ATTACHMENTS_DIR, attachment), "rb").read())
                cover_letter.add_header('Content-Disposition', 'attachment', filename=attachment)
                msg.attach(cover_letter)
        try:
            print("Email successfully sent to", to_addrs)
            return msg
        except smtplib.SMTPAuthenticationError:
            print('SMTPAuthenticationError')
            print("Email not sent to", to_addrs)

    def compress_html(self, filename):
        with open('message/' + filename, 'r', encoding='utf-8') as f:
            new_html = premailer.Premailer(f.read())
            html = new_html.transform()
        return html

    def send_mail(self):
        for to_addr in self._get_email_list():
            self._send_mail(to_addr, self.form_message(to_addr, attachmens=True))
