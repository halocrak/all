import requests
import time
import re
import os
os.system('clear')


   
                                                                                                                              
                                                                                                                                                                                           
                                                                                                                                                                                                          
print('\033[1;30;40m[+] 1-  Report tiktok  ')
kurd = input('\033[1;30;40m[+] halbzhera==> : \x1b[0m')
if kurd == '1':
    time.sleep(1)
    print('''
[+] Spam
''')
    time.sleep(1)
    print('[!] Report All ....')
    time.sleep(1)
    print("")
    id1 = input('\033[1;30;40m[+] User  ==> : \x1b[0m')
    print('[+] Started Report...')
    url = f'https://www.tiktok.com/@{id1}?'
    req = requests.get(url).text
    ref = re.findall('"pageId":"(.*?)"', req)
    ref2 = "".join(ref)
    url1 = f'https://www.tiktok.com/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web&referer=https:%2F%2Fwww.tiktok.com%2Flogout%3Fredirect_url%3Dhttps%253A%252F%252Fwww.tiktok.com%252F%2540{id1}%253Flang%253Dar%2526is_copy_url%253D1%2526is_from_webapp%253Dv1%26lang%3Dar&root_referer=https:%2F%2Fwww.google.com%2F&user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F88.0.4324.150+Safari%2F537.36&cookie_enabled=true&screen_width=1366&screen_height=768&browser_language=ar&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F88.0.4324.150+Safari%2F537.36&browser_online=true&ac=3g&timezone_name=Asia%2FRiyadh&page_referer=https:%2F%2Fwww.tiktok.com%2F%3Flang%3Dar&priority_region=&verifyFp=verify_kktawy8t_4JksVm1Z_b02R_4OZw_8Xow_ltbTSgi07rs4&appId=1233&region=SA&appType=m&isAndroid=false&isMobile=false&isIOS=false&OS=windows&did=6926024599109109250'
    headers1 = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '102',
    'content-type': 'application/json',
    'cookie': 'tt_webid_v2=6926024599109109250; tt_webid=6926024599109109250; s_v_web_id=verify_kktawy8t_4JksVm1Z_b02R_4OZw_8Xow_ltbTSgi07rs4; ttwid=1%7CuU0ZIsyDyN3VZI2n8WRgeKbCOnBi7rzo0O5ubfexN7c%7C1612590836%7C1c5cb49ee5e8f958b35190103ce1ea37891a648dc344853098c36dd9d798f52b; passport_csrf_token=abd11d0de6008199789a3435e8e75597; passport_csrf_token_default=abd11d0de6008199789a3435e8e75597; store-idc=alisg; store-country-code=sa; passport_auth_status=0a5f55489be7d62253f3cc65c0176ba7%2C; passport_auth_status_ss=0a5f55489be7d62253f3cc65c0176ba7%2C; tt_csrf_token=3H0AVQGcx3wrGM9Ct5CM86g8; bm_sz=CEDD94E411A442C0D8E8E4DB52B38D15~YAAQlV4zVqiAhxl3AQAAxXWqjArR9DTcYUvyaCSG9u+t7aVTy7HuDoYx8ajcmmNYUnwVb0ofH6T45tb9rcEchG+dZ4pafmNiEuCgKDh0ryEQnEyo0PmCAosf+kaD7eKlDjPVXIxQUXf+QsOTAfcADI7+LVaBsHrfiMGjZC/yYdGdPc3B1IeIjgQ46A3C6u/G; ak_bmsc=C95264048DEF32C5F485D597CDDA107556335E95983C0000AD0224609B6F3619~plon9AFfsdCa7UthZMJWRzvGwvRyLQ9TuVg+nGfF+pqdoJq0xsnTEMvqOMic/6Az69Gp+PhH8OyzdeFjv86fX+1HiIEvt3Nektr52S8c/swDc2/xxX0TmLwEMvkRcIev4RiKFJb8HALUwB8ApgJX3xwAnyS3fWmZoMoVhJ+rGQguO2eQTW3kR/8tfx4DRAwQJi3QGGHtxLpyQHXTCEByGOc0zqJ6mwBcrZkPyh/ot6GetqN0U9NhRVe6Fb23lvr43L; csrf_session_id=fdc677247e844960a04f30d6d0b0a0fd; MONITOR_WEB_ID=6926024599109109250; _abck=D86CAAA87344DFBC4EA1879ADDCFE240~0~YAAQjl4zVhGq6f92AQAAnT/TjAUKGXHN19p4EVtqmzMGH7FlwvEIvovKpDne9kvqd5zYRK/ZQ1mCfjCPOg13LPS1MAAdbrvl8e07eG7Pn01jAIIuHJ5x3obR3AFPPEThQ5+PZNJwU9hhvBGqr3DYjAPmKUpsOKJEm679IBKf+SNlyBPfgJYm0I2iF9lhwxHvW9opR60PjzHUaD4CTgjmTxM9jRGinMRQMYjg1FK/tTsDhx0zmnFvR7CUlJs9ePjiBmf3G1aA7pM3q092HOB7egyQtMjas5G7go1ur0J+eOiM0OeSXyO1UaTw0KiCIUNBuuvPsR9l/fM9zKmxA0c9xkZdlhtSrA==~-1~||-1||~-1; odin_tt=79ba0c090463658d4e00cea7ef9d83836810b0b60877fec0060cefae0a0bc7548b6391b7cdff121053c133136653b22d7f34a3a4f8fbbc1c746a72e99258b380dd070278f0ec3519a5a8162c48369a69; sid_guard=e1e9772b7f3ee4d7de9f5142d6dd8028%7C1612975986%7C21600%7CWed%2C+10-Feb-2021+22%3A53%3A06+GMT; uid_tt=e7564b699b2f412e7d98038a067e6c89; uid_tt_ss=e7564b699b2f412e7d98038a067e6c89; sid_tt=e1e9772b7f3ee4d7de9f5142d6dd8028; sessionid=e1e9772b7f3ee4d7de9f5142d6dd8028; sessionid_ss=e1e9772b7f3ee4d7de9f5142d6dd8028; bm_sv=BE8DC204511096FF25C1C4C74525246F~JFcUOsKuslhtsbwJCHYiRHmC8qSngmagSpzdnLsxA7i3mO40Rit2u/Azu7dWJMzPwWSXSApVM4M6YQ2ET26E8N7ggWII9nohsu/p8tiLh60p8c6NlUXJiJnjuMM2x7hGZYVze8qLe9UUMDSsGon7ZV9HBDojB1TR7d/IJAjByzY=',
    'origin': 'https://www.tiktok.com',
    'referer': f'https://www.tiktok.com/@{id1}?lang=ar&is_copy_url=1&is_from_webapp=v1',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'tt-csrf-token': '3H0AVQGcx3wrGM9Ct5CM86g8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'x-secsdk-csrf-token': '000100000001788eba932e33cf37b46dd7526624d86a87a58ecd646527ab2b87387e800e86d21662711de009d90a'
    }
    data1 = {
    'object_id': f"{ref2}",
    'owner_id': f"{ref2}",
    'reason': '310',
    'report_type': "user"
    }
    url2 = f'https://www.tiktok.com/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web&referer=https:%2F%2Fwww.tiktok.com%2Flogout%3Fredirect_url%3Dhttps%253A%252F%252Fwww.tiktok.com%252F%2540{id1}%253Flang%253Dar%2526is_copy_url%253D1%2526is_from_webapp%253Dv1%26lang%3Dar&root_referer=https:%2F%2Fwww.google.com%2F&user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F88.0.4324.150+Safari%2F537.36&cookie_enabled=true&screen_width=1366&screen_height=768&browser_language=ar&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F88.0.4324.150+Safari%2F537.36&browser_online=true&ac=4g&timezone_name=Asia%2FRiyadh&page_referer=https:%2F%2Fwww.tiktok.com%2F%3Flang%3Dar&priority_region=&verifyFp=verify_kktawy8t_4JksVm1Z_b02R_4OZw_8Xow_ltbTSgi07rs4&appId=1233&region=SA&appType=m&isAndroid=false&isMobile=false&isIOS=false&OS=windows&did=6926024599109109250'
    headers2 = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '102',
    'content-type': 'application/json',
    'cookie': 'tt_webid_v2=6926024599109109250; tt_webid=6926024599109109250; s_v_web_id=verify_kktawy8t_4JksVm1Z_b02R_4OZw_8Xow_ltbTSgi07rs4; ttwid=1%7CuU0ZIsyDyN3VZI2n8WRgeKbCOnBi7rzo0O5ubfexN7c%7C1612590836%7C1c5cb49ee5e8f958b35190103ce1ea37891a648dc344853098c36dd9d798f52b; passport_csrf_token=abd11d0de6008199789a3435e8e75597; passport_csrf_token_default=abd11d0de6008199789a3435e8e75597; store-idc=alisg; store-country-code=sa; passport_auth_status=0a5f55489be7d62253f3cc65c0176ba7%2C; passport_auth_status_ss=0a5f55489be7d62253f3cc65c0176ba7%2C; tt_csrf_token=3H0AVQGcx3wrGM9Ct5CM86g8; bm_sz=CEDD94E411A442C0D8E8E4DB52B38D15~YAAQlV4zVqiAhxl3AQAAxXWqjArR9DTcYUvyaCSG9u+t7aVTy7HuDoYx8ajcmmNYUnwVb0ofH6T45tb9rcEchG+dZ4pafmNiEuCgKDh0ryEQnEyo0PmCAosf+kaD7eKlDjPVXIxQUXf+QsOTAfcADI7+LVaBsHrfiMGjZC/yYdGdPc3B1IeIjgQ46A3C6u/G; ak_bmsc=C95264048DEF32C5F485D597CDDA107556335E95983C0000AD0224609B6F3619~plon9AFfsdCa7UthZMJWRzvGwvRyLQ9TuVg+nGfF+pqdoJq0xsnTEMvqOMic/6Az69Gp+PhH8OyzdeFjv86fX+1HiIEvt3Nektr52S8c/swDc2/xxX0TmLwEMvkRcIev4RiKFJb8HALUwB8ApgJX3xwAnyS3fWmZoMoVhJ+rGQguO2eQTW3kR/8tfx4DRAwQJi3QGGHtxLpyQHXTCEByGOc0zqJ6mwBcrZkPyh/ot6GetqN0U9NhRVe6Fb23lvr43L; csrf_session_id=fdc677247e844960a04f30d6d0b0a0fd; MONITOR_WEB_ID=6926024599109109250; odin_tt=79ba0c090463658d4e00cea7ef9d83836810b0b60877fec0060cefae0a0bc7548b6391b7cdff121053c133136653b22d7f34a3a4f8fbbc1c746a72e99258b380dd070278f0ec3519a5a8162c48369a69; sid_guard=e1e9772b7f3ee4d7de9f5142d6dd8028%7C1612975986%7C21600%7CWed%2C+10-Feb-2021+22%3A53%3A06+GMT; uid_tt=e7564b699b2f412e7d98038a067e6c89; uid_tt_ss=e7564b699b2f412e7d98038a067e6c89; sid_tt=e1e9772b7f3ee4d7de9f5142d6dd8028; sessionid=e1e9772b7f3ee4d7de9f5142d6dd8028; sessionid_ss=e1e9772b7f3ee4d7de9f5142d6dd8028; bm_sv=BE8DC204511096FF25C1C4C74525246F~JFcUOsKuslhtsbwJCHYiRHmC8qSngmagSpzdnLsxA7i3mO40Rit2u/Azu7dWJMzPwWSXSApVM4M6YQ2ET26E8N7ggWII9nohsu/p8tiLh61QrCoHj5w/gSzZaNy1d6/WU2+Om/yOSP/tA/LXIq2ZmZId6brtxawDlJMtVZuKMW0=; _abck=D86CAAA87344DFBC4EA1879ADDCFE240~0~YAAQfl4zVrtO8/92AQAA8KPfjAXsxiD/MdAlLTP6NSsVlU7O+R0tkpL0uIorFUemWyXLTjMbkTb/HWatAdQaJIz623vb+hw4iFfq0yyZZl5RTRUIblOkzAz1M4NeQJZUVorRdy+3P6lMpw4zRTKACbSWfpeb6F/eRLD17c9rxBHkZnH1R8ERpGGmMsmbVbgFsd9tz1Xm19B1yZUtrYPuwWErRwKrgMl4cKxvJiN+RFHVu9hmQQpfU4lLB/5YnP3E9UOuE4w/dlq6YRSi1O9RL/FADZd/ctdZ2las4F5s4A/fKKDMRHwVuB/3zA/YRWjD25NJTqvmAnU84xDUHxf/flaB2GWJ8Q==~-1~-1~-1',
    'origin': 'https://www.tiktok.com',
    'referer': f'https://www.tiktok.com/@{id1}?lang=ar&is_copy_url=1&is_from_webapp=v1',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'tt-csrf-token': '3H0AVQGcx3wrGM9Ct5CM86g8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'x-secsdk-csrf-token': '000100000001788eba932e33cf37b46dd7526624d86a87a58ecd646527ab2b87387e800e86d21662711de009d90a'
    }
    data2 = {
    'object_id': f"{ref2}",
    'owner_id': f"{ref2}",
    'reason': '306',
    'report_type': "user"
    }
    url3 = f'https://www.tiktok.com/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web&referer=https:%2F%2Fwww.tiktok.com%2Flogout%3Fredirect_url%3Dhttps%253A%252F%252Fwww.tiktok.com%252F%2540{id1}%253Flang%253Dar%2526is_copy_url%253D1%2526is_from_webapp%253Dv1%26lang%3Dar&root_referer=https:%2F%2Fwww.google.com%2F&user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F88.0.4324.150+Safari%2F537.36&cookie_enabled=true&screen_width=1366&screen_height=768&browser_language=ar&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F88.0.4324.150+Safari%2F537.36&browser_online=true&ac=4g&timezone_name=Asia%2FRiyadh&page_referer=https:%2F%2Fwww.tiktok.com%2F%3Flang%3Dar&priority_region=&verifyFp=verify_kktawy8t_4JksVm1Z_b02R_4OZw_8Xow_ltbTSgi07rs4&appId=1233&region=SA&appType=m&isAndroid=false&isMobile=false&isIOS=false&OS=windows&did=6926024599109109250'
    headers3 = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '103',
    'content-type': 'application/json',
    'cookie': 'tt_webid_v2=6926024599109109250; tt_webid=6926024599109109250; s_v_web_id=verify_kktawy8t_4JksVm1Z_b02R_4OZw_8Xow_ltbTSgi07rs4; ttwid=1%7CuU0ZIsyDyN3VZI2n8WRgeKbCOnBi7rzo0O5ubfexN7c%7C1612590836%7C1c5cb49ee5e8f958b35190103ce1ea37891a648dc344853098c36dd9d798f52b; passport_csrf_token=abd11d0de6008199789a3435e8e75597; passport_csrf_token_default=abd11d0de6008199789a3435e8e75597; store-idc=alisg; store-country-code=sa; passport_auth_status=0a5f55489be7d62253f3cc65c0176ba7%2C; passport_auth_status_ss=0a5f55489be7d62253f3cc65c0176ba7%2C; tt_csrf_token=3H0AVQGcx3wrGM9Ct5CM86g8; bm_sz=CEDD94E411A442C0D8E8E4DB52B38D15~YAAQlV4zVqiAhxl3AQAAxXWqjArR9DTcYUvyaCSG9u+t7aVTy7HuDoYx8ajcmmNYUnwVb0ofH6T45tb9rcEchG+dZ4pafmNiEuCgKDh0ryEQnEyo0PmCAosf+kaD7eKlDjPVXIxQUXf+QsOTAfcADI7+LVaBsHrfiMGjZC/yYdGdPc3B1IeIjgQ46A3C6u/G; ak_bmsc=C95264048DEF32C5F485D597CDDA107556335E95983C0000AD0224609B6F3619~plon9AFfsdCa7UthZMJWRzvGwvRyLQ9TuVg+nGfF+pqdoJq0xsnTEMvqOMic/6Az69Gp+PhH8OyzdeFjv86fX+1HiIEvt3Nektr52S8c/swDc2/xxX0TmLwEMvkRcIev4RiKFJb8HALUwB8ApgJX3xwAnyS3fWmZoMoVhJ+rGQguO2eQTW3kR/8tfx4DRAwQJi3QGGHtxLpyQHXTCEByGOc0zqJ6mwBcrZkPyh/ot6GetqN0U9NhRVe6Fb23lvr43L; csrf_session_id=fdc677247e844960a04f30d6d0b0a0fd; MONITOR_WEB_ID=6926024599109109250; odin_tt=79ba0c090463658d4e00cea7ef9d83836810b0b60877fec0060cefae0a0bc7548b6391b7cdff121053c133136653b22d7f34a3a4f8fbbc1c746a72e99258b380dd070278f0ec3519a5a8162c48369a69; sid_guard=e1e9772b7f3ee4d7de9f5142d6dd8028%7C1612975986%7C21600%7CWed%2C+10-Feb-2021+22%3A53%3A06+GMT; uid_tt=e7564b699b2f412e7d98038a067e6c89; uid_tt_ss=e7564b699b2f412e7d98038a067e6c89; sid_tt=e1e9772b7f3ee4d7de9f5142d6dd8028; sessionid=e1e9772b7f3ee4d7de9f5142d6dd8028; sessionid_ss=e1e9772b7f3ee4d7de9f5142d6dd8028; _abck=D86CAAA87344DFBC4EA1879ADDCFE240~0~YAAQfl4zVrtO8/92AQAA8KPfjAXsxiD/MdAlLTP6NSsVlU7O+R0tkpL0uIorFUemWyXLTjMbkTb/HWatAdQaJIz623vb+hw4iFfq0yyZZl5RTRUIblOkzAz1M4NeQJZUVorRdy+3P6lMpw4zRTKACbSWfpeb6F/eRLD17c9rxBHkZnH1R8ERpGGmMsmbVbgFsd9tz1Xm19B1yZUtrYPuwWErRwKrgMl4cKxvJiN+RFHVu9hmQQpfU4lLB/5YnP3E9UOuE4w/dlq6YRSi1O9RL/FADZd/ctdZ2las4F5s4A/fKKDMRHwVuB/3zA/YRWjD25NJTqvmAnU84xDUHxf/flaB2GWJ8Q==~-1~-1~-1; bm_sv=BE8DC204511096FF25C1C4C74525246F~JFcUOsKuslhtsbwJCHYiRHmC8qSngmagSpzdnLsxA7i3mO40Rit2u/Azu7dWJMzPwWSXSApVM4M6YQ2ET26E8N7ggWII9nohsu/p8tiLh63FOdDR93DRy/7eK+6Q9eE6lML02i620733Uf7aOjwkcE8u3Ftj/XPTm7x6xt5Mlvg=',
    'origin': 'https://www.tiktok.com',
    'referer': f'https://www.tiktok.com/@{id1}?lang=ar&is_copy_url=1&is_from_webapp=v1',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'tt-csrf-token': '3H0AVQGcx3wrGM9Ct5CM86g8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'x-secsdk-csrf-token': '000100000001788eba932e33cf37b46dd7526624d86a87a58ecd646527ab2b87387e800e86d21662711de009d90a'
    }
    data3 = {
    'object_id': f"{ref2}",
    'owner_id': f"{ref2}",
    'reason': '3051',
    'report_type': "user"
    }
    while True:
        time.sleep(3)
        req1 = requests.post(url1, json=data1, headers=headers1).text
        if '{"statusCode":0,"body":{"statusCode":0,"errMsg":"نشكرك على ملاحظاتك"},"errMsg":"نشكرك على ملاحظاتك"}' in req1:
            print('\033[1;32m[+] Report Orginal Has Been Sent')
        else:
            print('\033[1;32m[+] Report Has Been Sent')
        time.sleep(3)
        req2 = requests.post(url2, json=data2, headers=headers2).text
        if '{"statusCode":0,"body":{"statusCode":0,"errMsg":"نشكرك على ملاحظاتك"},"errMsg":"نشكرك على ملاحظاتك"}' in req2:
            print('\033[1;32m[+] Report Hate Speech Has Been Sent')
        else:
            print('\033[1;32m[+] Report Has Been Sent')
        time.sleep(3)
        req3 = requests.post(url3, json=data3, headers=headers3).text
        if '{"statusCode":0,"body":{"statusCode":0,"errMsg":"نشكرك على ملاحظاتك"},"errMsg":"نشكرك على ملاحظاتك"}' in req3:
            print('[+] Report tiktok sent')
        else:
            print('\033[1;32m[+] Report tiktok Sent')
