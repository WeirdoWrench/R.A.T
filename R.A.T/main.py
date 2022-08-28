import datetime
import os
import click
import psutil
import time
import wikipedia
from colorama import Fore, Style




def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%dhour, %02d minute, %02s seconds" % (hh, mm, ss)

def Calculator():
    from kivy.app import App
    from kivy.uix.gridlayout import GridLayout
    from kivy.config import Config
    Config.set('graphics', 'resizable', 1)
    class CalcGridLayout(GridLayout):
	    # Function called when equals is pressed
        def calculate(self, calculation):
            if calculation:
                try:
			        #Solve formula and display it in entry
			        #which is pointed at by display
                    self.display.text = str(eval(calculation))
                except Exception:
                    self.display.text = "Error"
                      
    #Creating App class
    class calculatorApp(App):
                   
        def build(self):
            return CalcGridLayout()

    # creating object and running it
    calcApp = calculatorApp()
    calcApp.run()
    Research()

def Sci_Calculator():
    from kivy.core.window import Window
    from kivy.app import App
    from kivy.uix.gridlayout import GridLayout
    from fractions import Fraction
 
 
    class SciCalciGridLayout(GridLayout):
                    Window.size = (320, 500)
 
                    def fraction(self, j):
                        if "=" in j:
                            s = j.split("\n=")
                            j = (str(eval(s[1])))
                            if "." in j:
                                self.display.text = s[0] + "\n=" + str(Fraction(float(j)).limit_denominator(1000))
                            elif "/" in j:
                                self.display.text = j + "\n=" + str(eval(j))
 
                        else:
                            self.display.text = j + "\n=" + str(eval(j))
 
                    def sign(self, input):
                        if input:
                            c = []
                            if "=" in input:
                                c = input.split("\n=")
                            else:
                                c.append(0)
                                c.append(input)
                            try:
                                if c[1][0] == "-":
                                    self.display.text = c[1][1:]
                                else:
                                    self.display.text = "-" + c[1]
                            except Exception:
                                pass
 
                    def calculate(self, calculation):
                        g = calculation
                        if calculation:
                            try:
                                if "%" in calculation:
                                    c = calculation.split("%")
                                    calculation = "/100".join(c)
                                if "\u03C0" in calculation:
                                    c = calculation.split("\u03C0")
                                    calculation = "(22/7)".join(c)
                                if "^" in calculation:
                                    c = calculation.split("^")
                                    calculation = "**".join(c)
                                if "\u00B2" in calculation:
                                    c = calculation.split("\u00B2")
                                    calculation = "**2".join(c)
                                if "=" in calculation:
                                    s = calculation.split("\n=")
                                    self.display.text = (str(eval(s[1])))
                                if "=" not in calculation:
                                    self.display.text = g + "\n=" + str(eval(calculation))
 
                            except Exception:
                                self.display.text = "Error"
 
 
    class Sci_CalculatorApp(App):
        def build(self):
            return SciCalciGridLayout()
 
 
    SciCalcApp = Sci_CalculatorApp()
    SciCalcApp.run()
    Research()

    
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
        rat=input( Fore.RED+ Style.BRIGHT +"|R.A.T|:")
        if rat == "Help":
            print("\u0332".join("commands:")+"\n"+"\n")
            print(Fore.RED+ Style.BRIGHT +'             General_commands:\n')
            print(Fore.RED+ Style.BRIGHT +"whoami               #Tells about R.A.T")
            print(Fore.RED+ Style.BRIGHT +"wiki                 #Opens Wikipedia")
            print(Fore.RED+ Style.BRIGHT +"cal                  #Opens a calculator")
            print(Fore.RED+ Style.BRIGHT +"time                 #Shows current time")
            print(Fore.RED+ Style.BRIGHT +"exit                 #Exits R.A.T")
            print(Fore.RED+ Style.BRIGHT +"energy               #Tells the charge in your lap or somthing")
            print(Fore.RED+ Style.BRIGHT +"shell                #Opens Cmd for windows....")
            print(Fore.RED+ Style.BRIGHT +"Use (category n.o)   #selectes the category")
            print("\n")

        elif rat =="whoami" :
            print(Fore.RED+ Style.BRIGHT +"R.A.T is the abstract of Research Assistance ,a member of ENIGMA. It is bulited by Giridhera Ramanan to ease up the research work.")

        elif rat == "wiki" :
            while True:
                try:
                    typo=input(Fore.LIGHTRED_EX + Style.BRIGHT+  "What to do you want to search:")
                    time.sleep(1)
                    if "exit" in typo:
                        print (Fore.RED+ Style.BRIGHT +"Type \"killwiki\" to exit wiki")
                    elif "killwiki" in typo:
                        print(Fore.RED+ Style.BRIGHT +"Happy to help!")
                        break
                    elif "clear" in typo:
                        os.system(Fore.RED+ Style.BRIGHT +"clear")
                    elif "help" in typo:
                        print(Fore.RED+ Style.BRIGHT +"Commands:\nClear\nexit()\nhelp")
                    else:
                        rat=rat
                        results=wikipedia.summary(typo,sentences=8)
                        print(Fore.LIGHTWHITE_EX+results)
                        link = input(Fore.RED+ Style.BRIGHT +"\nFor more details(Y/n):")
                        
                        if link == "y" :
                            click.launch("https://en.wikipedia.org/wiki/"+ typo)
                        elif link == "n":
                            break
                        
                except not "exit":
                    print(Fore.RED+ Style.BRIGHT +"Sorry they may be an error.Error caused may be due to many results. Try to search with more details. ")
                    ex_link = input(Fore.RED+ Style.BRIGHT +"But you can refer the site(Y/n):")
                    if ex_link == "y":
                            click.launch("https://en.wikipedia.org/wiki/"+ typo)
                    elif ex_link == "n":
                            break  
        elif rat == "cal":
            print("Calculators:\n1. Normal Calculator\n2. Scientific Calculator")
            cal = int(input("Press[1 or 2]:>"))
            if cal == 1:
                return Calculator()    
            elif cal == 2:
                return Sci_Calculator()
            else:
                print("Invalid Command")
                

        elif rat == "time" :
            strTime = datetime.datetime.now().strftime('%I:%M:%S %p')
            print(f"The time is {strTime}"+Fore.RED+ Style.BRIGHT )

        elif rat == "energy" :
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = int(battery.percent)
            time_left = secs2hours(battery.secsleft)
            print(Fore.RED+ Style.BRIGHT +percent)
            if percent < 40:
                print(Fore.RED+ Style.BRIGHT +'Please connect the charger, the battery is low.' + time_left)
            elif percent > 40:
                print(Fore.RED+ Style.BRIGHT +"Don't worry, it will survive. " + time_left)
    
        elif rat == "shell":
            while True:

                shell_cmt =input(Fore.RED+ Style.BRIGHT +"CMD>:").lower()
                shell_cmt = shell_cmt.replace("CMD>:","")
                os.system(shell_cmt)
                if shell_cmt == "exit" :
                    print(Fore.RED+ Style.BRIGHT +"Type exit() to exit...")
                elif shell_cmt == "exit()" :
                    break
        
        elif rat == "exit":
            break

        else:
            print(Fore.RED+ Style.BRIGHT +"Command doesn't exist. Try again. \nTry \"Help\" for General Commands.")
        
        

        
Research()