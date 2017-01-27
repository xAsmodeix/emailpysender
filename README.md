emailpysender
=============

The small library for sending emails in HTML with attachments.

You must enable support for third-party apps in the settings of mail sender person.

Version: 0.0.1


Install
=======

Python 3.4+ is required.

```
pip install emailpyinstaller
```


Settings:
=========

 - SMTP_SERVER: choose gmail, outlook, mailru or yandex
 - USERNAME: your email
 - PASSWORD: your password
 - ATTACHMENT_DIR: These files will be added to the letter, and if the directory is empty, not added
 - MESSAGE_CONF: subject(subject letter -> title letter)
 - EMAIL_LIST: TXT file with the recipient's mailbox, supports one mailbox for the line
 
 
 
Quickstart
==========

```python
from emailpysender import Sender

# names html files(with css in header) in configs directory
mail_names = ['mail', 'mail2']

# The class Sender get html filename(without ".html") and read/send file to persons in email_list.txt
# and add attacments in ditectory "config/attachments"
# You can change directory in settings.py
for file in mail_names:
    send = Sender(file)
    send.send_mail()
    
```

Contributions
=============

I wait your pull requests and I want to make the library better.

What can be done?

 - Write some tests 
 - change architecture
 - write/rewrite methods
 - update readme and docs


Example letter
==============

![Preview](https://github.com/serbernar/emailpysender/blob/master/pic.jpg "Example email letter")
