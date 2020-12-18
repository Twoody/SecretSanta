import random
import smtplib

'''
Written by: Tanner Lee Woody

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
          ("Tanner Woody",      'twoody@precoa.com',        '2108 Buck Street, West Linn, Oregon, 97068',       'Dogs, books, traveling, gardening, everything!'),#1
          ('Daven Septon',      'dsepton@precoa.com',       '14358 SW 147th Pl, Portland OR 97224',             'Nerd'),                                          #2
          ('Tyler Brady',       'tbrady@precoa.com',        '1440 nw Lancashire ct, Beaverton, OR 97006',       'Candy, chocolate, old cool xbox game?'),         #3
          ('AJ Ruffner',        'aruffner@precoa.com',      '34681 Boulder Court, Saint Helens OR 97051',       'I am an avid golfer, and a huge sports fan. I also love Harry Potter'),
          ('Brandon Quinn',     'bquinn@precoa.com',        '12041 SW Sagehen street Beaverton, OR 97007',      'I prefer consumable things like popcorn or shower bombs or caffeine-free tea or hand lotion.'),
          ('Jason Giardino',    'jgiardino@precoa.com',     '1326 SE 152nd Pl., Portland, OR  97233',           'Ideas: KeyForge decks (any), Star Wars-themed, D&D-themed'),
          ('Kathy Grahn',       'kgrahn@precoa.com',        '16488 NW Brandberry Drive, Portland, OR 97229',    'Craft supplies, Christmas ornaments in blue or silver, Cookie decorating supplies'),
          ('Lisa Glazier',      'lglazier@precoa.com',      '11944 SW Aspen Ridge Dr, Tigard, OR 97224', "I love any shape or form of Reese's peanut butter cups/candies, pretty much anything from bobs red mill (grains, flours, baking mixes, granola bars), and I also like things for baby girls"),
          ('Shane Malan',       'smalan@precoa.com',        '22933 SW Saunders Dr., Sherwood, OR 97140', 'Restaurants/Food, games, book(history or biographies), music (Apple)'),
          ('JP Nye',            'jpnye@precoa.com',         '19620 SW Southview St, Beaverton OR 97078', 'Wood working tools, Chisels, ScrewDrivers, Tape measures, Clamps, Drill Bits, etc'),
          ('Nick Wahlin',       'nwahlin@precoa.com',       '790 N Main St, Alpine, UT 84004', 'Chocolate, Coffee, Books'),                                       #11
          ('Sean Gallagher',    'sgallagher@precoa.com',    '18904 SW Strickland Drive, Beaverton, OR 97007', "I'm a big fan of science fiction/fantasy, and parti#12cularly Star Trek, Star Wars, Warhammer 40k, LOTR, and D&D. I also enjoy a good cup of tea, coffee, or hot cocoa during the winter season. "),
          ('Remy Nakamura',     'jremy@precoa.com',         '1125 NW 9th Ave Apt 432, Portland, OR 97209', "I really like crows, but understand the prohibition on#13 not sending living things. I'd welcome just about any gift, but if it helps, here are some ideas to go on: I like mushrooms,  \"cities of the world\" color scheme 3M post-it notes, Miyazaki films, colorful tarot and playing card decks, Mister Rogers, carabiners for rock climbing. "),
          ('Amrit Saini',       'asaini@precoa.com',        '1621 E 6th Street, Unit 1317, Austin, TX 78702', 'Dog Toys & Socks'),                                #14
          ('Jake Zollinger',    'jzollinger@precoa.com',    '1564 n 325 w, Orem UT 84057', 'I like Legos, Starwars and food'),                                    #15
          ('Casey Siglermann',  'csigelmann@precoa.com',    '7572 SW Oleson Rd Apt D11, Portland OR, 97223', 'Fantasy or sci-fi books or decorations')            #16
         ]

hat    = [
          ("Tanner Woody",      'twoody@precoa.com',        '2108 Buck Street, West Linn, Oregon, 97068',       'Dogs, books, traveling, gardening, everything!'),
          ('Daven Septon',      'dsepton@precoa.com',       '14358 SW 147th Pl, Portland OR 97224',             'Nerd'),
          ('Tyler Brady',       'tbrady@precoa.com',        '1440 nw Lancashire ct, Beaverton, OR 97006',       'Candy, chocolate, old cool xbox game?'),
          ('AJ Ruffner',        'aruffner@precoa.com',      '34681 Boulder Court, Saint Helens OR 97051',       'I am an avid golfer, and a huge sports fan. I also love Harry Potter'),
          ('Brandon Quinn',     'bquinn@precoa.com',        '12041 SW Sagehen street Beaverton, OR 97007',      'I prefer consumable things like popcorn or shower bombs or caffeine-free tea or hand lotion.'),
          ('Jason Giardino',    'jgiardino@precoa.com',     '1326 SE 152nd Pl., Portland, OR  97233',           'Ideas: KeyForge decks (any), Star Wars-themed, D&D-themed'),
          ('Kathy Grahn',       'kgrahn@precoa.com',        '16488 NW Brandberry Drive, Portland, OR 97229',    'Craft supplies, Christmas ornaments in blue or silver, Cookie decorating supplies'),
          ('Lisa Glazier',      'lglazier@precoa.com',      '11944 SW Aspen Ridge Dr, Tigard, OR 97224',        "I love any shape or form of Reese's peanut butter cups/candies, pretty much anything from bobs red mill (grains, flours, baking mixes, granola bars), and I also like things for baby girls"),
          ('Shane Malan',       'smalan@precoa.com',        '22933 SW Saunders Dr., Sherwood, OR 97140', 'Restaurants/Food, games, book(history or biographies), music (Apple)'),
          ('JP Nye',            'jpnye@precoa.com',         '19620 SW Southview St, Beaverton OR 97078', 'Wood working tools, Chisels, ScrewDrivers, Tape measures, Clamps, Drill Bits, etc'),
          ('Nick Wahlin',       'nwahlin@precoa.com',       '790 N Main St, Alpine, UT 84004', 'Chocolate, Coffee, Books'),
          ('Sean Gallagher',    'sgallagher@precoa.com',    '18904 SW Strickland Drive, Beaverton, OR 97007', "I'm a big fan of science fiction/fantasy, and particularly Star Trek, Star Wars, Warhammer 40k, LOTR, and D&D. I also enjoy a good cup of tea, coffee, or hot cocoa during the winter season. "),
          ('Remy Nakamura',     'jremy@precoa.com',         '1125 NW 9th Ave Apt 432, Portland, OR 97209', "I really like crows, but understand the prohibition on not sending living things. I'd welcome just about any gift, but if it helps, here are some ideas to go on: I like mushrooms,  \"cities of the world\" color scheme 3M post-it notes, Miyazaki films, colorful tarot and playing card decks, Mister Rogers, carabiners for rock climbing. "),
          ('Amrit Saini',       'asaini@precoa.com',        '1621 E 6th Street, Unit 1317, Austin, TX 78702', 'Dog Toys & Socks'),
          ('Jake Zollinger',    'jzollinger@precoa.com',    '1564 n 325 w, Orem UT 84057', 'I like Legos, Starwars and food'),
          ('Casey Siglermann',  'csigelmann@precoa.com',    '7572 SW Oleson Rd Apt D11, Portland OR, 97223', 'Fantasy or sci-fi books or decorations')
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
    return

def testNames():
      print("CHECKING THAT THE NAMES ARE THE SAME; IF NOT, WE FAIL HERE\n")
      for i in range (0, length):
            print("\t"+people[i][0]+" should be the same as "+hat[i][0])
            assert people[i][0] == hat[i][0]
      print("\nALL OF THE NAMES ARE THE SAME. GOING TO COMMENCE EMAILING\n\n\n")



testNames()
############################################################
############################################################
############################################################
############################################################

def secretSantaEmail():
      counter      = 0
      addy         = 'precoa.santa@gmail.com'
      usersGmail   = 'precoa.santa@gmail.com'
      pwz          = "1that'shard2guess"
      organization = "Precoa"
      year         = '2020'
      name         = 'Tanner Woody'
      emailSubject = "Precoa 2020 Secret Santa Drawing"
      spy     = ''#This should be used just for testing. The print statement should be commented out below
      msg2    = "You've been chosen to participate in the {yr} Secret Santa for {org}!\n\n".format(yr=year, org=organization)
      msg3    = "The results are now in.\n"
      msg4    = "Please keep in mind your drawing before the holidays roll around!\n"
      msg5    = "Also, please try to keep in mind the limitations that are being set in place for the prices.\n"
      msg6    = "The current limitations are set in between a 15 to 20 dollar gap.\n"
      msg7    = "More importantly, it is the thought that counts!\n\n"
      msg8    = "That being said, please enjoy the {yr} Secret Santa for {org}!\n\n".format(yr=year, org=organization)
      msgs    = msg2+msg3+msg4+msg5+msg6+msg7+msg8
      ending  = "\n\nBest Regards,\n\n{nm}".format(nm = name)
      while( len(hat)!=0 ):
            if ((len(hat)==2)): #Avoid someone drawing their own name!
                  counter+=1
                  if people[0][0]==hat[0][0]:
                        mesg1   = "Hi {p},\n\n".format(p=people[0][0])
                        message = mesg1+msgs
                        body1   = "\t\tDraw {c}.\t{p1} picks {p2}\n".format(c=counter, p1=people[0][0], p2=hat[1][0])
                        body1   = body1 + '\t\t\tAddress: {a}\n\t\t\tLikes: {l}'.format(a=hat[1][2], l=hat[1][3])
                        spy     = spy + '\n' + body1
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
                        body2   = "\t\tDraw {c}.\t{p1} picks {p2}\n".format(c=counter, p1=people[1][0], p2=hat[0][0])
                        body2   = body2 + '\t\t\tAddress: {a}\n\t\t\tLikes: {l}'.format(a=hat[0][2], l=hat[0][3])
                        spy     = spy + '\n' + body2
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
                  elif(people[1][0]==hat[0][0]):
                        mesg1   = "Hi {p},\n\n".format(p=people[1][0])
                        message = mesg1+msgs
                        body1   = "\t\tDraw {c}.\t{p1} picks {p2}\n".format(c=counter, p1=people[1][0], p2=hat[1][0])
                        body1   = body1 + '\t\t\tAddress: {a}\n\t\t\tLikes: {l}'.format(a=hat[1][2], l=hat[1][3])
                        spy     = spy + '\n' + body1
                        body1   = message + body1 + ending
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
                        body2   = "\t\tDraw {c}.\t{p1} picks {p2}\n".format(c=counter, p1=people[0][0], p2=hat[0][0])
                        body2   = body2 + '\t\t\tAddress: {a}\n\t\t\tLikes: {l}'.format(a=hat[0][2], l=hat[0][3])
                        spy     = spy + '\n' + body2
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
                        body1   = "\t\tDraw {c}.\t{p1} picks {p2}\n".format(c=counter, p1=people[0][0], p2=hat[0][0])
                        body1   = body1 + '\t\t\tAddress: {a}\n\t\t\tLikes: {l}'.format(a=hat[0][2], l=hat[0][3])
                        spy     = spy + '\n' + body1
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
                        body2   = "\t\tDraw {c}.\t{p1} picks {p2}\n".format(c=counter, p1=people[1][0], p2=hat[1][0])
                        body2   = body2 + '\t\t\tAddress: {a}\n\t\t\tLikes: {l}'.format(a=hat[1][2], l=hat[1][3])
                        spy     = spy + '\n' + body2
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
                  if matchee[0] == matcher[0]:
                        print("\n\t\tPutting name back in hat\n\n")
                  else:
                  #This is the call that is going to be iterated most often
                        counter+=1
                        print("Drawing name #{ctr} for {pers}.\n".format(ctr=counter, pers = matchee[0]))
                        body = message
                        body = body + "\t\tDraw {c}. {p1} picks {p2}".format(c=counter, p1=matchee[0], p2=matcher[0])
                        body = body + '\n\t\t\tAddress: {a}\n\t\t\tLikes: {l}'.format(a=matcher[2], l=matcher[3])
                        spy  = spy + body
                        body = body + ending
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
            if ((matchee[0] == matcher[0]) & (len(hat)==1)):
                  print("\n\nTHIS ONE IS BROKEN!!!\n")
                  break
      print(spy)
      assert len(hat)==0
      assert len(people)==0

secretSantaEmail()
