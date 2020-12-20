import os
import smtplib
from dotenv import load_dotenv

def sendEmail(
        to_addr_list, 
        cc_addr_list,
        subject,
        message,
    ):
    # Get local variables
    G_ACCT = os.getenv("GMAIL_ACCT")
    G_PW = os.getenv("GMAIL_PW")
    G_PORT = os.getenv("GMAIL_PORT")

    # Build out the email
    header  = '''
    From: {f}
    To: {t}
    Cc: {cc}
    Subject: {s}\n\n'''.format(
        f  = G_ACCT,
        t  = ','.join(to_addr_list),
        cc = ','.join(cc_addr_list),
        s  = subject,
    )
    email = header + message
    print(email)
    # Send the prepped email
    #server = smtplib.SMTP(G_PORT)
    #server.starttls()
    #server.login(G_ACCT, G_PW)
    #problems = server.sendmail(G_ACCT, to_addr_list, email)
    #server.quit()
    return

def test_email():
    sendEmail(['bar'], ['baz'], 'subj', 'message')

def test_env():
    print('called')
    G_ACCT = os.getenv("GMAIL_ACCT")
    G_PW = os.getenv("GMAIL_PW")
    G_PORT = os.getenv("GMAIL_PORT")
    assert len(G_ACCT) > 0
    assert len(G_PW) > 0
    assert len(G_PORT) > 0
    return

def test_msg():
    email = ''
    with open('email.txt', 'r') as file:
        email = email + file.read()
    assert len(email) > 1
    return 


if __name__ == '__main__':
    load_dotenv('./.env')
    print('Starting tests')
    test_email()
    test_env()
    test_msg()
