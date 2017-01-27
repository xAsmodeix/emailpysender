import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_DIR = os.path.join(BASE_DIR, 'configs')
ATTACHMENTS_DIR = os.path.join(BASE_DIR, 'configs', 'attachments')

SMTP_SERVER = 'gmail'
EMAIL_LIST = os.path.join(CONFIG_DIR, 'email_list.txt')

SENDER = {
    'default': {
        'USERNAME': 'example@gmail.com',
        'PASSWORD': 'password',
    }
}

MESSAGE_CONF = {
    'subject': 'Приглашение!',
    'from': SENDER['default']['USERNAME'],
}
