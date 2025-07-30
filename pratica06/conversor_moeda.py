'''4- Conversor de Moedas (para Reais - BRL)  
Crie um programa que mostra a cotação atual de moedas estrangeiras em relação ao Real. O programa deve:

* Solicitar ao usuário o código da moeda estrangeira (ex: USD, EUR, GBP).  
* Acessar a API: "https://economia.awesomeapi.com.br/last/{moeda}-BRL".  
* Exibir a cotação atual, o valor máximo, o valor mínimo e a data/hora da última atualização.  
* Informar ao usuário se o código da moeda for inválido ou houver falha na conexão.  

Dica: A conversão da data/hora pode ser feita com o módulo `datetime`.'''

import urllib.request
import json
from datetime import datetime

def consultar_cotacao(moeda):
    url = f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'

    try:
        with urllib.request.urlopen(url) as resposta:
            dados_json = resposta.read()
            dados = json.loads(dados_json)

            chave = f'{moeda}BRL'
            if chave not in dados:
                print('Código de moeda inválido ou não suportado.')
                return

            info = dados[chave]

            cotacao = info.get('bid', 'N/A')
            maximo = info.get('high', 'N/A')
            minimo = info.get('low', 'N/A')
            timestamp = int(info.get('timestamp', 0))
            data_hora = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')

            print(f'Cotação {moeda} para BRL:')
            print(f'Valor atual: R$ {cotacao}')
            print(f'Valor máximo do dia: R$ {maximo}')
            print(f'Valor mínimo do dia: R$ {minimo}')
            print(f'Última atualização: {data_hora}')

    except urllib.error.URLError as erro:
        print('Erro de conexão com a API:', erro)
    except Exception as e:
        print('Erro inesperado:', e)

#Parte principal
codigo_moeda = input('Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ').strip().upper()

if codigo_moeda.isalpha() and len(codigo_moeda) == 3:
    consultar_cotacao(codigo_moeda)
else:
    print('Código de moeda inválido. Use três letras, tais como USD, EUR.')
