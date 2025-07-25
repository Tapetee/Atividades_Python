'''4- Analisador de Números Pares e Ímpares
Desenvolva um programa que classifica números inteiros como pares ou ímpares. O programa deve:

* Solicitar números inteiros até que o usuário digite "fim".  
* Informar se o número digitado é par ou ímpar.  
* Ao final, exibir a quantidade total de números pares e ímpares informados.  
* Tratar entradas inválidas com mensagens de erro apropriadas. '''

#Criando as variáveis
num_par = 0
num_impar = 0

while True:
    #Pedir número ao usuário
    numero_entrada = input('Digite um número inteiro (ou "fim" para encerrar): ')

    #Avaliar se o usuário vai encerrar ou não o programa
    if numero_entrada.lower() == 'fim':
        break

    #Tentar converter a entrada para um número inteiro
    try:
        numero = int(numero_entrada)

        #Agora, verificar se o número é par ou ímpar
        if numero % 2 == 0:
            print(f'{numero} é par')
            num_par += 1
        else:
            print(f'{numero} é ímpar')
            num_impar += 1
    except ValueError:
        print('Erro - Digite um número inteiro válido') #Erro para quando o usuário digitar eventualmente um número que não seja inteiro

#Mostrar os números totais tanto pares, quanto ímpares
print(f'Total de números pares: {num_par}')
print(f'Total de números ímpares: {num_impar}')