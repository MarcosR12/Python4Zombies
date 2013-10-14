#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Lista 3 de exercicios
'''
5.Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
o algoritmo de Euclides. 
'''
def mdc(n1,n2):
    if n2 == 0:
        return n1
    else:
        return mdc(n2,(n1%n2))

print(mdc(252,105))    
