#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Lista 3 de exercicios
'''
2.Faça um programa que leia um nome de
usuário e a sua senha e não aceite a senha igual ao
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''
def dados():
    while 1:
        user = input("Nome de usuário :")
        password = input("Senha: ")
        if password == user:
            input("A senha nao pode ser igual ao usuário!")
            
