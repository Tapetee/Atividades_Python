'''2- Gerador de Usuário Aleatório  
Crie um programa que acessa uma API pública e exibe informações de um usuário fictício. Para isso:

* Use a API pública "https://randomuser.me/api/" para obter dados aleatórios.  
* Mostre na tela: nome completo, e-mail e país do usuário.  
* O programa deve tratar possíveis erros de conexão ou falha na API.  

Dica: Utilize o módulo `requests` para fazer a requisição e o método `.json()` para acessar os dados.'''

import urllib.request
import json

def gerar_usuario():
    try:
        with urllib.request.urlopen("https://randomuser.me/api/") as resposta:
            dados_json = resposta.read()
            dados = json.loads(dados_json)
            usuario = dados['results'][0]

            nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
            email = usuario['email']
            pais = usuario['location']['country']

            print("Usuário gerado com sucesso:")
            print("Nome:", nome_completo)
            print("E-mail:", email)
            print("País:", pais)

    except urllib.error.URLError as erro:
        print("Erro ao conectar à API:", erro)
    except Exception as e:
        print("Erro inesperado:", e)

gerar_usuario()