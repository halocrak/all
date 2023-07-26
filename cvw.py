import os
import random
import telebot
import time
zhmara_cv='1234567890'
mang=['01','02','03','04','05','06','07','08','09','10','11','12']
sal=['24','25','26','27','28']
cve='1234567890'

yak=['5','4']
halo=range(10000)
for i in halo:
    time.sleep(2)
    zh1=random.choice(zhmara_cv)
    zh2=random.choice(zhmara_cv)
    zh3=random.choice(zhmara_cv)
    zh4=random.choice(zhmara_cv)
    zh5=random.choice(zhmara_cv)
    zh6=random.choice(zhmara_cv)
    zh7=random.choice(zhmara_cv)
    zh8=random.choice(zhmara_cv)
    zh9=random.choice(zhmara_cv)
    zh10=random.choice(zhmara_cv)
    zh11=random.choice(zhmara_cv)
    zh12=random.choice(zhmara_cv)
    zh13=random.choice(zhmara_cv)
    zh14=random.choice(zhmara_cv)
    zh15=random.choice(zhmara_cv)
    zh16=random.choice(zhmara_cv)
    zhm=random.choice(yak)
    halo=(zhm+zh1+zh2+zh3+zh4+zh5+zh6+zh7+zh8+zh9+zh10+zh11+zh12+zh13+zh14+zh15+zh16)
    salm=random.choice(sal)
    mangm=random.choice(mang)
    cve1=random.choice(cve)
    cve2=random.choice(cve)
    cve3=random.choice(cve)
    cvem=(cve1+cve2+cve3)
    mrx=(halo+'|'+mangm+'|'+salm+'|'+cvem)
    print(mrx)
