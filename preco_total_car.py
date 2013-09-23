#!/usr/bin/env python
#_*_ encoding: utf-8 _*_
#Lista 1 de exercicios
#9)Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
#   usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
#   sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

def calc(dias,km):
    return float ((dias * 60.00)+(km * 0.15))

km =  float(input ("Quantidade de kilometros rodado: "))
dias = int (input ("Total de dias alugados: "))
print ("Valor total: R$%.2f" %calc(dias,km))

