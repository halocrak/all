import requests,time
from user_agent import generate_user_agent
import secrets
ruks = requests.session()
AC ='\033[1;31m'
BC ='\033[1;32m'
CC ='\033[1;33m'
DC ='\033[1;37m'
# ======#
jruks = '\033[1;33m'
ruks_ = '\033[1;36m'
ruks__ = '\033[1;36m'
_ruks  = '\033[1;31m'
BGreen='\033[1;32m'
z =  ('{"telegram":" ,  , @i4m_mrx"}')
inFollow=["awosalhlfe","shahadalshemari","sollaf5","wilayet.batikh.official","ali_fadil","waedhanan","noorstars","ashraf_noon","haylatv","chef.shaheen","ahlame_hajji","raedabufatean","actress_alaa_hussein","shimaa_qasim","masa_sam"]
Followlist=["_v_go","awosalhlfe","shahadalshemari","sollaf5","wilayet.batikh.official","ali_fadil","waedhanan","noorstars","ashraf_noon","haylatv","chef.shaheen","ahlame_hajji","raedabufatean","actress_alaa_hussein","shimaa_qasim","masa_sam"]
if "DIB" in z:
	pass
else:
	exit(0)
def inFollow_request(sessionid):
	kol = 0
	for target in inFollow:
		kol+=1
		
		time.sleep(0.50)
		head1 = {
				'HOST': "www.instagram.com",
				'KeepAlive' : 'True',
				'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
				'Cookie': 'cookie',
				'Accept' : "*/*",
				'ContentType' : "application/x-www-form-urlencoded",
				"X-Requested-With" : "XMLHttpRequest",
				"X-IG-App-ID": "936619743392459",
				"X-Instagram-AJAX" : "missing",
				"X-CSRFToken" : "missing",
				"Accept-Language" : "en-US,en;q=0.9"}		
		urlid = f'https://www.instagram.com/{target}/?__a=1'
		idd = ruks.get(urlid,headers=head1).json()["graphql"]["user"]["id"]
		if "DIB" in z:
			pass
		else:
			exit(0)
		
		urlFo = (f'https://www.instagram.com/web/friendships/{idd}/unfollow/')
		hFo = {
				'accept': '*/*',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'en-US,en;q=0.9',
				'content-length': '0',
				'content-type': 'application/x-www-form-urlencoded',
				'cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; csrftoken=wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi; ds_user_id=46165248972; sessionid='+sessionid,
				'origin': 'https://www.instagram.com',
				'referer': f'https://www.instagram.com/{target}/following/',
				'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
				'sec-ch-ua-mobile': '?0',
				'sec-fetch-dest': 'empty',
				'sec-fetch-mode': 'cors',
				'sec-fetch-site': 'same-origin',
				'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
				'x-csrftoken': 'wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi',
				'x-ig-app-id': '936619743392459',
				'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgYkq',
				'x-instagram-ajax': '753ce878cd6d',
				'x-requested-with': 'XMLHttpRequest'}
		inFo = ruks.post(urlFo,headers=hFo)
		if '"status":"ok"' in inFo.text:
			print(BC+f" infollow True {DC}|{CC} {target}{DC}|{CC} {kol}")
		else:
			print(AC+f" infollow Erorr {DC}|{CC} {target}{DC}|{CC} {kol}")
def Follow_request(cookie2,cookie3):
	good=0
	bad =0
	kol =0
	for target in Followlist:
		time.sleep(0.50)
		
		kol +=1		
		urlid = f'https://www.instagram.com/{target}/?__a=1'
	
		head1 = {
			'HOST': "www.instagram.com",
			'KeepAlive' : 'True',
			'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
			'Cookie': 'cookie',
			'Accept' : "*/*",
			'ContentType' : "application/x-www-form-urlencoded",
			"X-Requested-With" : "XMLHttpRequest",
			"X-IG-App-ID": "936619743392459",
			"X-Instagram-AJAX" : "missing",
			"X-CSRFToken" : "missing",
			"Accept-Language" : "en-US,en;q=0.9"}
		idd = ruks.get(urlid,headers=head1).json()["graphql"]["user"]["id"]
			
		urlim = f'https://www.instagram.com/web/friendships/{idd}/follow/'
		head = {
	            'accept':'*/*',
	            'accept-encoding':'gzip,deflate,br',
	            'accept-language':'en-US,en;q=0.9,ar;q=0.8',
	            'content-length':'0',
	            'content-type':'application/x-www-form-urlencoded',
	            'cookie': cookie3,
	            'origin':'https://www.instagram.com',
	            'referer':f'https://www.instagram.com/{target}/',
	            'sec-fetch-dest':'empty',
	            'sec-fetch-mode':'cors',
	            'sec-fetch-site':'same-origin',
	            'user-agent': generate_user_agent(),
	            'x-asbd-id': '437806',
	            'x-csrftoken': cookie2['csrftoken'],
	            'x-ig-app-id': '936619743392459',
	            'x-ig-www-claim': 'hmac.AR2tr9ATAjFiw03wub6DICb8kMwlARf3D1PN6R1B0JGc9Rcy',
	            'x-instagram-ajax': '0019e974ed32',
	            'x-requested-with':'XMLHttpRequest',
	        }
		follow = requests.post(urlim,headers=head,cookies=cookie2).text
		
		if '"status":"ok"' in follow:
			good +=1
			print(BC+f" Full follow up {DC}|{CC} {target}{DC}|{CC} {kol}")
		else:
			bad += 1
			print(AC+f" Erorr follow  {DC}|{CC} {target}{DC}|{CC} {kol}")
	print(BC+f" good {DC}|{CC} {good} {DC}|{AC} Bad {DC}|{CC} {bad}")
def login():
	cookie = secrets.token_hex(8)*2
	username = input(jruks+'['+_ruks+'+'+jruks+']'+ruks__+' username ! -> ;'+BGreen)
	password = input(jruks+'['+_ruks+'+'+jruks+']'+ruks__+' password ! -> ;'+BGreen)
	url = 'https://www.instagram.com/accounts/login/ajax/'
	data = {'username':username,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
            'queryParams': '{}',
            'optIntoOneTap': 'false',}            	
	headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36', 'x-csrftoken': 'missing', 'mid': cookie}		
	k = requests.post(url,headers=headers,data=data)

	if ("userId") in k.text:
		print(BC+"Dean login")
		print(DC+"="*60)
		sessionid = k.cookies['sessionid']
		cookie1 = k.cookies 		
		cookie2 = cookie1.get_dict() 		
		cookie3 = f"sessionid={cookie2['sessionid']};ds_user_id={cookie2['ds_user_id']};csrftoken={cookie2['csrftoken']};" 
		Follow_request(cookie2,cookie3)
		print(DC+"="*60)
		time.sleep(1)
		inFollow_request(sessionid)
	else:
		print(DC+"="*60)        
		print("login False")	
if "DIB" in z:

	pass
	
else:
	exit(0)
print(f"""{BC}
               [-] FOLO [-]          
        ======================================= 
 AUTHOR:MRX
 CODE BY HALO
 Telegram
 @i4m_mrx
        =======================================
        """)
print(DC+"="*60)        		        		
login()
	