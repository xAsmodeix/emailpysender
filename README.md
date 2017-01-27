emailpysender
=============

Small library for sending html emails with attachments.

You must enable support for third-party apps in the settings of mail.

Settings:
=========

 - SMTP_SERVER: choose gmail, outlook, mailru or yandex
 - USERNAME: your email
 - PASSWORD: your password
 - ATTACHMENT_DIR: These files will be added to the letter, and if the directory is empty, not added
 - MESSAGE_CONF: subject(subject letter -> title letter)
 - EMAIL_LIST: TXT file with the recipient's mailbox, supports one mailbox for the line


Example
=======

![Prewiew](https://github.com/serbernar/emailpysender/blob/master/pic.jpg "Example")
