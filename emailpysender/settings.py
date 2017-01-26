import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MESSAGE_DIR = os.path.join(BASE_DIR, 'message')
ATTACHMENTS_DIR = os.path.join(MESSAGE_DIR, 'attacments')

SMTP_SERVER = 'gmail'
EMAIL_LIST = 'email_list.txt'

SENDER = {
    'default': {
        'USERNAME': 'example@gmail.com',
        'PASSWORD': 'your_password',
    }
}

MESSAGE_CONF = {
    'subject': 'Приглашение!',
    'from': SENDER['default']['USERNAME'],
}
