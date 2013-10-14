#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Lista 2 de exercicios
6.Faça um Programa que pergunte quanto você
ganha por hora e o número de horas trabalhadas no mês. Calcule
e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, q
uanto pagou ao INSS,quanto pagou ao sindicato e o salário líquido.
Observe que Salário bruto - Descontos = Salário Líquido.
 Calcule osdescontos e o salário líquido, conforme a tabela abaixo:
a.+ Salário salario : R$
b.-IR (11%) : R$
c.-INSS (8%) : R$
d.-Sindicato ( 5%) : R$
e.= Salário Liquido : R$
'''
#Calcula desconto
def desc(n1,n2):
    return (n1 * n2)/100

#Recebe um valor parago por hora e um total de horas trabalhado
def salario(vlHr,ttlHr):
    salario = vlHr * ttlHr
    print("Salario salario: R$%.2f "%(salario))
    print("Imposto de Renda: R$%.2f"%desc(salario,11))
    salario -= desc(salario,11)
    print("INSS: R$%.2f" %desc(salario,8))
    salario -= desc(salario,8)
    print("Sindicato: R$%.2f" %desc(salario,5))
    salario -= desc(salario,5)
    print("Salario Liquido: R$%.2f" %salario)
    
salario(100,10)
