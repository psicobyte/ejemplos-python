#!/usr/bin/python
# -*- coding: utf-8 -*-
def tabla_multiplicar(nombre, numero = 1):
    print "Tabla de multiplicar del " + str(numero)
    print "Impresa automáticamente por " + nombre
    i = 0
    while i < 11:
        print str(numero) + " X " + str(i) + " = " + str(numero * i)
        i += 1

tabla_multiplicar("Pablo")
