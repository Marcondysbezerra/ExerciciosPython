# Faça um Programa que peça dois números e imprima a soma.

numero_1 = int(input('Primeiro número: '))
numero_2 = int(input('Segundo número: '))

soma = numero_1 + numero_2
print("O resultado da soma entre os números {} e {} foi {}.".format(numero_1, numero_2, soma))
print("O resultado da soma entre os números {1} e {2} foi {0}.".format(soma, numero_1, numero_2))
print(f"O resultado da soma entre os números {numero_2} e {numero_1} foi {soma}")