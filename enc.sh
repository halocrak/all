#!/bin/bash

# Kode bokep
w="\033[39;1m" #ini jav
r2='\033[31m' #ini barat

echo -e $r2"HALO ENCRYPT VIP"

echo ""
echo -e $r2"["$w"!"$r2"] Am Toola Bo Enc Python a"
echo ""
echo -e -n $r2"["$w"?"$r2"]"$w" Nawi Fail : "$r2"> "$w
read script;
echo -e $r2"["$w"*"$r2"]"$w" Tozek BosTa "
cd /sdcard
sleep 3
python2 -OO -m py_compile $script
rm $script
mv $script"o" $script
echo -e $r2"["$w"√"$r2"]"$w"Tawaw Enc Bu"

#
#