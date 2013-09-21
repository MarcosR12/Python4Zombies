#!/usr/bin/env python
#_*_ encoding: utf-8 _*_
#Lista 1 de exercicios
#6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
#   esperada para a viagem.
def calc(dist,vel):
    if dist/vel <= 0:
        print ("É rapido, não vai gastar nem uma hora...")
    else:
        print("Tempo estimado: %.1f hora(s)" %float(dist/vel))
        
dist = int (input("Distancia (Km): "))
vel = int (input("Velocidade Média (Km/h): "))
calc(dist,vel)


