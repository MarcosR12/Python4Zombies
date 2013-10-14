#!/usr/bin/env python
#_*_ encoding: utf-8 _*_
#Lista 3 de Exercícios - Desafios
'''
1.Dizemos que um número natural é triangular se ele é produto de três números naturais
consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120.
Dado um inteiro não-negativo n, verificar se n é triangular.

Fórmula wikipedia: 
frac{T_n * (T_n+1)}{2} = Resultado (1+2+3+4+...+n)
'''
def geraTriangular(num):
    return int((num * (num +1))/2)

def valida(num):
    if ((num -1) * ( (num-1) -1)) * ( ( (num-1) -1) -1) == num:
        return True
    else:
        return valida(num -3)

print(valida(120))
    
a * (a+1) * ((a+1)+1)
((a+1)+1) * (a+1)+1)+1 * (((a+1)+1)+1)+1