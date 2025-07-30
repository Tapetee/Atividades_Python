'''3- Consulta de CEP  
Desenvolva um programa que consulta dados de endereço a partir de um CEP brasileiro. Siga os passos abaixo:

* Solicite ao usuário que digite um CEP (apenas números, sem traço).  
* Acesse a API pública do ViaCEP: "https://viacep.com.br/ws/{cep}/json/".  
* Exiba as seguintes informações: logradouro, bairro, cidade, estado e o próprio CEP.  
* Caso o CEP não exista ou haja erro, informe isso de forma clara ao usuário.  

Dica: Use o módulo `requests` e trate exceções com `try/except`.'''

import urllib.request
import json

def consultar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'

    try:
        with urllib.request.urlopen(url) as resposta:
            dados_json = resposta.read()
            dados = json.loads(dados_json)

            #Verificando a validade do CEP
            if 'erro' in dados:
                print('CEP não encontrado. Tente novamente.')
                return

            #Exibindo os dados
            print('Dados encontrados:')
            print('CEP:', dados.get('cep', ''))
            print('Logradouro:', dados.get('logradouro', ''))
            print('Bairro:', dados.get('bairro', ''))
            print('Cidade:', dados.get('localidade', ''))
            print('Estado:', dados.get('uf', ''))

    except urllib.error.URLError as erro:
        print('Erro ao conectar à API:', erro)
    except Exception as e:
        print('Erro inesperado:', e)

#Parte principal
cep_digitado = input('Digite o CEP (somente números): ').strip()

#Verificando se são só números e se tem oito dígitos
if len(cep_digitado) == 8 and cep_digitado.isdigit():
    consultar_cep(cep_digitado)
else:
    print('CEP inválido. Digite exatamente 8 números.')


