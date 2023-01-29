import requests

apiKey = '46A4AAF6-49B3-42C5-8311-F898324F8723'
moneda_cripto  = input("escribe una moneda cripto conocida:").upper()

while moneda_cripto != "" and moneda_cripto.isalpha():
    
    r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apiKey}')

    #print(r.status_code)

    #print(r.text)

    #capturar resultados correctos
    resultado = r.json() #GUARDA EL R.JSON en resultado (diccionario en python)
    if r.status_code == 200: 
        # valor = round(resultado["rate"],4)
        # print(f"{valor} €")
        print("{:,.2f}€".format(resultado["rate"]))
    else: 
        print(resultado["error"])
#capturar errores

#como controlo inputs vacios, q no realice consulta si el input esta vacio

    moneda_cripto = input("escribe una moneda cripto conocida:").upper()



