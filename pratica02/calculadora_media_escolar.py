"""3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais."""

#Criando variáveis
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

#Printando resultados
print(f"A sua primeira nota foi {nota1:.2f}")
print(f"A sua segunda nota foi {nota2:.2f}")
print(f"A sua terceira nota foi {nota3:.2f}")
print(f"Portanto, sua média final é: {media:.2f}")