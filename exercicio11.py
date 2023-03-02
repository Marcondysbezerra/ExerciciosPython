"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a. o produto do dobro do primeiro com metade do segundo .
    c. a soma do triplo do primeiro com o terceiro.
    d. o terceiro elevado ao cubo.
"""

a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))
r = float(input("Digite um número real: "))

ressultado_a = (3 * 2) + (b / 2)
ressultado_b = (a * 3) + r
ressultado_c = r**3

print(f"O produto do dobro do primeito com metade do segundo {ressultado_a}")
print(f"Soma do triplo do primeiro com o terceiro {ressultado_b}")
print(f"O terceiro elevado ao cubo {ressultado_c}")