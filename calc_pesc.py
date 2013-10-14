#!/usr/bin/env python
#_*_ encoding: utf-8 _*_
#Lista 2 de exercicios
"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de
seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do
estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você
faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na
variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais
variáveis com o conteúdo ZERO.
"""
def contrl(peso):
    multa = 0
    excesso = 0
    if peso > 50:
        excesso = peso - 50
        multa = excesso * 4
    print ("Excedente: %d\n" %excesso +
           "Multa: %d\n" %multa)
#teste
contrl(10)
