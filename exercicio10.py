"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""

celsius = int(input("Digite a temperatura em graus Celsius: "))

resultado_da_conversao = (celsius * 1.8) + 32
print("Resultado: {}".format(resultado_da_conversao))