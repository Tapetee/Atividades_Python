'''3- Verificador de Senhas Fortes
Crie um programa que avalia a força de uma senha informada pelo usuário. O programa deve:

* Solicitar a senha até que o usuário digite "sair".  
* Verificar se a senha possui pelo menos 8 caracteres.  
* Verificar se contém pelo menos um número.  
* Informar se a senha é fraca ou forte.  
* Encerrar o programa apenas quando a senha for forte ou se o usuário digitar "sair".'''

while True:
#Pedindo a senha do usuário
    senha = input('Digite a senha (ou "sair" para encerrar): ')

#Verificando se o usuário digitou "sair"
    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break

#Verificando o comprimento da senha
    if len(senha) < 8:
        print('Erro - Senha fraca: A senha deve ter pelo menos 8 caracteres.')
        continue

#Verificando se contém pelo menos um número
    possui_numero = False
    for digito in senha:
        if digito.isdigit():
            possui_numero = True
            break

    if not possui_numero:
        print('Erro - Senha fraca: A senha deve conter pelo menos um número.')
        continue

#Se concluiu as verificações, a senha é forte
    print("Senha forte")
    break


