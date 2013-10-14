#!/usr/bin/env python
#_*_ encoding: utf-8 _*_
#Lista 3 de Exercícios - Desafios
'''
5.Faça um programa que peça um inteiro positivo e o mostre invertido.
Ex.: 1234 gera 4321
'''
def invertido(num):
    saida = []
    for x in reversed(list(str(num))):
        saida+=x
    print("%s"%saida)
invertido(100)

    




