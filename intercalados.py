#!/usr/bin/env python
#_*_ encoding: utf-8 _*_
#Lista 4 de Exercícios
'''
3.Faça um programa que crie dois vetores com 10 elementos
aleatórios entre 1 e 100. Gere um terceiro
vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
intercalados dos dois outros vetores.Imprima os três vetores.
'''
from random import randint
def intercalados():
    v1 = []
    v2 = []
    v3 = []
    for x in range(0,10):
        v1.append(randint(1,100))
        v2.append(randint(1,100))
        v3.append(v1[x])
        v3.append(v2[x])
    return v1,v2,v3
print(intercalados())

