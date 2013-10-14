#!/usr/bin/env python
#_*_ encoding: utf-8 _*_
#Lista 4 de Exercícios - Desafios
'''
2.Sorteie 20 inteiros entre 1 e 100 numa lista.
Armazene os números pares na lista PAR e
os números ímpares na lista IMPAR. Imprima as três listas.
'''
from random import randint
def num():
    total = []
    pares = []
    impares = []
    for x in range(0,20):
        total.append(randint(1,100))
        if total[x]%2 == 0:
            pares.append(total[x])
        else:
            impares.append(total[x])
    print ("Total: %s - com %d elementos"%(total,len(total))) 
    print ("Pares: %s - com %d elementos"%(pares,len(pares)))
    print ("Impares: %s - com %d elementos"%(impares,len(impares)))
    
num()

        
    
