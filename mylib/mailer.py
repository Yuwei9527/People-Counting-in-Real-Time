import smtplib, ssl

class Mailer:

    """
    This script initiaties the email alert function.

    """
    def __init__(self):
        # Enter your email below. This email will be used to send alerts.
        # E.g., "email@gmail.com"
        self.EMAIL = ""
        # Enter the email password below. Note that the password varies if you have secured
        # 2 step verification turned on. You can refer the links below and create an application specific password.
        # Google mail has a guide here: https://myaccount.google.com/lesssecureapps
        # For 2 step verified accounts: https://support.google.com/accounts/answer/185833
        self.PASS = ""
        self.PORT = 465
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', self.PORT)

    def send(self, mail, cc, mode): # mode0: 無CC, mode1:有CC
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', self.PORT)
        self.server.login(self.EMAIL, self.PASS)
        # message to be sent
        SUBJECT = 'ALERT!'
        TEXT = f'People limit exceeded in your building!'
        # message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        if mode == 0:
            message = 'From: {}\r\n'.format(self.EMAIL) + 'To: {}\r\n'.format(mail) + 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        elif mode == 1:
            message = 'From: {}\r\n'.format(self.EMAIL) + 'To: {}\r\n'.format(mail) + 'CC: {}\r\n'.format(cc) + 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

        # sending the mail
        self.server.sendmail(self.EMAIL, mail, message)
        self.server.quit()
