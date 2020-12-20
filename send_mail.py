import os
import smtplib
from dotenv import load_dotenv

def sendEmail(
        from_addr,
        to_addr_list, 
        cc_addr_list,
        subject,
        message,
        login,
        password,
        smtpserver ='smtp.gmail.com:587'
    ):
    # Build out the email
    header  = '''
    From: {f}
    To: {t}
    Cc: {cc}
    Subject: {s}\n\n'''.format(
        f  = from_addr,
        t  = ','.join(to_addr_list),
        cc = ','.join(cc_addr_list),
        s  = subject,
    )
    email = header + message
    print(email)
    # Send the prepped email
    #server = smtplib.SMTP(smtpserver)
    #server.starttls()
    #server.login(login,password)
    #problems = server.sendmail(from_addr, to_addr_list, email)
    #server.quit()
    return

def test_email():
    sendEmail('foo', ['bar'], ['baz'], 'subj', 'message', 'login', 'pw')

def test_env():
    print('called')
    G_ACCT = os.getenv("GMAIL_ACCT")
    G_PW = os.getenv("GMAIL_PW")
    G_PORT = os.getenv("GMAIL_PORT")
    assert len(G_ACCT) > 0
    assert len(G_PW) > 0
    assert len(G_PORT) > 0
    return


if __name__ == '__main__':
    load_dotenv('./.env')
    print('Starting tests')
    test_email()
    test_env()
