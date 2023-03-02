"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

fahrenheit = int(input("Digite a temperatura em graus fharenheit: "))

resultado_da_conversao = 5 * ((fahrenheit - 32)/9)
print("O resultado da conversão de {}F° para celsius foi {}°C ".format(fahrenheit, resultado_da_conversao))