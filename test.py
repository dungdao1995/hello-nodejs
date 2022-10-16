import requests

access_token = 'LuyTPig2cdbVqu2NVKUhwunCd9jopx89UPMmK5Dl'
headers = {'Authorization': 'Bearer ' + access_token}
url = "https://api.cryptoquant.com/v1/btc/exchange-flows/netflow?exchange=binance&window=day&from=20191001&limit=1"
print(requests.get(url, headers=headers).json())