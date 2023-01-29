import requests

r = requests.get('https://rest.coinapi.io/v1/exchangerate/BTC/EUR?apikey=46A4AAF6-49B3-42C5-8311-F898324F8723')

print(r.status_code)

print(r.text)