#!/usr/bin/env python
#_*_ encoding: utf-8 _*_
#Lista 1 de exercicios
#3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
#   Calcule o total em segundos.
def conv2seg (dias,horas,minutos,segundos):
    conversao = {'dias'   :dias*3600*24,
                 'horas'  :horas*3600  ,
                 'minutos':minutos*60  ,
                 'segundos':segundos}
    total = int (conversao['dias'] + conversao['horas'] + conversao['minutos'] + conversao['segundos'])
    print("Conversao - Dias: %d segundos" %conversao['dias'])
    print("Conversao - Horas: %d segundos" %conversao['horas'])
    print("Conversao - Minutos: %d segundos" %conversao['minutos'])
    print("Conversao - Segundos: %d segundos" %conversao['segundos'] )
    print("Total - %d segundos" %total)

d = int (input("Dias: "))
h = int (input("Horas: "))
m = int (input("Minutos: "))
s = int (input("Segundos: "))
conv2seg(d,h,m,s)
