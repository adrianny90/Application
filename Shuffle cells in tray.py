import requests

url_prefix = 'https://cellapi.de.tesla.com/v1/prd/trays/'
url_postfix = '/sorter-shuffle-test'
trays = ['C80AS002660:ZB'
         ]
allgood = '?allgood=true'
# '?type=1&allgood=true'
type='?type=4'
for tray in trays:
    url = url_prefix + tray + url_postfix + type
    response = requests.post(url, verify=False)
    print(response)
