#!/usr/bin/env python
#_*_ encoding: utf-8 _*_
#Lista 1 de exercicios
#10)Escreva um programa para
#  calcular a redução do tempo de vida de um fumante. Pergunte a
#  quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
#  perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
#  total de dias.

def calc(cigPdia,anos):
    #minutos perdidos por dia. Se o cigPdia for => 140, a pessoa que testou é um zumbi. 1 dia = 1440 min.
    
    #Tempo em minutos perdido por dia pelo fumante
    minPerCig = cigPdia * 10

    #Tempo em dias que a pessoa fuma
    diasFumados = anos * 365

    #Tempo perdido no total de dias que a pessoa
    return int ((minPerCig * diasFumados) / 1440)
    
cig = int ( input("Numero de cigarros fumados por dia: "))    
anos = int ( input("Há quantos anos você fuma?: "))
print("Voce ja perdeu %d dias da sua vida..." %calc(cig,anos))
