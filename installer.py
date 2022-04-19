#THE AUTHOR OF THIS  SCRIPT IS DARK DEVIL
#PLEASE GIVE CREDITS IF U WANT TO COPY
# JOIN ~ @DARK0_0DEVIL00 FOR MORE 
#IMPORT
import os
from colorama import init, Fore
from time import sleep
import csv
import time
import random
import os
import pickle
import sys

#COLORS
init()
n = Fore.RESET
lg = Fore.BLUE
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
gr = Fore.GREEN
colors = [lg, r, w, cy, ye, gr]

# REQUIREMENTS 
try:
    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

# BANNER {LOGO} DARK DEVIL
def banner():
    import random

    b = [
'██████╗  █████╗ ██████╗ ██╗  ██╗██╗   ██╗',   
'██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝╚██╗ ██╔╝',
'██║  ██║███████║██████╔╝█████╔╝  ╚████╔╝',
'██║  ██║██╔══██║██╔══██╗██╔═██╗   ╚██╔╝',    
'██████╔╝██║  ██║██║  ██║██║  ██╗   ██║',   
'╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝',      
                                             
 '█████╗ ██████╗ ██████╗ ███████╗██████╗',      
'██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗',     
'███████║██║  ██║██║  ██║█████╗  ██████╔╝',     
'██╔══██║██║  ██║██║  ██║██╔══╝  ██╔══██╗',     
'██║  ██║██████╔╝██████╔╝███████╗██║  ██║',     
'╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝',  

                                                                                            


    ]
    for char in b:    
        print(f'{w}{char}{n}{w}')
    print(f'{r}   {r}')
    print(f'{r}  ᴄʜᴀɴɴᴇʟ  : {gr}@dark0_0devil0 {gr}')
    print(f'{r}  ɢʀᴏᴜᴘ    : {gr}@dark0_0devil00{gr}')
    print(f'{r}  ᴅᴇᴠᴇʟᴏᴘᴇʀ : {gr}ᴅᴀʀᴋ😈ᴅᴇᴠɪʟ{gr}')
    print(f'{r}   {r}')

# FUNCTION CALLING 
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
while True:
    clr()
    banner()
    print(ye+'Choose an Option:'+n)
    print(cy+'            [1] ꜱᴇᴛᴜᴘ ꜱᴄʀɪᴘᴛ'+n)
    print(cy+'            [2] ᴇxɪᴛ'+n)
    a = int(input('\n Enter your choice: '))
    if a == 1:
    
       print("[+] Installing requierments ...")
       os.system('pip install telethon==1.24.0')
       os.system('pip install colorama==0.4.3')
       os.system('pip install cryptography')
       print("[+] setup complete !")
       print("[+] now you can run any tool !")
        
       input(f'\n Press enter to goto main menu...')
       
    if a == 2:
        clr()
        banner()
        exit()

 
