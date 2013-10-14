#!/usr/bin/env python
#_*_ encoding: utf-8 _*_
#Lista 2 de exercicios
#1.Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
#  um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
"""
1) Eqüilátero: possui três lados iguais, ou seja, congruentes.
 Todos os seus ângulos internos medem 60º (são congruentes), assim, ele é também um eqüiângulo.
--
2) Escaleno: não possui os três lados congruentes, assim, todos os lados e ângulos são diferentes.
--
3) Isósceles: possui dois lados e dois ângulos adjacentes à base congruentes.
 Possui pelo menos dois lados de mesma medida e dois ângulos congruentes.
--
Fonte: http://www.fontedosaber.com/matematica/triangulos-definicao-elementos-e-classificacao.html
"""
#Verifica se eh um triangulo
def verifTri(a,b,c):
    if (b - c) < a and a < (b + c):
        return True
    else:
        return False

#devolve a classificação do triângulo
def classTri(a,b,c):
    if verifTri(a,b,c):
        if a == b and a == c:
            return "Eqüilátero"
        elif a == b or a == c or b == c:
            return "Escaleno"
        elif a != b and a != c and b != c:
            return "Isósceles"
    else:
        return "Valores inválidos para um triângulo."
    
print (classTri(1,100,1))            
        

        

        
        






