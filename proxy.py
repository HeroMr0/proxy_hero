import requests
from colorama import *
import pyfiglet
import os 
import time
import random
print(Fore.GREEN + Style.BRIGHT)
print(pyfiglet.figlet_format("MR HERO", font="sblood"))
print(pyfiglet.figlet_format("PROXY", font="sblood"))

time.sleep(3)
init(convert=True)

os.system('cls' if os.name == 'nt' else 'clear')

# FILES

https_file = open("https.txt","a") 
http_file = open("http.txt", "a")


# REQUEST API

rhttps = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=7000&country=ALL&anonymity=elite&ssl=no')
rhttp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=7000&country=ALL&anonymity=elite&ssl=no')


# HTTPS

https = []
https = rhttps.text
https = https.split()
lines = len(https)


# HTTP

http = []
http = rhttp.text
http = http.split()
hlines = len(http)

number = random.randint(1, 5)



def main():
    print(Fore.LIGHTRED_EX + '''
 _   _    __                 ____ 
|       \ |       \  /      \ |  \  |  \|  \    /  \|        \ 
| $$$$$$$\| $$$$$$$\|  $$$$$$\| $$  | $$ \$$\  /  $$ \$$$$$$$$
| $$/ $$| $$| $$| $$  | $$ \$$\/  $$  \$$\/  $$     /  $$ 
| $$    $$| $$    $$| $$  | $$  >$$  $$    \$$  $$     /  $$  
| $$$$$$$ | $$$$$$$\| $$  | $$ /  $$$$\     \$$$$     /  $$   
| $$      | $$  | $$| $$/ $$|  $$ \$$\    | $$     /  $$_ 
| $$      | $$  | $$ \$$    $$| $$  | $$    | $$    |  $$    \ 
 \$$       \$$   \$$  \$$$$$$  \$$   \$$     \$$     \$$$$$$$$ - V2

              Note - Must Test Proxies Before You Use
              Please Do Not Use It For Bad Activity
                                                             
''')
    time.sleep(3)
    print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTRED_EX  + "1" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTWHITE_EX + "HTTPS")
    print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTRED_EX  + "2" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTWHITE_EX + "HTTP")
    print(Fore.RESET + ' ')
    a = input(Fore.LIGHTWHITE_EX + "Choose Type of Proxy : ")
    if(a == "1"):
        for i in range(lines):
            print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTRED_EX + "Success -> HTTPS" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTRED_EX + https[i])
            https_file.write('\n' + https[i])
            time.sleep(2)
    elif(a == "2"):
        for a in range(hlines):
            print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTRED_EX + "Success -> HTTP" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTRED_EX + http[a])
            http_file.write('\n' + http[a])
            time.sleep(2)
    else:
        print(f"No Option Found Named -> '{a}' ")









if name == "main":

    main()
    print("All Proxy's Successfully Generated And Saved To File!")

os.system('pause' if os.name == 'nt' else 'pause')
