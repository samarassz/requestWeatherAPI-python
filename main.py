import requests

url = 'http://api.weatherapi.com/v1/current.json?key=ece0b720322f466a9da165832211209'
local = '&q='+input('Digite o nome da cidade: ')
lang = '&lang=pt'

def search():
    response = requests.get(url+local+lang)
    erro = False
    if response.status_code == 200:
        data = response.json()
        cidade = data['location']['name']
        estado = data['location']['region']
        pais = data['location']['country']
        tempC = data['current']['temp_c']
        condicao = data['current']['condition']['text']
        sensacaoC = data['current']['feelslike_c']
        umidade = data['current']['humidity']
    else:
        erro == True
    if erro == False:
        print(
            'Clima em', cidade, estado, pais, '\n',
            'Temperatura:', tempC, 'ºC', '\n',
            'Condição:', condicao, '\n',
            'Sensação Térmica:', sensacaoC,'ºC', '\n',
            'Umidade:', umidade,'%'
        )
    else:
        print('Minha nossa! Um erro!')

if __name__ == '__main__':
    search()