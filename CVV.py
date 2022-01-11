import requests

E = '\033[1;32m'
T = '\033[1;33m'
n ='\033[1;36m'
R =('='*60)
print(f"""{E}{R}
   ____  __     __ __     __
  / ___| \ \   / / \ \   / /
 | |      \ \ / /   \ \ / / 
 | |___    \ V /     \ V /  
  \____|    \_/       \_/  @python968
{R}""")
API_TOKEN = input('TOKEN:')
id=input(' ID:')
def xoshnaw():
    ruks = requests.Session()
    url = "https://www.colorschemer.com/fetchdata/generate-home-credit-card/"
    headers = {
        "Host": "www.colorschemer.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.colorschemer.com/credit-card-generator/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Length": "98",
        "Origin": "https://www.colorschemer.com",
        "DNT": "1",
        "Connection": "keep-alive",
        "Cookie": "__cfduid=dc0c9026439474694eeab705e7e633e8d1616410321; csrftoken=czvtORBrer3uv45UuVbKfDbESjgFQqk8xi9obC59foTQPO9mqlWBUirb2mY6jSOx; cookieconsent_status=dismiss"}
    data = 'brand=VISA&country=UNITED+STATES&bank=1880+BANK&cvv=&year=random&range=500+-+1000&amount=20&pin=on'
    r = ruks.post(url,headers=headers,data=data)
    a = 0
    h=0
    while True:
        h+=1
        
        try:
            
            card_number = int(r.json()['creditCard'][a]['CardNumber'])
            Bank = str(r.json()['creditCard'][a]['Bank'])
            name = str(r.json()['creditCard'][a]['Name'])
            Address = str(r.json()['creditCard'][a]['Address'])
            CVV = int(r.json()['creditCard'][a]['CVV'])
            Data_time = str(r.json()['creditCard'][a]['Expiry']) 
            print(f'\r{E}{h}',end=f"{T}--Good")          
            tlg =(f'https://api.telegram.org/bot{API_TOKEN}/sendMessage?chat_id={id}&text=\n----------\n{card_number}|{CVV}|{Data_time}|{Bank}|{name}|{Address} \n----------\n {ruksz} ')
            req = requests.post(tlg)
            a+=1
        except:
            print('')
            print(T+'')
            break
xoshnaw()
