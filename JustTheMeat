import random
import smtplib

'''
This is the meat of the emailing program for Secret Santa.

Please note that you must have a GMail account in order to use
this program. If you do not have a gmail account, then you will
have to go make one before you should continue any execution of this
python function.

To run this program, a few details must be included. These
details are the following:

    1. A list of `people` that has nodes that are tuples.
          1.a. The first node should contain the persons name
          1.b. The second node should contain the persons email address

    2. A list of names for the `hat`. These names should be in the same order
       as the names listed in `people`.
           WARNING: IF THE NAMES ARE NOT THE SAME, AN ASSERTION ERROR WILL
                    TAKE PLACE BEFORE SENDING OUT IMPROPER EMAILS

    3. The Users login information should also be entered in the head
       of the secretSantaEmail() function. The other information should also
       be changed accordingly here (i.e. `organization`, `year`, etc.).

    4. The main message that is sent out to everyone should also be looked at.
       As it currently stands, the message is very centric to one purpose.

    5. The program will only email the user as it currently stands. To get
       of this feature, the changes to `addy` must be reestablished.
       To do this, simply delete the leading `#` on each change to addy in
       the main part of the program.

If everything is changed and modified accordingly, then this program can be
completely yours, and you can impress them with your coding skills!
'''

people = [
          ("Stephen"        ,"stephen@domain.org")           , #1
          ("Eddie"          ,"Eddie@domain.gov")             ,
          ("Matt"           ,"matt@domain.com")              , #3
          ("Tanner"         ,"tanner@domain.edu")            ,
         ]

hat    = [
          "Stephen"           , #1
          "Eddie"             ,
          "Matt"              , #3
          "Tanner"         
         ]

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



testNames()
############################################################
############################################################
############################################################
############################################################

def secretSantaEmail():
      counter      = 0
      addy         = 'yourGMAIL@gmail.com'
      usersGmail   = 'yourGMAIL@gmail.com'
      pwz          = 'sUPer DupER Secret Password'
      organization = "A Coffee Shot"
      year         = '2014'
      name         = 'John Doe'
      emailSubject = "THE REAL SECRET SANTA DRAWING!!!"
      spy     = ''#This should be used just for testing. The print statement should be commented out below
      msg2    = "You've been chosed to participate in the {yr} Secret Santa for {org}!\n\n".format(yr=year, org=organization)
      msg3    = "The results are now in.\n"
      msg4    = "Please keep in mind your drawing before the holidays roll around!\n"
      msg5    = "Also, please try to keep in mind the limitations that are being set in place for the prices.\n"
      msg6    = "The current limitations are set in between a 5 to 10 dollar gap.\n"
      msg7    = "More importantly, it is the thought that counts.\n\n"
      msg8    = "That being said, please enjoy the {yr} Secret Santa for {org}!\n\n".format(yr=year, org=organization)
      msgs    = msg2+msg3+msg4+msg5+msg6+msg7+msg8
      ending  = "\n\nBest Regards,\n\n{nm}".format(nm = name)
      while( len(hat)!=0 ):
            if ((len(hat)==2)): #Avoid someone drawing their own name!
                  counter+=1
                  if people[0][0]==hat[0]:
                        mesg1   = "Hi {p},\n\n".format(p=people[0][0])
                        message = mesg1+msgs
                        body1   = "\t\tDraw {c}.\t{p1} picks {p2}".format(c=counter, p1=people[0][0], p2=hat[1])
                        spy     = spy + '\n' + "Draw {c}.\t{p1} picks {p2}".format(c=counter, p1=people[0][0], p2=hat[1])
                        body1   = message+body1+ending
                        #addy    = people[0][1]                 #Sending email1 to people[0][0]
                        print("Drawing name #{ctr} for {pers}.\n".format(ctr=counter, pers = people[0][0]))
                        sendemail(from_addr    = usersGmail   ,
                            to_addr_list       = [addy]       ,
                            cc_addr_list       = [addy]       ,
                            subject            = emailSubject ,
                            message            = body1        ,
                            login              = usersGmail   ,
                            password           = pwz)          #Email statement 1; Uses `body1`
                        counter+=1
                        mesg1   = "Hi {p},\n\n".format(p=people[1][0])
                        message = mesg1+msgs
                        body2   = "\t\tDraw {c}.\t{p1} picks {p2}".format(c=counter, p1=people[1][0], p2=hat[0])
                        spy     = spy + '\n' + "Draw {c}.\t{p1} picks {p2}".format(c=counter, p1=people[1][0], p2=hat[0])
                        body2   = message+body2+ending
                        #addy    = people[1][1]                 #Sending email2 to people[1][0]
                        print("Drawing name #{ctr} for {pers}.\n".format(ctr=counter, pers = people[1][0]))
                        sendemail(from_addr    = usersGmail   ,
                            to_addr_list       = [addy]       ,
                            cc_addr_list       = [addy]       ,
                            subject            = emailSubject ,
                            message            = body2        ,
                            login              = usersGmail   ,
                            password           = pwz)          #Email statement 2; Uses `body2`
                        hat.remove(hat[1])
                        hat.remove(hat[0])
                        people.remove(people[1])
                        people.remove(people[0])
                        print(counter)
                  elif(people[1][0]==hat[0]):
                        mesg1   = "Hi {p},\n\n".format(p=people[1][0])
                        message = mesg1+msgs
                        body1   = "\t\tDraw {c}.\t{p1} picks {p2}".format(c=counter, p1=people[1][0], p2=hat[1])
                        spy     = spy + '\n' + "Draw {c}.\t{p1} picks {p2}".format(c=counter, p1=people[1][0], p2=hat[1])
                        body1   = message+body1+ending
                        #addy    = people[1][1]                 #Sending email3 to people[1][0]
                        print("Drawing name #{ctr} for {pers}.\n".format(ctr=counter, pers = people[1][0]))
                        sendemail(from_addr    = usersGmail   ,
                            to_addr_list       = [addy]       ,
                            cc_addr_list       = [addy]       ,
                            subject            = emailSubject ,
                            message            = body1        ,
                            login              = usersGmail   ,
                            password           = pwz)          #Email statement 3; Uses `body1`
                        counter+=1
                        mesg1   = "Hi {p},\n\n".format(p=people[0][0])
                        message = mesg1+msgs
                        body2   = "\t\tDraw {c}.\t{p1} picks {p2}".format(c=counter, p1=people[0][0], p2=hat[0])
                        spy     = spy + '\n' + "Draw {c}.\t{p1} picks {p2}".format(c=counter, p1=people[0][0], p2=hat[0])
                        body2   = message+body2+ending
                        #addy    = people[0][1]                 #Sending email4 to people[0][0]
                        print("Drawing name #{ctr} for {pers}.\n".format(ctr=counter, pers = people[0][0]))
                        sendemail(from_addr    = usersGmail   ,
                            to_addr_list       = [addy]       ,
                            cc_addr_list       = [addy]       ,
                            subject            = emailSubject ,
                            message            = body2        ,
                            login              = usersGmail   ,
                            password           = pwz)          #Email statement 4; Uses `body2`
                        hat.remove(hat[1])
                        hat.remove(hat[0])
                        people.remove(people[1])
                        people.remove(people[0])
                  else:
                        mesg1   = "Hi {p},\n\n".format(p=people[0][0])
                        message = mesg1+msgs
                        body1   = "\t\tDraw {c}.\t{p1} picks {p2}".format(c=counter, p1=people[0][0], p2=hat[0])
                        spy     = spy + '\n' + "Draw {c}.\t{p1} picks {p2}".format(c=counter, p1=people[0][0], p2=hat[0])
                        body1   = message+body1+ending
                        #addy    = people[0][1]                 #Sending email5 to people[0][0]
                        print("Drawing name #{ctr} for {pers}.\n".format(ctr=counter, pers = people[0][0]))
                        sendemail(from_addr    = usersGmail   ,
                            to_addr_list       = [addy]       ,
                            cc_addr_list       = [addy]       ,
                            subject            = emailSubject ,
                            message            = body1        ,
                            login              = usersGmail   ,
                            password           = pwz)          #Email statement 5; Uses `body1`
                        counter+=1
                        mesg1   = "Hi {p},\n\n".format(p=people[1][0])
                        message = mesg1+msgs
                        body2   = "\t\tDraw {c}.\t{p1} picks {p2}".format(c=counter, p1=people[1][0], p2=hat[1])
                        spy     = spy + '\n' + "Draw {c}.\t{p1} picks {p2}".format(c=counter, p1=people[1][0], p2=hat[1])
                        body2   = message+body2+ending
                        #addy    = people[1][1]                 #Sending email6 to people[1][0]
                        print("Drawing name #{ctr} for {pers}.\n".format(ctr=counter, pers = people[1][0]))
                        sendemail(from_addr    = usersGmail   ,
                            to_addr_list       = [addy]       ,
                            cc_addr_list       = [addy]       ,
                            subject            = emailSubject ,
                            message            = body2        ,
                            login              = usersGmail   ,
                            password           = pwz)          #Email statement 6; Uses `body2`
                        hat.remove(hat[1])
                        hat.remove(hat[0])
                        people.remove(people[1])
                        people.remove(people[0])
                  break #Ends long 'if len(hat)==2' clause
            else:
                  matchee = random.choice(people)
                  mesg1   = "Hi {p},\n\n".format(p=matchee[0]) 
                  message = mesg1+msgs
                  matcher = random.choice(hat)
                  if matchee[0] == matcher:
                        print("\n\t\tPutting name back in hat\n\n")
                  else:
                  #This is the call that is going to be iterated most often
                        counter+=1
                        print("Drawing name #{ctr} for {pers}.\n".format(ctr=counter, pers = matchee[0]))
                        body = message
                        body = body+"\t\tDraw {c}.\t{p1} picks {p2}".format(c=counter, p1=matchee[0], p2=matcher)
                        body = body + ending
                        spy  = spy + '\n' + "\tDraw {c}.\t{p1} picks {p2}".format(c=counter, p1=matchee[0], p2=matcher)
                        #addy = matchee[1]                      #matchee is a tuple; index 1 is email
                        sendemail(from_addr    = usersGmail   ,
                            to_addr_list       = [addy]       ,
                            cc_addr_list       = [addy]       ,
                            subject            = emailSubject ,
                            message            = body         ,
                            login              = usersGmail   ,
                            password           = pwz)          #Email statement 7; Uses `body`
                        people.remove(matchee) 
                        hat.remove(matcher)
            if ((matchee[0] == matcher)&(len(hat)==1)):
                  print("\n\nTHIS ONE IS BROKEN!!!\n")
                  break
      print(spy)
      assert len(hat)==0
      assert len(people)==0

secretSantaEmail()
