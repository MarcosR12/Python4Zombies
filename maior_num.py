#!/usr/bin/env python
#_*_ encoding: utf-8 _*_
"""
Lista 2 de exercicios
4.Faça um Programa que leia três números e mostre o maior deles.
5.Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
def maiorNum(n1,n2,n3):
    return max(n1,n2,n3)

assert maiorNum(1,2,3) == 3

def menorNum(n1,n2,n3):
    return min(n1,n2,n3)

assert menorNum(1,2,3) == 1

#the end
print("Maior numero: %d \nMenor numero: %d" %(maiorNum(1,2,3),menorNum(1,2,3)))