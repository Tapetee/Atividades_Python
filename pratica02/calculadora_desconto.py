"""2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes."""

#Criando variáveis
nome_produto = "Camiseta"
preco_original = 50.00
desconto = 20

calculo_desconto = preco_original * desconto / 100
preco_final = preco_original - calculo_desconto

#Printando resultados
print(f"Produto: {nome_produto}")
print(f"Preço original: R${preco_original:.2f}")
print(f"Porcentagem de desconto: {desconto}%")
print(f"Valor do desconto: R${calculo_desconto:.2f}")
print(f"Preço final: R${preco_final:.2f}")