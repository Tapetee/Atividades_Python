'''2- Escrita de Arquivo CSV  
Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV. Para isso:

* Crie uma lista de listas com dados fictícios de pelo menos três pessoas.  
* Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.  
* Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.  
* Confirme a gravação exibindo uma mensagem com o nome do arquivo.  
* Trate possíveis erros de escrita de arquivo.

Dica: Use `csv.writer()` para escrever os dados linha por linha.'''

import csv

#Listas com dados de pessoas (nome, idade, cidade)
dados_pessoas = [
    ['Henrique', 25, 'Macaé'],
    ['Lucas', 24, 'Caxias'],
    ['Mariana', 15, 'Fazenda Rio Grande']
]

#Solicita o nome do arquivo CSV ao usuário
nome_arquivo = input('Digite o nome do arquivo CSV: ')

#Cabeçalhos do CSV
cabecalhos = ['Nome', 'Idade', 'Cidade']

try:
    #Abre o arquivo no modo de escrita
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        #Cria o objeto writer
        escritor = csv.writer(arquivo_csv)

        #Escreve os cabeçalhos
        escritor.writerow(cabecalhos)

        #Escreve os dados das pessoas
        escritor.writerows(dados_pessoas)

    #Mensagem de confirmação
    print(f'Dados gravados com sucesso no arquivo: {nome_arquivo}')

except Exception as e:
    #Trata erros de escrita
    print(f'Ocorreu um erro ao tentar gravar o arquivo: {e}')
