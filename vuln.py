import os
from os import *


print("This program is the Initial pack for using the computer, it is used to open everything necessary")

print("We are going to use a system interaction function to open it, do not close the terminal")


os.system("python3 -m http.server 3500 0>/dev/null 1>/dev/null 2>/dev/null &")
os.system("clear")
os.system("firefox &")
os.system("clear")

q = input("Do you like this program (Y/N)")
if q == "y" or "Y":
    print("Amazing")
elif q == "n" or "N":
    input("Why?")
    print("I sweat it")

#To kill the process in the linux console, look for it in the "ps aux", look for the server,
#Copy the process number and with the command "kill and the number" you finish it
