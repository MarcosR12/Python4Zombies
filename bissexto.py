#!/usr/bin/env python
#_*_ encoding: utf-8 _*_
#Lista 2 de exercicios
#Determine se um ano é bissexto

def verif(ano):
    if ano%4 == 0:
        #verifica qts digitos tem o ano informado e verifica se os 2 ultimos são == 00
        if str(ano)[len(str(ano))-1] != '0' and str(ano)[len(str(ano))-2] != '0':
            print("Ano Bissexto")
        elif str(ano)[len(str(ano))-1] == '0' and str(ano)[len(str(ano))-2] == '0':
            if ano%400 == 0:
                print("Ano Bissexto")
            else:
                print("Ano Normal")
        else:
            print("Ano Normal")
    else:
        print("Ano Normal")

verif(2020)      
