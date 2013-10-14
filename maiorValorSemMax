#!/usr/bin/env python
#_*_ encoding: utf-8 _*_
#Lista 4 de Exercícios - Desafios
'''
1.Sorteie 10 inteiros entre 1 e 100 para uma lista
e descubra o maior e o menor valor, sem usar as funções max e min.
'''
import random
def geraLista(lista):
    for x in range(0,10):
        lista.append(random.randint(1,100))
    return lista

def maxMin():
    lista = []
    geraLista(lista)
    maior,menor = lista[0],lista[0]
    for x in range(0,10):
        if lista[x] > maior:
            maior = lista[x]
        if lista[x] < menor:
            menor = lista[x]
    return maior,menor

print(maxMin())


