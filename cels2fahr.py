#!/usr/bin/env python
#_*_ encoding: utf-8 _*_
#Lista 1 de exercicios
#7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

def conv(graus):
    return int (9*graus/5 + 32)

graus = int(input("Graus em Celsius: "))
print("%d grau(s) Celsius" %graus + "é equivalente a %d grau(s) Fahrenheit." %conv(graus))
