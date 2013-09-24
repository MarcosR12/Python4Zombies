#!/usr/bin/env python   
#_*_ encoding: utf-8 _*_
#Lista 1 de exercicios
#11)Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado
#   a um milhão.

#Apenas para usar com outros valores, vou utilizar uma função... n1^n2. No solicitado 2^1kk
def count(n1,n2):
    return len(str(pow(n1,n2)))

print("Resultado: %d" %count(2,1000000))