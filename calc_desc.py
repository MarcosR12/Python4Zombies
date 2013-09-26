#!/usr/bin/env python
#_*_ encoding: utf-8 _*_
#
#Lista 1 de exercícios
#5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
#   preço a pagar.
def calc(preco,perc):
    desconto = preco*perc/100
    print("Desconto: %d" %desconto)
    print("Total a pagar: %d" %(preco - desconto))

#para simplificar, trabalhando apenas com valores/numeros inteiros :]
preco = int (input("Preço: "))
perc = int(input("Percentual de desconto (%): "))
calc(preco,perc)


