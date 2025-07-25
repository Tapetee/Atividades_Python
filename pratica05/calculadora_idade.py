'''4- Calculadora de Idade em Dias
Crie um programa que calcula a idade aproximada de uma pessoa em dias. Para isso:

* Solicite o ano de nascimento da pessoa.  
* Considere o ano atual automaticamente.  
* Calcule a idade em anos e transforme em dias (desconsidere anos bissextos).  
* Exiba o resultado final.'''

#Criando a função

def calcular_idade():
    ano_nascimento = int(input('Digite seu ano de nascimento: '))
    ano_atual = 2025

    #Cálculo da idade tendo como o ano atual de referência
    idade_anos = ano_atual - ano_nascimento

    #Cálculo da idade levando em conta os dias do ano
    idade_dias = idade_anos * 365

    print(f'Sua idade em dias é aproximadamente: {idade_dias} dias.') #Ignorando anos bissextos, por isso, "aproximadamente"

calcular_idade()