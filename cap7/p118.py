#!/usr/bin/python
# -*- coding: utf-8 -*-

""" >
Ejemplo de decorador
"""
def decorador(funcion_entrada):
    def funcion_salida():
        funcion_entrada()
        print "Esto no estaba en la función original"
    return funcion_salida

@decorador
def saludo():
    print "Hola"

saludo()
