import json
import urllib.request
import webbrowser
import os
try:
    R='\033[91m'
    Y='\033[93m'
    G='\033[92m'
    CY='\033[96m'
    W='\033[97m'
    path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
    def start():
        os.system('clear')
        print (CY+"""
                                             
,------.,------. ,------.  ,-----. ,------.  
|  .---'|  .--. '|  .--. ''  .-.  '|  .--. ' 
|  `--, |  '--'.'|  '--'.'|  | |  ||  '--'.' 
|  `---.|  |\  \ |  |\  \ '  '-'  '|  |\  \  
`------'`--' '--'`--' '--' `-----' `--' '--' 
                                             

"""+Y+"""v1.0"""+G+"""
             
      Zaneary Lasar IP
"""+R+""">>"""+Y+"""----"""+CY+""" Author - MRX """+Y+"""----"""+R+"""<<""")
        
    def m3():
        try:
            print(R+"""\n
#"""+Y+""" Halbzhera ==>"""+G+""" >>"""+Y+"""
1)"""+G+""" Zaneary Lasar Ip Xot"""+Y+"""
2)"""+G+""" Zaneary Lasar IP Kasany Tr Websit"""+Y+"""
3)"""+G+""" Exit
""")
            ch=int(input(CY+"Halbzhera: "+W))
            if ch==1:
                main2()
                m3()
            elif ch==2:
                main()
                m3()
            elif ch==3:
                print(Y+"Exit................"+W)
            else:
                print(R+"\Halat Krd La Halbzhardn Dubara Halbzhera\n")
                m3()
        except ValueError:
            print(R+"\Halat Krd La Halbzhardn Dubara Halbzhera\n")
            m3()
        
    def finder(u):
        try:
            try:
                response = urllib.request.urlopen(u)
                data = json.load(response)
                ip=data['query']
                org=data['org']
                c=data['city']
                cont=data['country']
                reg=data['regionName']
                latt=data['lat']
                lonp=data['lon']

                print(R+"\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print(Y+'\n>>>'+CY+' IP address details\n ')
                print(G+"1) IP Address : "+Y,ip,'\n')
                print(G+"2) Org : "+Y,org,'\n')
                print(G+"3) City : "+Y,c,'\n')
                print(G+"4) Region : "+Y,reg,'\n')
                print(G+"5) Country : "+Y,cont,'\n')
                print(G+"6) Location\n")
                print(G+"\tLattitude : "+Y,latt,'\n')
                print(G+"\tLongitude : "+Y,lonp,'\n')
                l='https://www.google.com/maps/place/'+str(latt)+'+'+str(lonp)
                print(R+"\n#"+Y+" Google Map link : "+CY,l)
                path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
                if path:
                    link='am start -a android.intent.action.VIEW -d '+str(l)
                    pr=input(R+"\n>>"+Y+" Ataue Har Esta Shueny Bzany Ba Naxsha??"+G+" (y|n): "+W)
                    if pr=="y":
                        lnk=str(link)+" > /dev/null"
                        os.system(str(lnk))
                        start()
                        m3()
                    elif pr=="n":
                        print("\nBo Darchun La TooL Ctrl + C\n\n")
                        start()
                        m3()
                    else:
                        print("\Xalat Halt Bzhard Dubara Halbzhera !\n")
                        m3()
                else:
                    pr=input(R+"\n>>"+Y+" Ataue Har Esta Shueny Bzany Ba Naxsha?"+G+" (y|n): "+W)
                    if pr=="y":
                        webbrowser.open(l,new=0)
                        start()
                        m3()
                    elif pr=="n":
                        print(R+"\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        print(Y+"\nBo Darchun La Tool  "+R+"Ctrl + C\n\n")
                        start()
                        m3()
                    else:
                        print(R+"\Xalat Halt Bzhard Dubara Halbzhera !\n")
                        m3()
                return
            except KeyError:
                print(R+"\n  IP XLAT nusea\n"+W)
                m3()
        except urllib.error.URLError:
            print(R+"\nError!"+Y+" Entarnet Pchra !\n"+W)
            exit()

        
    def main():
        u=input(G+"\n>>> "+Y+":"+W+" ")
        if u=="":
            print(R+"\nEnter valid IP Address/website address!")
            main()
        else:
            url ='http://ip-api.com/json/'+u
            finder(url)
    def main2():
        url ='http://ip-api.com/json/'
        finder(url)
        
    start()
    m3()
except KeyboardInterrupt:
    print(Y+"\nInterrupted ! Have a nice day :)"+W)