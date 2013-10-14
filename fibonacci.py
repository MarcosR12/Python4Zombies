#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Lista 3 de exercicios
'''
4.A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o
seu númerode Fibonacci. F1= 1, F2= 1, F3= 2, etc.
'''
def fibonacci():
    a,b = 1,1
    saida = "0 1"
    while len(saida) < 100:
        soma = b+a
        a = b
        b = soma
        saida += " "+str(b)
    return saida
print (fibonacci())



