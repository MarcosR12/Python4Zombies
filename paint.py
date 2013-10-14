#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
7.Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total.
Obs. : somente são vendidos um número inteiro de latas.
"""

def paint(metrosQuad):
    #Quantas latas serão utilizadas
    totalLatas = int(metrosQuad / 18)
    precoTotal = totalLatas * 80
    return print("Total de latas utilizadas: %d \n Preco Total: R$ %d,00" %(totalLatas,precoTotal))

paint(100)
   