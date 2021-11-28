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
print '\033[31;1m1- DOWLOD HTML WEB'
print '2- HOST WEB'



im = raw_input('HALLBZHERA:')
if im == '1':
    import os
    os.system("clear")
    os.system("git clone https://github.com/halocrak/staf")    
    os.system("python all/download-html.py")
if im == '2':
    import os
    os.system("clear")
    os.system("rm -rf all")
    os.system("git clone https://github.com/halocrak/all.git")    
    os.system("python2 all/auto-deface.py")
    sys.exit()