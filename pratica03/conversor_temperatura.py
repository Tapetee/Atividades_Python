'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''

#Criando variáveis
temperatura = float(input('Informe a temperatura atual: '))
unidade_origem = input('Informe a unidade da temperatura de origem (°C, °F ou K): ')
unidade_destino = input('Informe a unidade da temperatura de origem (°C, °F ou K): ')

#Verificando as condições
if unidade_origem == '°C' and unidade_destino == '°F':
    resultado = (temperatura * 9/5) + 32
    print(f'{temperatura}°C = {resultado}°F')
elif unidade_origem == '°C' and unidade_destino == 'K':
    resultado = temperatura + 273.15
    print(f'{temperatura}°C = {resultado}K')
elif unidade_origem == '°F' and unidade_destino == '°C':
    resultado = (temperatura - 32) * 5/9
    print(f'{temperatura}°F = {resultado}°C')
elif unidade_origem == '°F' and unidade_destino == 'K':
    resultado = ((temperatura - 32) * 5/9) + 273.15
    print(f'{temperatura}°F = {resultado}K')
elif unidade_origem == 'K' and unidade_destino == '°C':
    resultado = temperatura - 273.15
    print(f'{temperatura}K = {resultado}°C')
elif unidade_origem == 'K' and unidade_destino == '°F':
    resultado = ((temperatura - 273.15) * 9/5) + 32
    print(f'{temperatura}K = {resultado}°F')