from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os
from colorama import init, Fore
from time import sleep
import webbrowser

init()

n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]

try:

    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

    print(f'| By DARK DEVIL {n}\n')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def banner():
    import random
    # fancy logo
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
    print(f'{r}  ᴄʜᴀɴɴᴇʟ : {ye}@dark0_0devil0 {ye}')
    print(f'{r}  ɢʀᴏᴜᴘ   : {ye}@dark0_0devil00{ye}')
    print(f'{r}   {r}')

while True:
    clr()
    banner()

    print(lg+'[1] ᴀᴅᴅ ɴᴇᴡ ᴀᴄᴄᴏᴜɴᴛꜱ'+n)
    print(lg+'[2] ꜰɪʟᴛᴇʀ ᴀʟʟ ʙᴀɴɴᴇᴅ ᴀᴄᴄᴏᴜɴᴛꜱ'+n)
    print(lg+'[3] ᴅᴇʟᴇᴛᴇ ꜱᴘᴇᴄɪꜰɪᴄ ᴀᴄᴄᴏᴜɴᴛꜱ'+n)
    print(lg+'[4] Quit'+n)
    a = int(input('\n ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ: '))
    if a == 1:
        new_accs = []
        with open('vars.txt', 'ab') as g:
            number_to_add = int(input(f'\n{lg} [~] ᴇɴᴛᴇʀ ɴᴜᴍʙᴇʀ ᴏꜰ ᴀᴄᴄᴏᴜɴᴛꜱ ᴛᴏ ᴀᴅᴅ:{r}'))
            for i in range(number_to_add):
                phone_number = str(input(f'\n{lg} [~] ᴇɴᴛᴇʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ:{r}'))
                parsed_number = ''.join(phone_number.split())
                pickle.dump([parsed_number], g)
                new_accs.append(parsed_number)
            print(f'\n{lg} [i] ꜱᴀᴠᴇᴅ ᴀʟʟ ᴀᴄᴄᴏᴜɴᴛꜱ ɪɴ vars.txt')
            clr()
            print(f'\n{lg} [*] ʟᴏɢɢɪɴɢ ɪɴ ꜰʀᴏᴍ ɴᴇᴡ ᴀᴄᴄᴏᴜɴᴛꜱ\n')
            for number in new_accs:
                c = TelegramClient(f'sessions/{number}', 16746680 , 'd038e172eb99839b69c39c3c25cd98cf')
                c.start(number)
                print(f'{lg}[+] ʟᴏɢɪɴ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟ')
                c.disconnect()
            input(f'\n ᴘʀᴇꜱꜱ ᴇɴᴛᴇʀ ᴛᴏ ɢᴏᴛᴏ ᴍᴀɪɴ ᴍᴇɴᴜ...')

        g.close()
    elif a == 2:
        accounts = []
        banned_accs = []
        h = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[!] ᴛʜᴇʀᴇ ᴀʀᴇ ɴᴏ ᴀᴄᴄᴏᴜɴᴛꜱ! ᴘʟᴇᴀꜱᴇ ᴀᴅᴅ ꜱᴏᴍᴇ ᴀɴᴅ ʀᴇᴛʀʏ')
            sleep(3)
        else:
            for account in accounts:
                phone = str(account[0])
                client = TelegramClient(f'sessions/{phone}', 16746680 , 'd038e172eb99839b69c39c3c25cd98cf')
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        #client.sign_in(phone, input('[+]ᴇɴᴛᴇʀ ᴛʜᴇ ᴄᴏᴅᴇ: '))
                        print(f'{lg}[+] {phone} is not banned{n}')
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' is banned!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'ᴄᴏɴɢʀᴀᴛꜱ! ɴᴏ ʙᴀɴɴᴇᴅ ᴀᴄᴄᴏᴜɴᴛꜱ')
                input('\nᴘʀᴇꜱꜱ ᴇɴᴛᴇʀ ᴛᴏ ɢᴏᴛᴏ ᴍᴀɪɴ ᴍᴇɴᴜ...')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('vars.txt', 'wb') as k:
                    for a in accounts:
                        Phone = a[0]
                        pickle.dump([Phone], k)
                k.close()
                print(lg+'[i] ᴀʟʟ ʙᴀɴɴᴇᴅ ᴀᴄᴄᴏᴜɴᴛꜱ ʀᴇᴍᴏᴠᴇᴅ'+n)
                input('\nᴘʀᴇꜱꜱ ᴇɴᴛᴇʀ ᴛᴏ ɢᴏᴛᴏ ᴍᴀɪɴ ᴍᴇɴᴜ...')

    elif a == 3:
        accs = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        print(f'{lg}[i] ᴄʜᴏᴏꜱᴇ ᴀɴ ᴀᴄᴄᴏᴜɴᴛ ᴛᴏ ᴅᴇʟᴇᴛᴇ\n')
        for acc in accs:
            print(f'{lg}[{i}] {acc[0]}{n}')
            i += 1
        index = int(input(f'\n{lg}[+] ᴇɴᴛᴇʀ ᴀ ᴄʜᴏɪᴄᴇ: {n}'))
        phone = str(accs[index][0])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        f = open('vars.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[+] ᴀᴄᴄᴏᴜɴᴛ ᴅᴇʟᴇᴛᴇᴅ     {n}')
        input(f'\nᴘʀᴇꜱꜱ ᴇɴᴛᴇʀ ᴛᴏ ɢᴏᴛᴏ ᴍᴀɪɴ ᴍᴇɴᴜ...')
        f.close()
    elif a == 4:
        webbrowser.open('https://t.me/dark0_0devil00')
        clr()
        banner()
        exit()


