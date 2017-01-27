from .settings import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from multiprocessing.dummy import Pool as ThreadPool
from premailer import Premailer


class Sender:
    servers = {
        'gmail': {'host': 'smtp.gmail.com', 'port': '587'},
        'mailru': {'host': 'smtp.mail.ru', 'port': '465'},
        'yandex': {'host': 'smtp.yandex.ua', 'port': '465'},
        'outlook': {'host': 'smtp-mail.outlook.com', 'port': '587'},
    }

    @staticmethod
    def compress_html(filename):
        with open(CONFIG_DIR + '/' + filename + '.html', 'r', encoding='utf-8') as f:
            new_html = Premailer(f.read())
            html = new_html.transform()
        return html

    def __init__(self, html_file):
        if '' in list(SENDER['default'].values()) + [EMAIL_LIST, SMTP_SERVER]:
            raise Exception('Please, configure settings.')
        self.server_name = self.servers[SMTP_SERVER]
        self.html_file = html_file
        self.email_list = EMAIL_LIST
        self._username = SENDER['default'].get('USERNAME')
        self._password = SENDER['default'].get('PASSWORD')
        self.subject = MESSAGE_CONF['subject']
        self.user = MESSAGE_CONF['from']
        self.attachments = os.listdir(os.path.join(BASE_DIR, 'configs', 'attachments'))
        self.pools = None
        if len(self.email_list) > 50:
            self.pools = 8

    def _get_email_list(self):
        return [line.strip() for line in open(self.email_list)]

    def _send_mail(self, to_addrs, msg):
        server = smtplib.SMTP(**self.server_name)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self._username, self._password)
        server.sendmail(self._username, to_addrs, msg.as_string())
        print("Email successfully sent to", to_addrs)
        server.quit()

    def _form_message(self, to_addrs):
        msg = MIMEMultipart()
        msg['Subject'] = self.subject
        msg['From'] = self.user
        msg['To'] = to_addrs
        body = MIMEText(self.compress_html(self.html_file), 'html')
        msg.attach(body)
        if self.attachments:
            for attachment in self.attachments:
                cover_letter = MIMEApplication(open(os.path.join(ATTACHMENTS_DIR, attachment), "rb").read())
                cover_letter.add_header('Content-Disposition', 'attachment', filename=attachment)
                msg.attach(cover_letter)
        try:
            return msg
        except smtplib.SMTPAuthenticationError:
            print('SMTPAuthenticationError')
            print("Email not sent to", to_addrs)

    def _sender(self, to_addr):
        self._send_mail(to_addr, self._form_message(to_addr))

    def send_mail(self):
        if self.pools:
            pool = ThreadPool(self.pools)
            pool.map(self._sender, self._get_email_list())
            pool.join()
            pool.close()
        else:
            for to_addr in self._get_email_list():
                self._sender(to_addr)
