'''2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"'''

#Criando variáveis
peso = int(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura * altura)

#Estabelecendo condições
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Você está no peso normal')
elif imc < 30:
    print('Você está um pouco acima do peso')
else:
    print('Você está obeso')