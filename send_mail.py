import smtplib

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
    header  = '''From: {f}\n
    To: {t}\n
    Cc: {cc}\n
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


if __name__ == '__main__':
    print('Starting tests')
    test_email()
