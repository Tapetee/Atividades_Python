'''Registro de Notas e Cálculo da Média
Desenvolva um programa para registrar notas de uma turma e calcular a média final. Siga as instruções abaixo:

* O programa deve solicitar notas continuamente até o usuário digitar "fim".  
* Somente notas entre 0 e 10 devem ser aceitas.  
* Ao final, exiba a média da turma com duas casas decimais e o total de notas válidas registradas.  
* Trate entradas inválidas com mensagens de erro.'''

#Criando variáveis
nota_total = 0
quantidade_notas = 0

while True:
    entrada = input('Registre uma nota (ou "fim" para terminar): ')
    
    #Se o usuário digitar "fim", vai encerrar o loop
    if entrada.lower() == 'fim': 
        break
    
    try:
        nota = float(entrada)

      #Para verificar se a nota está entre 0 e 10  
        if 0 <= nota <= 10:  
            nota_total += nota
            quantidade_notas += 1
        else:
            print('Erro - a nota deve estar entre 0 e 10.')
    except ValueError:
        print('Erro - entrada inválida. Insira uma nota numérica válida.')

#Cálculo e exibição da média
if quantidade_notas > 0:
    media = nota_total / quantidade_notas
    print(f'Média da turma: {media:.2f}')
    print(f'Total de notas válidas registradas: {quantidade_notas}')
else:
    print('Nenhuma nota válida foi registrada.')
