'''Gerador de Senhas Seguras  
Crie um programa que gera senhas aleatórias com letras, números e caracteres especiais. Siga as instruções abaixo:

* Solicite ao usuário o tamanho da senha desejada (por exemplo: 8, 12, 16 caracteres).  
* A senha gerada deve conter letras maiúsculas, minúsculas, números e símbolos (ex: !@#$%&*).  
* Exiba a senha gerada ao final do programa.  

Dica: Use os módulos `random` e `string` para gerar os caracteres aleatórios.'''

import random
import string

def gerar_senha(tamanho):
    if tamanho < 4:
        print('A senha precisa ter pelo menos 4 dígitos')
        return None

    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = '!@#$%&*'

    # Certificar-se de que vai ter pelo menos um dos tipos
    senha = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    # Linha para sugerir senha forte ao usuário
    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos
    senha += random.choices(todos_caracteres, k=tamanho - 4)
    random.shuffle(senha)

    return ''.join(senha)  # <- aqui está corretamente indentado DENTRO da função

try:
    tamanho = int(input('Digite sua senha (mínimo 4 caracteres): '))
    senha_gerada = gerar_senha(tamanho)
    if senha_gerada:
        print('Senha gerada:', senha_gerada)
except ValueError:
    print('Crie uma senha mais forte.')

    

