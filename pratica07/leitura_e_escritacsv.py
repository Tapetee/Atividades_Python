'''4- Leitura e Escrita de Arquivo JSON  
Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON. Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo. Para isso:

* Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).  
* Solicite ao usuário o nome do arquivo JSON.  
* Salve os dados no arquivo usando o módulo `json`.  
* Após salvar, leia o mesmo arquivo e imprima os dados carregados.  
* Trate possíveis erros como ausência do arquivo ou problemas na escrita.

Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.'''

import json

#Criação de um dicionário com dados
dados_pessoa = {
    'nome': 'Henrique Ferreli',
    'idade': 25,
    'cidade': 'Macaé'
}

#Solicita ao usuário o nome do arquivo JSON
nome_arquivo = input('Digite o nome do arquivo JSON: ')

try:
    #Abre o arquivo JSON no modo de escrita
    with open(nome_arquivo, mode='w', encoding='utf-8') as arquivo_json:
        #Salva os dados no arquivo usando json.dump()
        json.dump(dados_pessoa, arquivo_json, ensure_ascii=False, indent=4)
    
    
    print(f'Dados salvos com sucesso no arquivo: {nome_arquivo}')

    #Lendo o arquivo JSON para verificar os dados salvos
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_json:
        
        dados_carregados = json.load(arquivo_json)
        
        #Exibe os dados carregados
        print('Dados carregados do arquivo:')
        print(dados_carregados)

except FileNotFoundError:
    #Caso o arquivo não seja encontrado
    print(f'O arquivo "{nome_arquivo}" não foi encontrado.')

except Exception as e:
    #Captura outros erros
    print(f'Ocorreu um erro: {e}')
