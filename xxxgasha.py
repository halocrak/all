import random
import os


os.system("rm -rif numcombo.txt")
kkm = input("NAWEK BNWSA : ")
b =("0750","0783","0751","0782","0771","0770","0772","0773","0780","0774","0781")
g =("112233445566","112233445566","123456654321","1234512345","1234554321")
saz =("_",".")
qq =("@yahoo.com","@gmail.com","@hotmali.com")
op=open("numcombo.txt","w")
for x in range(100000000):
	f = "1234567890"
	x1 = random.choice(f)
	x2 = random.choice(b)
	x3 = random.choice(f)
	x4 = random.choice(f)
	x5 = random.choice(f)
	x6 = random.choice(f)
	x7 = random.choice(f)
	x8 = random.choice(f)
	x9 = random.choice(f)
	x10 = random.choice(g)
	x11 = random.choice(f)
	x12 = random.choice(f)
	x13 = random.choice(f)
	x14 = random.choice(f)
	x15 = random.choice(saz)
	x16 = random.choice(qq)
	dd = kkm+x1+x3+x4
	
	jk = dd+x16+":"+dd
	print(jk)
	op.write(jk+"\n")
	
	