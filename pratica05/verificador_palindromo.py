'''2- Verificador de Palíndromos
Crie um programa que verifica se uma palavra ou frase é um palíndromo, ou seja, se pode ser lida da mesma forma de trás para frente, desconsiderando espaços, acentos e pontuação. Para isso:

*Solicite ao usuário uma palavra ou frase.
*Desconsidere letras maiúsculas, espaços e sinais de pontuação.
*Verifique se a frase é um palíndromo.
*Exiba "Sim" se for palíndromo ou "Não" se não for.

Exemplo: A frase "A cara rajada da jararaca" deve ser reconhecida como um palíndromo.'''

#Criando função
def verificar_palindromo():
    palavra = input('Digite uma palavra: ')
    palavra_vazia = ''

    #Loop para retirar espaços, pontuação e deixar minúsculo
    for letra in palavra:
        if letra.isalpha():
            palavra_vazia += letra.lower()
    
    #Verificador da palavra
    if palavra_vazia == palavra_vazia [::-1]:
        print('Sim')
    else:
        print('Não')

verificar_palindromo()