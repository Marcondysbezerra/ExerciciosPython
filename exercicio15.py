"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    a. salário bruto.
    b. quanto pagou ao INSS.
    c. quanto pagou ao sindicato.
    d. o salário líquido.
    e. calcule os descontos e o salário líquido, conforme a tabela abaixo

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
"""

reais_por_hora  = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = int(input("Quantas horas você trabalhou nesse mês? "))

salario_bruto = reais_por_hora * horas_trabalhadas

imposto_de_renda = salario_bruto * 0.11

inss = salario_bruto * 0.08

sindicato = salario_bruto * 0.05

descontos = [imposto_de_renda, inss, sindicato]
salario_liquido = salario_bruto - sum(descontos)

print("+ Salário Bruto R${:.2f}".format(salario_bruto))
print("- Impsto de Renda R${:.2f}".format(imposto_de_renda))
print("- INSS R${:.2f}".format(inss))
print("- Sindicato R${:.2f}".format(sindicato))
print("= salário Liquido R${:.2f}".format(salario_liquido))