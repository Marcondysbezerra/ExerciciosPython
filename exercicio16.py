"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
import math

area = int(input("Digite o tamanho da parede em m²: "))
lata_litros = 18
preco_lata = 80

cobertura = area/3
latas = math.ceil(cobertura/lata_litros)
valor = latas * preco_lata

print("Para pintar {}m², você precisa de {}L de tinta que lhe custará R${}.".format(area, latas, valor))