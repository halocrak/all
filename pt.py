import requests,random,time
x2 = '[🖤] - @i4m_mrx'
j='''
[☑️] SNAPCHAT USER:
'''
print("snapChat checker By @i4m_mrx \n  ")
ID=input("YOUR TELEGRAM ID: ")
token=input("YOUR BOT TOKEN: ")
count = 0
req = requests.session()
user = ""


length = int(8)
chars = "qwertyuiopasdfghjklzxcvbnm1234567890_"
while True:
    time.sleep(1.2)
    if count < 1000:
        count += 1
        for user in range(1):
            user = ""
            for item in range(length):
                user += random.choice(chars)
        url = 'https://accounts.snapchat.com/accounts/get_username_suggestions'
        headers_check = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '57',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'cookie': 'xsrf_token=qguFhKiP7FrimtibnGvopQ; web_client_id=6dee3ce3-db42-4fd0-b538-682cdb294f9a; _scid=482919d7-1390-46c8-8951-d3031e352b63; _sca={%22cid%22:%22e22c1577-7f73-4b69-85ff-79b72444951a%22%2C%22token%22:%22v1.key.2020-03-05_UKiB4eNE.iv.MeUzIJboKx7l+nZu.zf9r/dgUl/1vg1iBp4fz27qapzxGL1VJowr9Clna1AvHYCTUocABFHpeSMdPC2BGmfDmAfrA8eEqFPnV5qNP/QJCPISHEUpj7aGeYGpoggjapYZZ%22}; sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true; _ga=GA1.2.148694331.1613677502; _gid=GA1.2.1609447525.1613677502; _gat_UA-41740027-4=1',
        'origin': 'https://accounts.snapchat.com',
        'referer': 'https://accounts.snapchat.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
        }
        data_checker = {
            'requested_username': user,
            'xsrf_token': 'qguFhKiP7FrimtibnGvopQ'}
        req_checker = requests.post(url, data=data_checker, headers=headers_check).text
        if '"status_code":"OK"' in req_checker:
        	print(f'[✅] 𝐁𝐀𝐑𝐃𝐀𝐒𝐓𝐀 ==> : {user}')
        	tele = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n𖡃 𝚄𝚂𝙴𝚁: {user}\n\n{x2}')
        	re = requests.post(tele)
        	with open('Available.txt', 'a') as x:
        		tl = '[] NEW USER -->  '
        		x.write(tl + user + '\n')
        elif '"status_code":"TAKEN"' in req_checker:
            print(f'[❌] 𝐁𝐀𝐑𝐃𝐀𝐒𝐓 𝐍𝐘𝐀 ==> : {user}')
        elif '"status_code":"INVALID_BEGIN"' in req_checker:
            print(f'[❌] 𝐁𝐀𝐑𝐃𝐀𝐒𝐓 𝐍𝐘𝐀 ==> : {user}')
        elif '"status_code":"INVALID_END"' in req_checker:
            print(f'[❌] 𝐁𝐀𝐑𝐃𝐀𝐒𝐓 𝐍𝐘𝐀 ==> : {user}')
        elif '"status_code":"DELETED"' in req_checker:
            print(f'[❌] 𝐁𝐀𝐑𝐃𝐀𝐒𝐓 𝐍𝐘𝐀 [ban] user ==> : {user}')
        elif '"status_code":"INVALID_SEPARATED"' in req_checker:
            print(f'[❌] 𝐁𝐀𝐑𝐃𝐀𝐒𝐓 𝐍𝐘𝐀 ==> : {user}')
        else:
            print(f'[❌] 𝐁𝐀𝐑𝐃𝐀𝐒𝐓 𝐍𝐘𝐀 ==> : {user}', req_checker)
