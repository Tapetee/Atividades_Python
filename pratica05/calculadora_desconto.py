'''3- Calculadora de Desconto em Produto
Desenvolva um programa que aplica um desconto sobre o preço de um produto. O programa deve:

* Solicitar o preço original do produto.  
* Solicitar o percentual de desconto desejado.  
* Calcular e exibir o preço final com desconto, arredondado para duas casas decimais.'''

#Criando função
def calcular_desconto():
    preco_original = float(input('Digite o preço original do produto: R$'))
    desconto_percentual = float(input('Digite o percentual de desconto: %'))

    preco_final = preco_original * (1 - desconto_percentual / 100)
   
    print(f'O preço final com desconto é de R$ {preco_final:.2f}')

calcular_desconto()