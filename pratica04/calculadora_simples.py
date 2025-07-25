'''1- Calculadora Simples
Crie um programa que simule uma calculadora básica com as seguintes funcionalidades:

* Solicite ao usuário dois números reais.  
* Peça a operação desejada (+, -, *, /).  
* Realize a operação escolhida e exiba o resultado.  
* Trate divisões por zero e operações inválidas com mensagens apropriadas.
O programa deve continuar solicitando entradas até que uma operação válida seja realizada com sucesso. '''

#Uso do while para possibilitar uma repetição dependendo do cenário

while True:
#Entrada dos números
    try:
        numero1 = float(input('Insira o primeiro número: '))
    except ValueError:
        print('Erro - entrada inválida. Insira um número.')
        continue

    try:
        numero2 = float(input('Insira o segundo número: '))
    except ValueError:
        print('Erro - entrada inválida. Insira um número.')
        continue

#Entrada da operação
    operacao = input('Insira a operação (+, -, *, /): ')
    if operacao not in ['+', '-', '*', '/']:
        print('Erro - operação inválida. Tente novamente.')
        continue

    #Realização da operação para tratar os erros
    try:
        if operacao == '+':
            resultado = numero1 + numero2
        elif operacao == '-':
            resultado = numero1 - numero2
        elif operacao == '*':
            resultado = numero1 * numero2
        elif operacao == '/':
            if numero2 == 0:
                raise ZeroDivisionError('Divisão por zero')
            resultado = numero1 / numero2

        print(f'Resultado: {numero1} {operacao} {numero2} = {resultado}')
        break  #Encerra o programa após uma operação correta

    except ZeroDivisionError as erro:
        print(f'Erro - {erro}. Tente novamente.')

