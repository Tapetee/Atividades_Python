'''3- Leitura de Arquivo CSV  
Desenvolva um programa que lê os dados de um arquivo CSV e imprime cada linha na tela. Para isso:

* Solicite ao usuário o nome do arquivo CSV a ser lido.  
* Utilize o módulo `csv` para abrir o arquivo e ler os dados.  
* Exiba cada linha completa como uma lista.  
* Trate erros como arquivo inexistente ou problemas na leitura.

Dica: Use `csv.reader()` para ler e percorrer as linhas do arquivo.'''

import csv

#Solicita o nome do arquivo CSV
nome_arquivo = input('Digite o nome do arquivo CSV a ser lido: ')

try:
    #Abre o arquivo no modo de leitura
    with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
        #Cria o objeto reader
        leitor = csv.reader(arquivo_csv)

        #Lê e imprime cada linha do arquivo
        for linha in leitor:
            print(linha)

except FileNotFoundError:
    
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")

except Exception as e:
    
    print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")
