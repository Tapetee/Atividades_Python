'''1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o 
em uma das seguintes categorias: 

*Criança (0-12 anos), 
*Adolescente (13-17 anos), 
*Adulto (18-59 anos) ou 
*Idoso (60 anos ou mais).'''

#Pedindo para o usuário digitar a idade
idade = int(input("Informe a sua idade:"))

#Estabelecendo condições
if idade >= 60:
    print (f'Você tem {idade} anos e é idoso')
elif idade >= 18:
    print(f'Você tem {idade} anos e é adulto')
elif idade >= 13:
    print(f'Você tem {idade} anos e é adolescente')
elif idade >= 0:
    print(f'Você tem {idade} anos e é criança')


