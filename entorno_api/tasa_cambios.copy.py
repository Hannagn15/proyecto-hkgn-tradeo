import requests

from utils import apiKey

r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={apiKey}')
if r.status_code != 200: 
    raise Exception( "Error en consulta de assets{}".format(r.status_code) )

lista_general= r.json()
lista_criptos=[]

for item in lista_general:
    if item["type_is_crypto"] == 1:
        lista_criptos.append(item['asset_id'])

print("monedas digitales; ", len(lista_criptos))
print("monedas no digitales; ", (len(lista_general) - len(lista_criptos)))

moneda_cripto = input("escribe una moneda cripto conocida:").upper()

while moneda_cripto != "" and moneda_cripto.isalpha():

    if moneda_cripto in lista_criptos: 
        r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apiKey}')

        resultado = r.json() 
        if r.status_code == 200: 
        
            print("{:,.2f}€".format(resultado["rate"]))
        else: 
            print(resultado["error"])

    moneda_cripto = input("escribe una moneda cripto conocida:").upper()



