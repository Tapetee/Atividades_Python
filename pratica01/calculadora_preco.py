'''4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. 
* Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3

* O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.'''

#Criando variáveis
nome_produto = 'Cadeira Infantil'
preco_unitario = 12.40
quantidade = 3
preco_final = preco_unitario * quantidade

#Printando os resultados
print('Produto:', nome_produto)
print(f'Preço Unitário: R$ {preco_unitario:.2f}')
print('Quantidade:', quantidade)
print(f'Preço Total: R$ {preco_final:.2f}')

