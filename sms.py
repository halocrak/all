import os
import sys
import time
import requests
os.system('clear')



logo = """   \033[5;37;40m

-------------------------------
      AUTHER: HALO
       [+] Instagram : i4m_rio
       [+] Telegram  : i4m_mrx
       [+] snapchat  : im_halo0
       [+] github    : halocrak
       [+] facebook  : imfor halo
       [+] youtube   : MRX CODAR
-------------------------------
"""

print logo
print '\033[33;1m1- Phone Number Information'
print '2- Attack Phone Number '


im = raw_input('HALLBZHERA:')
if im == '1':
    import os
    os.system("rm -rf all")
    os.system("clear")
    os.system("git clone https://github.com/halocrak/all")    
    os.system("python all/sp.py")
if im == '2':
    import os
    os.system("rm -rf all")
    os.system("git clone https://github.com/halocrak/all.git")    
    os.system("bash all/sms.sh")
    sys.exit()