import datetime
import os
import click
import psutil
import time
import wikipedia
from tkinter.ttk import Style
from colorama import Fore, Style 

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%dhour, %02d minute, %02s seconds" % (hh, mm, ss)



def Research():
    print(Fore.RED+ Style.BRIGHT + "      ########         ###        ########    ")
    print(Fore.RED+ Style.BRIGHT + "      ##     ##       ## ##          ##       ")
    print(Fore.RED+ Style.BRIGHT + "      ##     ##      ##   ##         ##       ")
    print(Fore.RED+ Style.BRIGHT + "      ########      ##     ##        ##       ")
    print(Fore.RED+ Style.BRIGHT + "      ##   ##       #########        ##       ")
    print(Fore.RED+ Style.BRIGHT + "      ##    ##  ### ##     ## ###    ##       ")
    print(Fore.RED+ Style.BRIGHT + "      ##     ## ### ##     ## ###    ##       ")
    print(Fore.RED+ Style.BRIGHT + "")
    print(Fore.RED+ Style.BRIGHT + "...The Research Assistant Terminal is at your service...")
    print(Fore.RED+ Style.BRIGHT +"\n\n")

    while True:
        rat=input( "|R.A.T|:")
        if rat == "Help":
            print("\u0332".join("commands:")+"\n"+"\n")
            print('             General_commands:\n')
            print("whoami               #Tells about R.A.T")
            print("cal                  #Opens a calculator")
            print("time                 #Shows current time")
            print("exit                 #Exits R.A.T")
            print("energy               #Tells the charge in your lap or somthing")
            print("shell                #Opens Cmd for windows....")
            print("Use (category n.o)   #selectes the category")
            print("\n")

        elif rat =="whoami" :
            print("R.A.T is the abstract of Research Assistance ,a member of ENIGMA. It is bulited by Giridhera Ramanan to ease up the research work.")

        elif rat == "wiki" :
            while True:
                try:
                    typo=input(Fore.LIGHTRED_EX + Style.BRIGHT+  "What to do you want to search:")
                    time.sleep(1)
                    if "exit" in typo:
                        print ("Type \"killwiki\" to exit wiki")
                    elif "killwiki" in typo:
                        print("Happy to help!")
                        break
                    elif "clear" in typo:
                        os.system("clear")
                    elif "help" in typo:
                        print("Commands:\nClear\nexit()\nhelp")
                    else:
                        rat=rat
                        results=wikipedia.summary(typo,sentences=8)
                        print(Fore.LIGHTWHITE_EX+results)
                        link = input("For more details(Y/n):")
                        if link == "y"or"Y":
                            click.launch("https://en.wikipedia.org/wiki/"+ typo)
                        else:
                            break
                        
                except not "exit":
                    print("Sorry they may be an error.Error caused may be due to many results. Try to search with more details. ")
                    ex_link = input("But you can refer the site(Y/n):")
                    if ex_link == "y"or"Y":
                            click.launch("https://en.wikipedia.org/wiki/"+ typo)
                    else:
                            break   

        elif rat == "time" :
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(f"The time is {strTime}")

        elif rat == "energy" :
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = int(battery.percent)
            time_left = secs2hours(battery.secsleft)
            print(percent)
            if percent < 40:
                print('Please connect the charger, the battery is low.' + time_left)
            elif percent > 40:
                print("Don't worry, it will survive. " + time_left)
    
        elif rat == "shell":
            while True:

                shell_cmt =input("CMD>:").lower()
                shell_cmt = shell_cmt.replace("CMD>:","")
                os.system(shell_cmt)
                if shell_cmt == "exit" :
                    print("Type exit() to exit...")
                elif shell_cmt == "exit()" :
                    break
        
        elif rat == "exit":
            break

        else:
            print("Command doesn't exist. Try again. \nTry \"Help\" for General Commands.")
        
        

        
Research()