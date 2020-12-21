import os
import smtplib

def build_env():
    from dotenv import load_dotenv
    load_dotenv('./.env')

    return {
        'G_ACCT': os.getenv("GMAIL_ACCT"),
        'G_PW':   os.getenv("GMAIL_PW"),
        'G_PORT': os.getenv("GMAIL_PORT"),
        'ORG':    os.getenv("ORG"),
        'YEAR':   os.getenv("YEAR")
    }

def get_body():
    email = ''
    with open('email.txt', 'r') as file:
        email = email + file.read()
    return email

def get_header(
        to_addr_list, 
        cc_addr_list,
        subject,
    ):
    e = build_env()
    header  = '''
    From: {f}
    To: {t}
    Cc: {cc}
    Subject: {s}\n\n'''.format(
        f  = e['G_ACCT'],
        t  = ','.join(to_addr_list),
        cc = ','.join(cc_addr_list),
        s  = subject,
    )
    return header

def get_updated_body():
    e = build_env()
    body = get_body()
    return body.format(min='15', max='20', yr=e['YEAR'], org=e['ORG'])

def main():
    try:
        # First, doing the building blocks
        e       = build_env()
        to      = [e['G_ACCT']]
        subject = 'EMAILING MYSELF'
        header  = get_header(to, to, subject)
        message = get_updated_body()

        # Second, put it all together
        email  = header + message

        # Finally send email
        send_email(email, to)
        return True
    except:
        print('failed')
        return False

def send_email(email, to_addr_list):
    # Get local variables
    e = build_env()

    # Send the prepped email
    try:
        server = smtplib.SMTP(e['G_PORT'])
        server.starttls()
        server.login(e['G_ACCT'], e['G_PW'])
        problems = server.sendmail(
            e['G_ACCT'], 
            to_addr_list, 
            email
        )
        server.quit()
        print('passed')
        return True
    except OSError as e:
        print(e)
        print('\tUhoh! Email not sent!')
        print('\tThe username/password might be the issue...')
        print('\tBut more than likely, the `less secure` setting in the respective google account needs to be turned on')
        return False

### ### ### ### ### ### ### ### ### ### 
#                                     #
#             TEST CASES              #
#                                     #
### ### ### ### ### ### ### ### ### ### 
def test_body():
    # First test that we are simply reading from file
    email = get_body()
    assert len(email) > 1

    # Second, test that file mods work right
    email = get_updated_body()
    assert len(email) > 1
    assert email.find('{yr}') == -1
    return 

def test_header():
    to = 'foo'
    subject = 'a subj'
    header  = get_header([to], [to], subject)
    assert len(header) > 1
    assert header.find(to) > -1
    assert header.find(subject) > -1


def test_env():
    e = build_env()

    assert len(e['G_ACCT']) > 0
    assert len(e['G_PW']) > 0
    assert len(e['G_PORT']) > 0
    assert len(e['ORG']) > 0
    assert len(e['YEAR']) > 0
    return

def test_server():
    try:
        e = build_env()
        server = smtplib.SMTP(e['G_PORT'])
        server.starttls()
        server.quit()
        return True
    except:
        return False


if __name__ == '__main__':
    test_env()
    test_body()
    assert test_server() == True
    test_header()

    assert main() == True
