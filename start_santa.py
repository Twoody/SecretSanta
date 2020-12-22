# Local Imports
import players
import send_mail

# Std Libs
import random
import smtplib

'''
Written by: Tanner Lee Woody
Original Date: 2013-12-01 (?)
Last Modified Date: 2013-12-01 (?)

Please note that you must have a GMail account in order to use this program.
If you do not have a gmail account,
then you will have to go make one before going any further.

To run this program, a few details must be included. These
details are the following:

    1. Run pip install on `requirement.txt` modules

    2. Configure .env file with GMAIL credentials, year, organization, min/max spend limits.

    3. A list of `people` need to be setup in `players.py`

    4. Check/modify `email.txt` to see what will be sent out
'''

def start_secret_santa():
    e            = send_mail.build_env()
    addy         = ''
    signature    = send_mail.get_signature()
    people       = players.people

    # Randomly mixup all the people
    random.shuffle(people)

    try:
        # First, doing the building blocks
        # TODO: Probably stash this somewhere...
        subject     = 'EMAILING MYSELF'
        message     = send_mail.get_updated_body()

        for i in range(0, len(people)):
            drawee    = people[i]
            # TODO: Probably store this somewhere + Be dynamic...
            draw_info = '\t\tDraw {i}. {p1} picks {p2}\n\t\t\tAddress: {a}\n\t\t\tLikes: {l}\n'
            # If testing, send emails to yourself initially
            to        = [drawee['email']] if not e['TESTING'] else [e['G_ACCT']]
            header    = send_mail.get_header(to, to, subject)

            # Loop around the assignment s.t. last person draws first in list
            person_drawn = people[i + 1] if i != len(people) - 1 else people[0]

            # TODO: Make ternary place holder with env option for on/off below
            # Begin formatting our data
            draw_info = draw_info.format(
                i  = str(i + 1),
                p1 = drawee['full_name'],
                p2 = person_drawn['full_name'],
                a  = person_drawn['address'],
                l  = person_drawn['likes']
            )

            # Second, put it all together
            email  = header + message + draw_info + signature
            print(email)

        # Finally send email
        #send_mail.send_email(email, to)
        return True
    except OSError:
        print('failed with gmail/server issues probs')
        return False

if __name__ == '__main__':
    start_secret_santa()
