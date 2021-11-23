import requests
import random

tok = input('tokin : ')
ID = input('id')
i =int(input('accawnt : '))
for i in range(i):
 user = '1234567890'
 us = str(''.join((random.choice(user) for i in range(7))))
 username = '+20122' + us
 password = '0122' + us
 us4 = str(''.join((random.choice(user) for i in range(8))))
 tlg =(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=ᯓ ʟᴏɢɪɴ » Facebook\n
ئەکاونتی تیک تۆک هاک بو لەسەر فەیسبوک بیکەوە
🔱 • یوسەر ☞{username}
🔱 • پاسپۆرد☞ +{us4}
🔱 • وڵات ☞ Egypt
🔱 • فۆڵۆ☞ +20 
🔱 • کاتی هاکردن ☞ 2021-10-12
ᯓ CH :@python968''')
 i = requests.post(tlg)