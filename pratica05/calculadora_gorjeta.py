'''1- Calculadora de Gorjeta
Crie um programa que calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida. Use as instruções abaixo:

* Defina o valor da conta (ex: R$ 100,00).  
* Informe a porcentagem da gorjeta (ex: 10%, 15%, 20%).  
* O programa deve calcular o valor correspondente e exibir o resultado com duas casas decimais.'''

#Criando a função
def calcular_gorjeta():
    try:
        valor_conta = float(input('Digite o valor da conta: R$'))
        valor_porcentagem = float(input('Digite a porcentagem da gorjeta: %'))

        #Calculando o valor da gorjeta
        gorjeta = valor_conta * (valor_porcentagem / 100)
        print(f'O valor da gorjeta é de (R${valor_porcentagem}%): R$ {gorjeta:.2f}')

    except ValueError:
        print('Insira um valor válido')
calcular_gorjeta()