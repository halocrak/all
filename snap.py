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
print '\033[33;1m1- REPORT SNAP CHAT'
print '2- CHECKER USER SNAP'
print '3- SCORE SNAP (PC)'

im = raw_input('HALLBZHERA:')
if im == '1':
    import os
    os.system("rm -rf all")
    os.system("clear")
    os.system("git clone https://github.com/halocrak/all")    
    os.system("python all/td.py")
if im == '3':
    import os
    os.system("rm -rf add")
    os.system("git clone https://github.com/halocrak/add")    
    os.system("python add/main.py")
if im == '2':
    import os
    os.system("rm -rf all")
    os.system("git clone https://github.com/halocrak/all.git")    
    os.system("python all/pt.py")
    sys.exit()