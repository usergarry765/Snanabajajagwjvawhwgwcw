import requests, secrets, re
from user_agent import generate_user_agent
import time
Cookie = secrets.token_hex(8)*8
uss = generate_user_agent()
headers = {
    'authority': 'www.gulf-up.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'Cookie': Cookie,
    'origin': 'https://www.gulf-up.com',
    'referer': 'https://www.gulf-up.com/5ddkga3tb8kx',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': uss,
}

data = {
    'op': 'download1',
    'usr_login': '',
    'id': '5ddkga3tb8kx',
    'fname': 'System launcher_RELEASE-4.21.15.3260-11081751_421153260.apk',
    'referer': '',
    'method_free': 'تحميل مجاني',
}

response = requests.post('https://www.gulf-up.com/5ddkga3tb8kx', headers=headers, data=data)

rre = re.findall(r'<td align="right"><div style="(.*?)"><span style="(.*?)">(.*?)</span><span style="(.*?)">(.*?)</span><span style="(.*?)">(.*?)</span><span style="(.*?)">(.*?)</span></div></td>', response.text)

#print(response.status_code)
p2=((rre[0][2]).replace("&#48;", "0").replace("&#49;", "1").replace("&#50;", "2").replace("&#51;", "3").replace("&#52;", "4").replace("&#53;", "5").replace("&#54;", "6").replace("&#55;", "7").replace("&#56;", "8").replace("&#57;", "9"))
p4=((rre[0][4]).replace("&#48;", "0").replace("&#49;", "1").replace("&#50;", "2").replace("&#51;", "3").replace("&#52;", "4").replace("&#53;", "5").replace("&#54;", "6").replace("&#55;", "7").replace("&#56;", "8").replace("&#57;", "9"))
p6=((rre[0][6]).replace("&#48;", "0").replace("&#49;", "1").replace("&#50;", "2").replace("&#51;", "3").replace("&#52;", "4").replace("&#53;", "5").replace("&#54;", "6").replace("&#55;", "7").replace("&#56;", "8").replace("&#57;", "9"))
p8=((rre[0][8]).replace("&#48;", "0").replace("&#49;", "1").replace("&#50;", "2").replace("&#51;", "3").replace("&#52;", "4").replace("&#53;", "5").replace("&#54;", "6").replace("&#55;", "7").replace("&#56;", "8").replace("&#57;", "9"))

#print(p2,p4,p6,p8)
###

p1=(((rre[0][1]).replace(";", ":").split(':')[3]).replace("px", ""))
p3=(((rre[0][3]).replace(";", ":").split(':')[3]).replace("px", ""))
p5=(((rre[0][5]).replace(";", ":").split(':')[3]).replace("px", ""))
p7=(((rre[0][7]).replace(";", ":").split(':')[3]).replace("px", ""))


rw = re.findall(r'name="rand" value="(.*?)"', response.text)
pr=(rw[0])
print(pr)
####
xx = {p1:p2, p3:p4, p5:p6, p7:p8}
#print(xx)
#####

a = [p1, p3, p5, p7]
j = ([int(x) for x in a])
j.sort()
hh=""
for i in j:
    #print(i)
    hh = (hh + xx[f"{i}"])
    #print(xx[f"{i}"],end="")
#print(response.text)
print(hh)
###
headersq = {
    'authority': 'www.gulf-up.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': Cookie,
    'origin': 'https://www.gulf-up.com',
    'referer': 'https://www.gulf-up.com/5ddkga3tb8kx',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': uss,
}

dataq = {
    'op': 'download2',
    'id': '5ddkga3tb8kx',
    'rand': pr,
    'referer': 'https://www.gulf-up.com/5ddkga3tb8kx',
    'method_free': 'تحميل مجاني',
    'method_premium': '',
    'adblock_detected': '0',
    'code': hh,
}
time.sleep(35)
responseq = requests.post('https://www.gulf-up.com/5ddkga3tb8kx', headers=headersq, data=dataq)


print(responseq.status_code)

###
rye = re.findall(r'<a href="(.*?)" class="downloadbtn downloadbtnmax">', responseq.text)

plink=(rye[0])
####
headerse = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Referer': 'https://www.gulf-up.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': uss,
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

#responsee = requests.get(plink,headers=headerse)
#print(responsee)
