import os
import time
import sys

###########
#colors   #
###########



WHITE = "\033[1;37;40m\n"
YELLOW = "\033[1;33;40m\n"
GREEN  = "\033[1;32;40m\n"
RED = "\033[1;31;40m\n"
BLUE  = "\033[1;34;40m\n"



def fairUSE():
    print(WHITE + "Use this tool ONLY for educational purposes?\n")
    fairanswer = input("\033[1;32;40mY/\033[1;31;40mN : ")
    if fairanswer == "Y"or"y":
       time.sleep(2)
       os.system("reset")       
       print("Well you won't but anyway...")
       time.sleep(2)    
    elif fairanswer == "N"or"n":
         exit("Don't be bad person\n ")
    else:
         exit("Can't you even press a key ? ")
        
fairUSE()
print( """
                        ..::::\033[1;36;40m:::::..
                ..:::aad8888\033[1;33;40m888baa:::..
                .::::d:?888888\033[1;36;40m88888?::8b::::.
          .:::d8888:?8888888\033[1;33;40m8??a888888b:::.
            .:::d8888888a88888\033[1;36;40m88aa8888888888b:::.
       ::::dP::::::::8888888\033[1;33;40m8888::::::::Yb::::
          ::::dP:::::::::Y8888\033[1;36;40m88888P:::::::::Yb::::
     ::::d8:::::::::::Y88888\033[1;33;40m88P:::::::::::8b::::
        .::::88::::::::::::Y88\033[1;36;40m888P::::::::::::88::::.
    :::::Y8baaaaaaaaaa88P:T:\033[1;33;40mY88aaaaaaaaaad8P:::::
        :::::::Y88888888888P::\033[1;36;40m|::Y88888888888P:::::::
    ::::::::::::::::888:::|:\033[1;33;40m::888::::::::::::::::
        `:::::::::::::::888888\033[1;36;40m8888888b::::::::::::::'
      ::::::::::::::88888888\033[1;33;40m888888::::::::::::::
          :::::::::::::d888888\033[1;36;40m88888888:::::::::::::
        :::::::::::88::88::8\033[1;33;40m8:::88::::::::::::
           `::::::::::88::88::\033[1;36;40m88:::88::::::::::'
          `::::::::88::88::P\033[1;33;40m::::88::::::::'
                `::::::88::88:\033[1;36;40m::::::88::::::'
               ``::::::::::::\033[1;33;40m:::::::''
                        ``::::::\033[1;36;40m:::''
  [Coded By NorthX]                             [XChoice]
""")
time.sleep(3)
os.system("reset")

print(YELLOW + '''


        ,..-,
         ,;;f^^"""-._
        ;;'          `-.
       ;/               `.
       ||  _______________\_______________________
       ||  |HHHHHHHHHHPo"~~\"o?HHHHHHHHHHHHHHHHHHH|
       ||  |HHHHHHHHHP-._   \,'?HHHHHHHHHHHHHHHHHH|
        |  |HP;""?HH|    """ |_.|HHP^^HHHHHHHHHHHH|
        |  |HHHb. ?H|___..--"|  |HP ,dHHHPo'|HHHHH|
        `| |HHHHHb.?Hb    .--J-dHP,dHHPo'_.rdHHHHH|
         \ |HHHi.`;;.H`-./__/-'H_,--'/;rdHHHHHHHHH|
           |HHHboo.\ `|"\"/"\" '/\ .'dHHHHHHHHHHHH|
           |HHHHHHb`-|.  \|  \ / \/ dHHHHHHHHHHHHH|
           |HHHHHHHHb| \ |\   |\ |`|HHHHHHHHHHHHHH|
           |HHHHHHHHHb  \| \  | \| |HHHHHHHHHHHHHH|
           |HHHHHHHHHHb |\  \|  |\|HHHHHHHHHHHHHHH|
           |HHHHHHHHHHHb| \  |  / dHHHHHHHHHHHHHHH|
           |HHHHHHHHHHHHb  \/ \/ .fHHHHHHHHHHHHHHH|
           |HHHHHHHHHHHHH| /\ /\ |HHHHHHHHHHHHHHHH|
           |""""""""""""""""""""""""""""""""""""""|
           |,;=====.     ,-.  =.       ,=,,=====. |
           |||     '    //"\\   \\   //  ||     ' |
           |||         ,/' `\.  `\. ,/'  ``=====. |
           |||     .   //"""\\   \\_//    .     |||
           |`;=====' =''     ``=  `-'     `=====''|
           |______________________________________|

''')



def MenuItems():
    menuid = BLUE + "1)WebScan\n\n" "2)DOS Tools\n\n""3)Password Crack\n\n""4)PayloadGenerator\n\n""5)Phishing\n\n""99)Exit\n\n"
    print(menuid)
    answer = int(input("Enter a choice : "))
    if answer == 1 :
        os.system("figlet WEBKILLER")
        ScanMenu()
    elif answer == 2:
        os.system("figlet D O S ")
        DOSMenu()
    elif answer == 3 :
        os.system("figlet PASSCRACK")
        Passmenu()
    elif answer == 4:
        PayloadGen()
        os.system("figlet P_A_Y_L_O_A_D")
    elif answer == 5:
        os.system("figlet P  H  !   $   H ")
        Phish()
    elif answer == 99:
         exit("Byeeeeeee")
    else :
        print(RED +"[!] Enter a vailed optiom")


###########################################################################
###########################################################################
###########################################################################

def ScanMenu():
    portmenu = YELLOW + """
    
1)Nmap\n
2)Unicorn\n 
3)Striker\n
4)Th3inspector\n
99)Return to main menu\n         """
    print(portmenu)
    portanswer = int(input("Enter a choice : "))
    if portanswer == 1 :
       os.system("git clone https://github.com/nmap/nmap.git ")
    elif portanswer == 2 :
       os.system("git clone https://github.com/IFGHou/Unicornscan.git ")
    elif portanswer == 3:
        os.system("git clone https://github.com/s0md3v/Striker.git ")
    elif portanswer == 4:
        os.system("git clone https://github.com/Moham3dRiahi/Th3inspector.git ")
    elif portanswer == 99:
        MenuItems()
    else:
        exit("[!] Enter a vailed option ")

def DOSMenu():
    dostools = GREEN + """
    
1)Hulk\n 
2)Xerxes\n 
3)Slowloris\n     
4)LOIC (for linux)\n 
99)Return to main menu\n      """
    print(dostools)
    dosnswer = int(input("Enter an option : "))
    if dosnswer == 1:
        os.system("git clone https://github.com/darkwarrior3/hulk.git")
    elif dosnswer == 2:
        os.sytem("git clone https://github.com/zanyarjamal/xerxes.git ")
    elif dosnswer == 3:
        os.system("git clone https://github.com/llaera/slowloris.pl.git ")
    elif dosnswer == 4:
        os.system("git clone https://github.com/NewEraCracker/LOIC.git ")
    elif dosnswer == 99:
        MenuItems()
    else:
        exit("[!] Enter a vailed option")


def Passmenu():
    passmenu = WHITE + """
    
1)Medusa\n
2)SocialBox\n 
3)Crunch (WordList generator)\n     
99)Return to main menu\n  
     """
    print(passmenu)
    passanswer = int(input("Enter a choice : "))
    if passanswer == 1 :
        os.system("git clone https://github.com/jmk-foofus/medusa.git ")
    elif passanswer == 2:
        os.system("git clone https://github.com/TunisianEagles/SocialBox.git ")
    elif passanswer == 3 :
        os.system("git clone https://github.com/crunchsec/crunch.git")
    elif passanswer == 99:
        MenuItems()
    else :
        exit("[!] Enter a vailed option")


def PayloadGen():
    payloadmenu = """
    
1)TheFatRat\n
2)Zirikatu\n
3)ezsploit\n
99)Return to main menu\n     
      """
    print(payloadmenu)
    payanswer = int(input("Enter your choice :"))
    if payanswer == 1:
        os.system("git clone https://github.com/Screetsec/TheFatRat.git ")
    elif payanswer == 2:
        os.system("git clone https://github.com/pasahitz/zirikatu.git ")
    elif payanswer== 3:
        os.system("git clone https://github.com/rand0m1ze/ezsploit.git ")
    elif payanswer == 99:
        MenuItems()
    else:
        exit("[!] Enter a vailed option ")


def Phish():
    phishmenu = """
    
1)PhishX (most powerful phishing tool)\n
2)Phisher-man\n
3)shellphish\n
99)Return to main menu\n 
     """
    print(phishmenu)
    phishanswer = int(input("Enter an option : "))
    if phishanswer == 1:
        os.system("git clone https://github.com/WeebSec/PhishX.git ")
    elif phishanswer == 2:
        os.system("git clone https://github.com/FDX100/Phisher-man.git ")
    elif phishanswer == 3:
        os.system("git clone https://github.com/thelinuxchoice/shellphish.git ")
    elif phishanswer == 99:
        MenuItems()


MenuItems()
