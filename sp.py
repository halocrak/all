import os
import sys
import time
import requests
import time,sys
os.system('clear')
logo = """
\x1b[1;92m
 __    __       ___       __        ______   
|  |  |  |     /   \     |  |      /  __  \  
|  |__|  |    /  ^  \    |  |     |  |  |  | 
|   __   |   /  /_\  \   |  |     |  |  |  | 
|  |  |  |  /  _____  \  |  `----.|  `--'  | 
|__|  |__| /__/     \__\ |_______| \______/  
                                             

                        
"""
print (logo)
token_login =input('token bot:')
id_login =input('id tlegram:')
import halo 
halo =input('zhmaraka baby +:')
url = requests.get('https://api.telnyx.com/anonymous/v2/number_lookup/' +halo).text
requests.post('https://api.telegram.org/bot'+token_login+'/sendMessage?chat_id='+id_login+'&text='+url+'\n')
os.system('figlet OK')