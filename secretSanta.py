import random
import smtplib
'''
    
    'People' and 'hat' are lists of people THAT SHOULD BE THE SAME.
    If they are not the same, then not only is this program borken,
    but so is your secret santa.

    To make this program your own, simply add the names of the people you
    want involved. To send messages to people, add the email addresses of the people
    you would like to email, and modify the email section inside of secretSantaEmail().
    This will include 

         1. Adding your gmail account in `login`, 
         2. Adding your password to your gmail account
         3. Modifying the `message` to something of your own (right now it includes "The Java House")
         4. Modigying the Title of the email to something a bit more professional, maybe.

    Either that, or just have fun running different scenarios.

    Take note that there is secretSanta() and testCases() that have different
    lists. secretSanta() uses global lists for readability, while testCases()
    uses local lists to run the multiple tests needed for an accurate percentage
    to be returned. This is a programming thing, and nothing to be concerned
    about. Just copy and paste the two lists into secretSantaTest() if the a
    desire to run the test exists. Else, just comment it out with a '#' infront
    of the call to testCases(), located directly at the bottom.

###################################################################################
# NOTE THAT RUNNING THIS PROGRAM WITH THE print(spy) MAY RUIN THE FUN OF THE GAME  #
#    FOR PEOPLE!!!! THIS SHOULD BE COMMENTED OUT IF YOU ARE NOT A NOSY PERSON      #
##################################################################################

For the main part of the program (EMAILING PEOPE!), jump to line 85 and change
the gmail credentials that are spelled out for you! Good luck, young coder!
    
'''
people = [
    ("Tanner", 'twoody@precoa.com'),
    ('Daven', 'dsepton@precoa.com'),
    ('Tyler Brady', 'tbrady@precoa.com'),
    ('AJ', 'aruffner@precoa.com'),
    ('Brandon', 'bquinn@precoa.com'),
    ('Jason', 'jgiardino@precoa.com'),
    ('Kathy', 'kgrahn@precoa.com'),
    ('Lisa', 'lglazier@precoa.com'),
    ('Shane', 'smalan@precoa.com'),
    ('JP', 'jpnye@precoa.com'),
    ('Nick', 'nwahlin@precoa.com'),
    ('Sean', 'sgallagher@precoa.com'),
    ('Remy', 'jremy@precoa.com'),
    ('Amrit', 'asaini@precoa.com'),
    ('Jake', 'jzollinger@precoa.com'),
    ('Casey', 'csigelmann@precoa.com')
]
hat = ["Tanner", 'Daven', 'Tyler Brady', 'AJ', 'Brandon', 'Jason', 'Kathy', 'Lisa', 'Shane', 'JP', 'Nick', 'Sean', 'Remy', 'Amrit', 'Jake', 'Casey']
length = len(hat)

def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

def testNames():
      print("CHECKING THAT THE NAMES ARE THE SAME; IF NOT, WE FAIL HERE\n")
      for i in range (0, length):
            print("\t"+people[i][0]+" should be the same as "+hat[i])
            assert people[i][0] == hat[i]
      print("\nALL OF THE NAMES ARE THE SAME. GOING TO COMMENCE EMAILING\n\n\n")

############################################################
############################################################
############################################################
############################################################
'''
This is the cool part of the program.

If you change the above to have everyones emails correct, you can send out
a mass email using this program to have everyone have a unique name.

The information below must be changed as well such to send the email from your
gmail account, using your gmail password. The user will also have to potentially
change their gmail accessibility settings to a lower security so that the smtp
server can access your account. This can be done by following the link:

          https://support.google.com/accounts/answer/6010255

Have fun, and Happy holidays!
'''
def secretSantaEmail():
      counter = 0
      spy = ''
      while( len(hat)!=0 ):
            message = "You've been chosed to participate in the Secret Santa game for The Java House!\n\n"
            matchee = random.choice(people)
            matcher = random.choice(hat)
            if matchee[0] == matcher:
                  print("\nPutting name back in hat\n")
            else:
                  body = message
                  counter+=1
                  body = body+"Draw {c}.\t{p1} picks {p2}".format(c=counter, p1=matchee[0], p2=matcher)
                  spy = spy + '\n' + body
                  addy = matchee[1]
                  sendemail(from_addr    = 'yourGmail@gmail.com',
                            to_addr_list = [addy],
                            cc_addr_list = [addy],
                            subject      = 'SECRET SANTA! OMGZ!',
                            message      = body,
                            login        = 'yourGmail@gmail.com',
                            password     = 'gmail password')
                  people.remove(matchee)
                  hat.remove(matcher)
            if ((matchee[0] == matcher)&(len(hat)==1)):
                  print("\n\nTHIS ONE IS BROKEN!!!\n")
                  break
      print(spy)

#secretSantaEmail()

############################################################
############################################################
############################################################
'''
The rest of the stuff below is just fun factual stuff to see stats and to see
the functions core process and random factor.
'''
def secretSanta():
      counter = 0
      spy = ''
      while( len(hat)!=0 ):
            message = "You've been chosed to participate in the Secret Santa game for The Java House!\n\n"
            matchee = random.choice(people)
            matcher = random.choice(hat)
            if ((len(hat)==2)):
                  counter+=1
                  body = message
                  body = body + "Draw {c}.\t{p1} picks {p2}".format(c=counter, p1=people[0][0], p2=hat[1])
                  spy = spy + '\n' + body
                  counter+=1
                  body = message
                  body = body + "Draw {c}.\t{p1} picks {p2}".format(c=counter, p1=people[1][0], p2=hat[0])
                  spy = spy + '\n' + body
                  break
            elif matchee[0] == matcher:
                  print("\nPutting name back in hat\n")
            else:
                  body = message
                  counter+=1
                  body = body + "Draw {c}.\t{p1} picks {p2}".format(c=counter, p1=matchee[0], p2=matcher)
                  spy = spy + '\n' + body
                  addy = matchee[1]
                  people.remove(matchee)
                  hat.remove(matcher)
      print(spy)
            
############################################################
############################################################
############################################################
############################################################
'''
The following is just a test case that can be run to see the percentages
of having a broken secret-santa. WITH MODIFICATION FOR 100 PERCENT
'''

def secretSantaTest():
      people = ["Tanner", 'Daven', 'Tyler Brady', 'AJ', 'Brandon', 'Jason', 'Kathy', 'Lisa', 'Shane', 'JP', 'Nick', 'Sean', 'Remy', 'Amrit', 'Casey', 'Jake']
      hat = ["Tanner", 'Daven', 'Tyler Brady', 'AJ', 'Brandon', 'Jason', 'Kathy', 'Lisa', 'Shane', 'JP', 'Nick', 'Sean', 'Remy', 'Amrit', 'Casey', 'Jake']
      flag = True
      while( len(hat)!=0 ):
            matchee = random.choice(people)
            matcher = random.choice(hat)
            if len(hat)==2:
                  people.remove(people[0])
                  hat.remove(hat[1])
                  people.remove(people[0])
                  hat.remove(hat[0])
            elif matchee != matcher:
                  people.remove(matchee)
                  hat.remove(matcher)
            elif ((matchee == matcher)&(len(hat)==1)):
                  flag = False
                  break
      if flag == False:
            return 0
      else:
            return 1


def testCases():
      print("\nWith modifications, that is, with a computer, this has the following stats.")
      passes = 0
      fails  = 0
      for i in range(0,10000):
            a = secretSantaTest()
            if a == 1:
                  passes += 1
            elif a ==0:
                  fails  += 1
            else:
                  print("Broke")
                  break
      print("Test passes:\t{p}\nTest fails:\t{f}".format(p=passes, f=fails))
      total = passes+fails
      good = (passes/total)*100
      bad  = (fails/total)*100
      print("PERCENT GOOD:\t{p}\nPERCENT BAD:\t{f}".format(p=good, f=bad))

############################################################
############################################################
############################################################
############################################################
'''
The following is just a test case that can be run to see the percentages
of having a broken secret-santa. WITHOUT MODIFICATION!
'''

def BADsecretSantaTest():
      people = ["Eddie", "Matt", "Stephen","Tanner"]
      hat    = ["Eddie", "Matt", "Stephen","Tanner"]
      flag = True
      while( len(hat)!=0 ):
            matchee = random.choice(people)
            matcher = random.choice(hat)
            if matchee != matcher:
                  people.remove(matchee)
                  hat.remove(matcher)
            if ((matchee == matcher)&(len(hat)==1)):
                  flag = False
                  break
      if flag == False:
            return 0
      else:
            return 1


def BADtestCases():
      print("\nWithout modifications, that is, IRL, this has the following stats.")
      passes = 0
      fails  = 0
      for i in range(1,10000):
            a = BADsecretSantaTest()
            if a == 1:
                  passes += 1
            elif a ==0:
                  fails  += 1
            else:
                  print("Broke")
                  break
      print("Test passes:\t{p}\nTest fails:\t{f}".format(p=passes, f=fails))
      total = passes+fails
      good = (passes/total)*100
      bad  = (fails/total)*100
      print("PERCENT GOOD:\t{p}\nPERCENT BAD:\t{f}".format(p=good, f=bad))

testNames()
secretSanta()
#testCases()
#BADtestCases()
