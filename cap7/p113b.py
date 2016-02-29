#!/usr/bin/python
# -*- coding: utf-8 -*-

def compara_numeros(n1, n2):
    """
    Recibe como parámetros dos números

    retorna:
    1 si el primero es mayor
    2 si el segundo es mayor
    0 si son iguales
    """

    if (n1 > n2):
        return 1
    elif (n1 < n2):
        return 2
    else:
        return 0

def tabla_multiplicar(numero):
    """Recibe un número e imprime su tabla de multiplicar"""

    print "Tabla del " + str(numero)
    i = 1
    while i < 11:
        print str(numero) + " X " + str(i) + " = " + str(i * numero)
        i += 1
