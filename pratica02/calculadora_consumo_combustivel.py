"""4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais."""

#Criando variáveis
distancia_percorrida = 300
combustivel_gasto = 25

consumo = distancia_percorrida / combustivel_gasto

#Printando resultados
print(f"A distância percorrida foi de {distancia_percorrida} km")
print(f"O combustível gasto foi de {combustivel_gasto} litros")
print(f"O consumo médio foi de {consumo:.2f} km/l")
