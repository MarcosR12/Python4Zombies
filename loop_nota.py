#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Lista 3 de exercicios
'''
1.Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário informe um valor válido.
'''
def nota():
    while 1:
        msg="Apenas valores entre 0 e 10"
        try:
            nota = int (input("Digite uma nota entre 0 e 10: "))
            if nota not in range(0,11):
                print(msg)
        except:
            print(msg)
nota()