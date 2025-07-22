"""1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais."""

#Criando variáveis
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

dolar_convertido = valor_reais / taxa_dolar
euro_convertido = valor_reais / taxa_euro

#Mostrando os resultados
print(f"Valor em reais: R${valor_reais:.2f}")
print(f"Valor em dólar: U${dolar_convertido:.2f}")
print(f"Valor em euro: €{euro_convertido:.2f}")