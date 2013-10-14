#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Lista 3 de exercicios
'''
3.Supondo que a população de um país A seja da ordem de 80000 habitantes
com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes
com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento
'''
def crescAnual(populacao,taxa):
    return populacao + (populacao * taxa)/100
    
def igualandoPop(paisA,paisB):
    ano = 0
    while 1:
        paisA += crescAnual(paisA,3)
        paisB += crescAnual(paisB,1.5)
        ano += 1
        if paisA == paisB or paisA > paisB:
            print("Aee chegamos e demorou %d anos! \o/"%ano)
            break     
igualandoPop(80000,200000)