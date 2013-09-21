#!/usr/bin/env python
#_*_ encoding: utf-8 _*_
#Lista 1 de exercicios
#Exercicio 2) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
def convMet2Mil(mt):
    return (mt*1000)

metros = int(input("Metros: "))
print ("Resultado: %d milímetros" %convMet2Mil(metros))

