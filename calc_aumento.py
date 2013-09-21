#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
#Lista 1 de exercicios
#4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
#   porcentagem do aumento. Exiba o valor do aumento e do novo salário.
def calc(sal,aum):
    return sal+(sal*aum/100) 
sal = int (input("Digite o seu salário: "))
aum = int (input("Digite o percentual de aumento: "))
print ("Seu salário final é %d, parabéns!(ou não)" %calc(sal,aum))

